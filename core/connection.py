"""Connection management for WebSocket clients and Pipecat processes."""

import subprocess
from typing import Dict, List, Optional, Tuple

from fastapi import WebSocket

from meetingbaas_pipecat.utils.logger import logger

# Global dictionary to store meeting details for each client
MEETING_DETAILS: Dict[
    str, Tuple[str, str, Optional[str], bool, str]
] = {}  # client_id -> (meeting_url, persona_name, meetingbaas_bot_id, enable_tools, streaming_audio_frequency)

# Global dictionary to store Pipecat processes
PIPECAT_PROCESSES: Dict[str, subprocess.Popen] = {}  # client_id -> process


class ConnectionRegistry:
    """Manages WebSocket connections for clients and Pipecat."""

    def __init__(self, logger=logger):
        self.client_input_connections: Dict[str, WebSocket] = {}
        self.client_output_connections: Dict[str, WebSocket] = {}
        self.pipecat_connections: Dict[str, WebSocket] = {}
        self.logger = logger

    async def connect(
        self,
        websocket: WebSocket,
        client_id: str,
        is_pipecat: bool = False,
        client_direction: Optional[str] = None,
    ):
        """Register a new connection."""
        await websocket.accept()
        if is_pipecat:
            already_exists = client_id in self.pipecat_connections
            self.pipecat_connections[client_id] = websocket
            self.logger.info(
                f"Pipecat client {client_id} connected (replaced existing: {already_exists})"
            )
        else:
            direction = client_direction or "output"
            if direction == "input":
                already_exists = client_id in self.client_input_connections
                self.client_input_connections[client_id] = websocket
                self.logger.info(
                    f"Client {client_id} INPUT connected (replaced existing: {already_exists})"
                )
            else:
                already_exists = client_id in self.client_output_connections
                self.client_output_connections[client_id] = websocket
                if client_direction is None:
                    self.logger.warning(
                        f"Client {client_id} connected without direction; treating as OUTPUT"
                    )
                self.logger.info(
                    f"Client {client_id} OUTPUT connected (replaced existing: {already_exists})"
                )

    async def disconnect(
        self,
        client_id: str,
        is_pipecat: bool = False,
        client_direction: Optional[str] = None,
    ):
        """Remove a connection and close the websocket."""
        try:
            # First, remove the connection from our dictionaries before attempting to close it
            if is_pipecat:
                if client_id in self.pipecat_connections:
                    websocket = self.pipecat_connections.pop(client_id)
                    # Try to close it if possible
                    try:
                        await websocket.close(code=1000, reason="Bot disconnected")
                    except Exception as e:
                        # It's normal for this to fail if the connection is already closed
                        self.logger.debug(
                            f"Could not close Pipecat WebSocket for {client_id}: {e}"
                        )
                    self.logger.info(f"Pipecat client {client_id} disconnected")
            else:
                directions = (
                    [client_direction]
                    if client_direction in ["input", "output"]
                    else ["input", "output"]
                )
                for direction in directions:
                    if direction == "input" and client_id in self.client_input_connections:
                        websocket = self.client_input_connections.pop(client_id)
                        try:
                            await websocket.close(code=1000, reason="Bot disconnected")
                        except Exception as e:
                            self.logger.debug(
                                f"Could not close client INPUT WebSocket for {client_id}: {e}"
                            )
                        self.logger.info(f"Client {client_id} INPUT disconnected")
                    if direction == "output" and client_id in self.client_output_connections:
                        websocket = self.client_output_connections.pop(client_id)
                        try:
                            await websocket.close(code=1000, reason="Bot disconnected")
                        except Exception as e:
                            self.logger.debug(
                                f"Could not close client OUTPUT WebSocket for {client_id}: {e}"
                            )
                        self.logger.info(f"Client {client_id} OUTPUT disconnected")
        except Exception as e:
            # This should rarely happen now, but just in case
            self.logger.debug(f"Error during disconnect for {client_id}: {e}")

    def get_client_input(self, client_id: str) -> Optional[WebSocket]:
        """Get the client INPUT connection (server -> meeting)."""
        return self.client_input_connections.get(client_id)

    def get_client_output(self, client_id: str) -> Optional[WebSocket]:
        """Get the client OUTPUT connection (meeting -> server)."""
        return self.client_output_connections.get(client_id)

    def get_client(self, client_id: str) -> Optional[WebSocket]:
        """Backward-compatible: return INPUT, else OUTPUT if present."""
        client = self.get_client_input(client_id)
        if client:
            return client
        return self.get_client_output(client_id)

    def get_pipecat(self, client_id: str) -> Optional[WebSocket]:
        """Get a Pipecat connection by ID."""
        return self.pipecat_connections.get(client_id)


# Create a singleton instance
registry = ConnectionRegistry()
