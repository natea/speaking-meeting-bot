"""Startup validation and API connectivity checks for Speaking Meeting Bot."""

import os
import sys
from typing import Dict, List, Tuple

import httpx
from loguru import logger


def validate_env_vars() -> List[str]:
    """
    Validate that all required environment variables are set.

    Returns:
        List of error messages for missing variables (empty if all valid).
    """
    errors = []

    # Core required variables
    required_vars = [
        ("MEETING_BAAS_API_KEY", "MeetingBaas API - required for bot creation"),
        ("OPENAI_API_KEY", "OpenAI API - required for LLM interactions"),
        ("CARTESIA_API_KEY", "Cartesia API - required for text-to-speech"),
    ]

    for var_name, description in required_vars:
        value = os.getenv(var_name)
        if not value or value.startswith("your_"):
            errors.append(f"Missing {var_name}: {description}")

    # STT provider - need at least one
    deepgram_key = os.getenv("DEEPGRAM_API_KEY")
    gladia_key = os.getenv("GLADIA_API_KEY")

    deepgram_valid = deepgram_key and not deepgram_key.startswith("your_")
    gladia_valid = gladia_key and not gladia_key.startswith("your_")

    if not deepgram_valid and not gladia_valid:
        errors.append(
            "Missing STT provider: Set DEEPGRAM_API_KEY or GLADIA_API_KEY"
        )

    return errors


def validate_personas() -> Tuple[bool, int, List[str]]:
    """
    Validate that personas directory exists and contains valid personas.

    Returns:
        Tuple of (is_valid, persona_count, persona_names)
    """
    from pathlib import Path

    personas_dir = Path(__file__).parent / "personas"

    if not personas_dir.exists():
        return False, 0, []

    persona_names = []
    for item in personas_dir.iterdir():
        if item.is_dir() and (item / "README.md").exists():
            persona_names.append(item.name)

    return len(persona_names) > 0, len(persona_names), persona_names


def validate_port(port_str: str, default: int = 7014) -> Tuple[int, str]:
    """
    Validate port number is valid.

    Returns:
        Tuple of (validated_port, error_message or empty string)
    """
    try:
        port = int(port_str)
        if port < 1 or port > 65535:
            return default, f"PORT {port} out of range (1-65535), using default {default}"
        return port, ""
    except ValueError:
        return default, f"Invalid PORT value '{port_str}', using default {default}"


async def validate_api_connectivity() -> Dict[str, bool]:
    """
    Ping external APIs to verify keys are valid.

    Returns:
        Dict mapping service name to connectivity status.
    """
    results = {}

    async with httpx.AsyncClient(timeout=5.0) as client:
        # Test OpenAI - list models endpoint
        openai_key = os.getenv("OPENAI_API_KEY")
        if openai_key and not openai_key.startswith("your_"):
            try:
                resp = await client.get(
                    "https://api.openai.com/v1/models",
                    headers={"Authorization": f"Bearer {openai_key}"},
                )
                results["openai"] = resp.status_code == 200
            except Exception:
                results["openai"] = False
        else:
            results["openai"] = False

        # Test Cartesia - list voices
        cartesia_key = os.getenv("CARTESIA_API_KEY")
        if cartesia_key and not cartesia_key.startswith("your_"):
            try:
                resp = await client.get(
                    "https://api.cartesia.ai/voices/",
                    headers={
                        "X-API-Key": cartesia_key,
                        "Cartesia-Version": "2024-06-10",
                    },
                )
                results["cartesia"] = resp.status_code == 200
            except Exception:
                results["cartesia"] = False
        else:
            results["cartesia"] = False

        # Test Deepgram - check auth (if using Deepgram)
        deepgram_key = os.getenv("DEEPGRAM_API_KEY")
        if deepgram_key and not deepgram_key.startswith("your_"):
            try:
                resp = await client.get(
                    "https://api.deepgram.com/v1/projects",
                    headers={"Authorization": f"Token {deepgram_key}"},
                )
                results["deepgram"] = resp.status_code == 200
            except Exception:
                results["deepgram"] = False
        else:
            # Check Gladia as alternative
            gladia_key = os.getenv("GLADIA_API_KEY")
            if gladia_key and not gladia_key.startswith("your_"):
                results["stt_provider"] = True  # Assume valid if key exists
            else:
                results["stt_provider"] = False

    return results


