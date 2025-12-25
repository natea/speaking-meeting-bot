# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Speaking Meeting Bot is an AI-powered meeting agent system that enables voice-interactive bots to join Google Meet, Microsoft Teams, and Zoom meetings. The system combines:
- **Pipecat** - AI framework for real-time voice conversations
- **MeetingBaas** - Meeting platform integration API
- **OpenAI GPT-4** - Language model for bot intelligence
- **Cartesia** - Text-to-speech synthesis
- **Deepgram/Gladia** - Speech-to-text transcription
- **FastAPI** - REST API and WebSocket server

## Common Commands

```bash
# Install dependencies
poetry install

# Compile Protocol Buffers (required after proto changes)
poetry run python -m grpc_tools.protoc --proto_path=./protobufs --python_out=./protobufs frames.proto

# Run the server (standard mode)
poetry run uvicorn app:app --reload --host 0.0.0.0 --port 7014

# Run in local dev mode with ngrok auto-configuration
poetry run python app/main.py --local-dev --port 7014

# Format code
ruff format .

# Lint code
ruff check .
```

## Architecture

```
FastAPI Server (app/main.py:7014)
├── HTTP Routes (app/routes.py)
│   ├── POST /bots - Create bot and join meeting
│   ├── DELETE /bots/{bot_id} - Remove bot from meeting
│   └── POST /personas/generate-image - Generate AI avatar
├── WebSocket Routes (app/websockets.py)
│   ├── /ws/{client_id} - MeetingBaas audio streaming
│   └── /pipecat/{client_id} - Pipecat service connection
└── Core Components (core/)
    ├── connection.py - ConnectionRegistry, MEETING_DETAILS, PIPECAT_PROCESSES
    ├── process.py - Pipecat subprocess management
    └── router.py - Audio message routing
```

### Request Flow
1. Client calls `POST /bots` with meeting URL and persona
2. Server resolves persona, generates WebSocket URL, calls MeetingBaas API
3. Pipecat subprocess spawned (`scripts/meetingbaas.py`)
4. MeetingBaas bot joins meeting, connects to `/ws/{client_id}`
5. Pipecat connects to `/pipecat/{client_id}`
6. Audio streams: Client -> STT (Deepgram) -> LLM (OpenAI) -> TTS (Cartesia) -> Client

### Key Data Stores (In-Memory)
- `MEETING_DETAILS` - Bot metadata indexed by client_id
- `PIPECAT_PROCESSES` - Subprocess tracking for cleanup

## Persona System

Personas are stored in `config/personas/{persona_name}/`:
```
persona_name/
├── README.md          # Main definition with metadata (image, voice_id, entry_message)
└── *.md              # Additional knowledge/behavior files
```

Persona loading is handled by `config/persona_utils.py` via `PersonaManager` class. The README.md contains YAML-like metadata section with `image`, `entry_message`, `cartesia_voice_id`, `gender`, `relevant_links`.

## Code Style

- **Formatter**: Ruff (line length 88 per pyproject.toml)
- **Style Guide**: Google Python Style Guide
- **Type hints**: Required for public APIs
- **Docstrings**: Google-style format
- **Indentation**: 4 spaces (no tabs)
- **Imports**: Grouped (future, stdlib, third-party, local), sorted lexicographically

## Key Files

| File | Purpose |
|------|---------|
| [app/main.py](app/main.py) | FastAPI app setup, server entry point |
| [app/routes.py](app/routes.py) | HTTP endpoints including bot creation/removal |
| [app/websockets.py](app/websockets.py) | WebSocket handlers for audio streaming |
| [core/connection.py](core/connection.py) | WebSocket connection registry and state |
| [core/process.py](core/process.py) | Pipecat subprocess spawning and termination |
| [scripts/meetingbaas.py](scripts/meetingbaas.py) | Pipecat audio pipeline (STT->LLM->TTS) |
| [scripts/meetingbaas_api.py](scripts/meetingbaas_api.py) | MeetingBaas REST API wrapper |
| [config/persona_utils.py](config/persona_utils.py) | Persona loading and management |
| [config/voice_utils.py](config/voice_utils.py) | Cartesia voice matching via OpenAI |
| [protobufs/frames.proto](protobufs/frames.proto) | Protocol buffer definitions for Pipecat |

## Environment Variables

Required:
- `MEETING_BAAS_API_KEY` - MeetingBaas API key
- `OPENAI_API_KEY` - OpenAI API key for LLM
- `CARTESIA_API_KEY` - Cartesia TTS API key
- `DEEPGRAM_API_KEY` or `GLADIA_API_KEY` - STT service

Optional:
- `BASE_URL` - WebSocket base URL (critical for production)
- `REPLICATE_KEY` - AI image generation
- `UTFS_KEY` / `APP_ID` - UploadThing image hosting
- `NGROK_AUTHTOKEN` - Local development tunneling

## WebSocket URL Resolution Priority

1. User-provided URL in request
2. `BASE_URL` environment variable (recommended for production)
3. ngrok URL detection in local dev mode
4. Auto-detection from request headers (fallback)

## API Authentication

All protected endpoints require header: `x-meeting-baas-api-key`

## Troubleshooting

### Common Issues

**Poetry not found on Windows:**
If `poetry` command is not recognized, use the virtual environment directly:
```powershell
.\.venv\Scripts\python.exe -m uvicorn app:app --host 0.0.0.0 --port 7014
```

**ModuleNotFoundError: No module named 'config':**
This was fixed in `core/process.py` by setting PYTHONPATH for the subprocess. If it recurs, verify that:
- `process.py` sets `env["PYTHONPATH"] = project_root`
- The subprocess runs with `cwd=project_root`

**ImportError: cannot import name 'TaskManager' from 'pipecat.utils.asyncio':**
This occurs with pipecat version 0.0.98 which doesn't have TaskManager. Fixed in `scripts/meetingbaas.py` by wrapping the import in try/except.

**Protobuf version mismatch (gencode vs runtime):**
Regenerate protobuf files:
```bash
.\.venv\Scripts\python.exe -m grpc_tools.protoc --proto_path=./protobufs --python_out=./protobufs frames.proto
```

**Old bots keep reconnecting after server restart:**
MEETING_DETAILS is in-memory and cleared on restart. Old MeetingBaas bots will fail with "No meeting details found". Remove them via the MeetingBaas dashboard or wait for them to timeout.

**Deepgram SDK version mismatch:**
If you see `ImportError: cannot import name 'AsyncListenWebSocketClient' from 'deepgram'`, upgrade pipecat-ai:
```bash
.\.venv\Scripts\pip.exe install --upgrade "pipecat-ai[cartesia,deepgram,openai,silero,websocket]"
```

### Debugging Pipecat Subprocess

Pipecat subprocess logs appear with `[Pipecat STDOUT]` and `[Pipecat STDERR]` prefixes in the server output. If you don't see these:
1. Ensure `-u` flag is passed to Python for unbuffered output (in `core/process.py`)
2. Check that PYTHONPATH is set correctly
3. Run the script directly to see immediate errors:
   ```powershell
   $env:PYTHONPATH="C:\Users\kmond\meeting bot\speaking-meeting-bot"
   .\.venv\Scripts\python.exe scripts/meetingbaas.py --help
   ```

### Version Compatibility

Tested with:
- Python 3.11+
- pipecat-ai 0.0.98 (note: some newer features require manual compatibility fixes)
- deepgram-sdk 4.7.0
- protobuf 5.x (runtime)
