import re
from typing import Tuple


MAX_TEXT_LENGTH = 5000


def validate_text(text: str) -> Tuple[bool, str]:
    """
    Validate input text for TTS.

    Rules:
    - Not empty after stripping whitespace
    - Length <= MAX_TEXT_LENGTH
    - Contains at least one alphanumeric character
    - No control characters (other than standard whitespace)
    """
    if text is None:
        return False, "Text must not be None."

    stripped = text.strip()
    if not stripped:
        return False, "Text must not be empty."

    if len(stripped) > MAX_TEXT_LENGTH:
        return False, f"Text must be at most {MAX_TEXT_LENGTH} characters."

    if not re.search(r"[0-9A-Za-z]", stripped):
        return False, "Text must contain at least one letter or number."

    # Disallow ASCII control characters except tab/newline/carriage-return
    for ch in stripped:
        code = ord(ch)
        if code < 32 and ch not in ("\t", "\n", "\r"):
            return False, "Text contains unsupported control characters."

    return True, ""