def run_startup_validation(local_dev: bool = False) -> bool:
    """
    Run all startup validations and exit if critical errors found.

    Args:
        local_dev: Whether running in local development mode

    Returns:
        True if all validations pass, exits with error if critical failures.
    """
    import asyncio

    logger.info("Running startup validation...")

    # Check environment variables
    env_errors = validate_env_vars()
    if env_errors:
        logger.error("=" * 50)
        logger.error("STARTUP FAILED: Missing required configuration")
        logger.error("=" * 50)
        for error in env_errors:
            logger.error(f"  - {error}")
        logger.error("")
        logger.error("Please check your .env file and ensure all required")
        logger.error("API keys are set. See .env.example for reference.")
        logger.error("=" * 50)
        sys.exit(1)

    # Check personas
    personas_valid, persona_count, persona_names = validate_personas()
    if not personas_valid:
        logger.error("=" * 50)
        logger.error("STARTUP FAILED: No personas found")
        logger.error("=" * 50)
        logger.error("The config/personas/ directory is empty or missing.")
        logger.error("Each persona needs a folder with a README.md file.")
        logger.error("=" * 50)
        sys.exit(1)

    # Check API connectivity
    try:
        api_status = asyncio.run(validate_api_connectivity())
    except Exception as e:
        logger.warning(f"Could not validate API connectivity: {e}")
        api_status = {}

    api_failures = [name for name, status in api_status.items() if not status]
    if api_failures:
        logger.error("=" * 50)
        logger.error("STARTUP FAILED: API connectivity check failed")
        logger.error("=" * 50)
        for api_name in api_failures:
            logger.error(f"  - {api_name.upper()} API: Connection failed or invalid key")
        logger.error("")
        logger.error("Please verify your API keys are correct and the")
        logger.error("services are reachable from this network.")
        logger.error("=" * 50)
        sys.exit(1)

    # All checks passed
    logger.info(f"Validation passed: {persona_count} personas loaded")
    return True


def print_startup_summary(
    port: int,
    local_dev: bool,
    ngrok_urls: List[str],
) -> None:
    """
    Print a startup summary showing configuration status.

    Args:
        port: Server port
        local_dev: Whether in local dev mode
        ngrok_urls: List of available ngrok URLs
    """
    # Get persona info
    _, persona_count, persona_names = validate_personas()
    preview_names = ", ".join(persona_names[:3])
    if len(persona_names) > 3:
        preview_names += f", +{len(persona_names) - 3} more"

    # Check API key status (presence only, connectivity already validated)
    api_checks = {
        "OPENAI": bool(os.getenv("OPENAI_API_KEY")),
        "CARTESIA": bool(os.getenv("CARTESIA_API_KEY")),
        "DEEPGRAM": bool(os.getenv("DEEPGRAM_API_KEY")),
        "MEETING_BAAS": bool(os.getenv("MEETING_BAAS_API_KEY")),
    }
    api_status = " ".join(
        f"{name} [{'OK' if ok else 'MISSING'}]" for name, ok in api_checks.items()
    )

    # ngrok status
    if local_dev:
        ngrok_status = f"{len(ngrok_urls)} tunnels available" if ngrok_urls else "NOT RUNNING"
    else:
        base_url = os.getenv("BASE_URL")
        ngrok_status = f"production: {base_url}" if base_url else "not configured"

    mode = "local-dev" if local_dev else "production"

    logger.info("=" * 50)
    logger.info("Speaking Meeting Bot Starting")
    logger.info("=" * 50)
    logger.info(f"Mode: {mode}")
    logger.info(f"Port: {port}")
    logger.info(f"Personas: {persona_count} loaded ({preview_names})")
    logger.info(f"ngrok: {ngrok_status}")
    logger.info(f"API Keys: {api_status}")
    logger.info("=" * 50)
