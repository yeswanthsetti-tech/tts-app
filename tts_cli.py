import argparse
import os

from tts_engine import list_voices, synthesize_to_file
from validation import validate_text


def _choose_voice(voice_name_or_id: str):
    voices = list_voices()
    for v in voices:
        if v["id"] == voice_name_or_id or v["name"].lower() == voice_name_or_id.lower():
            return v["id"]
    raise SystemExit(f"Voice '{voice_name_or_id}' not found. Available: {[v['name'] for v in voices]}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple Text-to-Speech CLI using pyttsx3.")
    parser.add_argument("text", help="Text to convert to speech.")
    parser.add_argument(
        "-o",
        "--output",
        default="output.wav",
        help="Output audio file path (default: output.wav)",
    )
    parser.add_argument(
        "-v",
        "--voice",
        help="Voice name or id (see --list-voices).",
    )
    parser.add_argument(
        "-r",
        "--rate",
        type=int,
        default=180,
        help="Speech rate (words per minute, default: 180).",
    )
    parser.add_argument(
        "-V",
        "--volume",
        type=float,
        default=1.0,
        help="Volume between 0.0 and 1.0 (default: 1.0).",
    )
    parser.add_argument(
        "--list-voices",
        action="store_true",
        help="List available voices and exit.",
    )

    args = parser.parse_args()

    if args.list_voices:
        voices = list_voices()
        print("Available voices:")
        for v in voices:
            print(f"- id={v['id']}, name={v['name']}, gender={v['gender']}, languages={v['languages']}")
        return

    is_valid, error = validate_text(args.text)
    if not is_valid:
        raise SystemExit(f"Invalid text: {error}")

    voice_id = None
    if args.voice:
        voice_id = _choose_voice(args.voice)

    output_path = os.path.abspath(args.output)
    synthesize_to_file(
        text=args.text,
        output_path=output_path,
        voice_id=voice_id,
        rate=args.rate,
        volume=args.volume,
    )
    print(f"Audio saved to {output_path}")


if __name__ == "__main__":
    main()


