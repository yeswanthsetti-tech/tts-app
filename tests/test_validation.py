import os
import sys

import pytest

# Ensure project root is on the Python path so `validation` can be imported
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from validation import validate_text, MAX_TEXT_LENGTH


@pytest.mark.parametrize(
    "text, expected_valid",
    [
        ("Hello world", True),
        (" 123 ", True),
        ("", False),
        ("   ", False),
        ("!!!@@@", False),
    ],
)
def test_basic_validation_cases(text, expected_valid):
    is_valid, _ = validate_text(text)
    assert is_valid is expected_valid


def test_too_long_text_is_invalid():
    text = "a" * (MAX_TEXT_LENGTH + 1)
    is_valid, msg = validate_text(text)
    assert not is_valid
    assert "at most" in msg


def test_control_characters_are_invalid():
    text = "Hello\u0007World"  # Bell character
    is_valid, msg = validate_text(text)
    assert not is_valid
    assert "control characters" in msg


