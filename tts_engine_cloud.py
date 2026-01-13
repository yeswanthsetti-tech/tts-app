"""
Cloud-compatible TTS engine using Google Text-to-Speech (gTTS).
This works on Streamlit Cloud and other cloud platforms.
"""
import os
from typing import List, Dict, Any, Optional

try:
    from gtts import gTTS
    import io
except ImportError:
    gTTS = None


# gTTS language codes mapped to voice names
GTTTS_VOICES = [
    {"id": "en", "name": "English (US)", "gender": "neutral", "language": "en"},
    {"id": "en-us", "name": "English (US)", "gender": "neutral", "language": "en"},
    {"id": "en-gb", "name": "English (UK)", "gender": "neutral", "language": "en"},
    {"id": "es", "name": "Spanish", "gender": "neutral", "language": "es"},
    {"id": "fr", "name": "French", "gender": "neutral", "language": "fr"},
    {"id": "de", "name": "German", "gender": "neutral", "language": "de"},
    {"id": "it", "name": "Italian", "gender": "neutral", "language": "it"},
    {"id": "pt", "name": "Portuguese", "gender": "neutral", "language": "pt"},
    {"id": "hi", "name": "Hindi", "gender": "neutral", "language": "hi"},
    {"id": "ja", "name": "Japanese", "gender": "neutral", "language": "ja"},
    {"id": "ko", "name": "Korean", "gender": "neutral", "language": "ko"},
    {"id": "zh", "name": "Chinese", "gender": "neutral", "language": "zh"},
]


def list_voices() -> List[Dict[str, Any]]:
    """
    Return available voices from gTTS.
    """
    if gTTS is None:
        return [{"id": "en", "name": "English (Default)", "gender": "neutral", "language": "en"}]
    return GTTTS_VOICES.copy()


def synthesize_to_file(
    text: str,
    output_path: str,
    voice_id: Optional[str] = None,
    rate: Optional[int] = None,
    volume: Optional[float] = None,
) -> str:
    """
    Synthesize the given text to an audio file using gTTS.
    
    Note: gTTS doesn't support rate/volume control directly, but we'll
    use the voice_id as language code.
    
    - voice_id: language code (e.g., 'en', 'es', 'fr')
    - rate: ignored (gTTS doesn't support this)
    - volume: ignored (gTTS doesn't support this)
    """
    if gTTS is None:
        raise ImportError("gTTS is not installed. Install it with: pip install gtts")
    
    # Use voice_id as language code, default to 'en'
    lang = voice_id if voice_id and voice_id in [v["id"] for v in GTTTS_VOICES] else "en"
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    
    # Create gTTS object and save to file
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(output_path)
    
    return output_path
