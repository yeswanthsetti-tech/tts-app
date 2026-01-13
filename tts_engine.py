import os
from typing import List, Dict, Any, Optional

import pyttsx3


_ENGINE: Optional[pyttsx3.Engine] = None


def _get_engine() -> pyttsx3.Engine:
    """Get a singleton pyttsx3 engine instance."""
    global _ENGINE
    if _ENGINE is None:
        _ENGINE = pyttsx3.init()
    return _ENGINE


def list_voices() -> List[Dict[str, Any]]:
    """
    Return available voices from the TTS engine.

    Each voice is represented as a dict with at least:
    - id: engine-specific id
    - name: human friendly name
    - languages: list of languages (if provided by engine)
    - gender: gender if exposed by engine, else 'unknown'
    """
    engine = _get_engine()
    voices_info: List[Dict[str, Any]] = []
    for v in engine.getProperty("voices"):
        voices_info.append(
            {
                "id": v.id,
                "name": getattr(v, "name", v.id),
                "languages": getattr(v, "languages", []),
                "gender": getattr(v, "gender", "unknown"),
            }
        )
    return voices_info


def synthesize_to_file(
    text: str,
    output_path: str,
    voice_id: Optional[str] = None,
    rate: Optional[int] = None,
    volume: Optional[float] = None,
) -> str:
    """
    Synthesize the given text to an audio file and return the output path.

    - voice_id: engine voice id from list_voices()
    - rate: words per minute (e.g. 150-200 typical)
    - volume: 0.0 to 1.0
    """
    engine = _get_engine()

    # Configure engine
    if voice_id is not None:
        engine.setProperty("voice", voice_id)
    if rate is not None:
        engine.setProperty("rate", int(rate))
    if volume is not None:
        # Clamp to [0.0, 1.0]
        volume = max(0.0, min(1.0, float(volume)))
        engine.setProperty("volume", volume)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    engine.save_to_file(text, output_path)
    engine.runAndWait()
    return output_path


def reset_engine() -> None:
    """Reset the global engine instance (useful for tests)."""
    global _ENGINE
    if _ENGINE is not None:
        _ENGINE.stop()
    _ENGINE = None


