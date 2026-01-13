import io
import os
from typing import Optional

import streamlit as st

from tts_engine import list_voices, synthesize_to_file
from validation import validate_text


def _get_default_voice_id() -> Optional[str]:
    voices = list_voices()
    return voices[0]["id"] if voices else None


def main() -> None:
    st.title("Text-to-Speech Demo")
    st.write("Convert text into speech with selectable voice, rate, and volume.")

    # Sidebar controls
    st.sidebar.header("Speech Settings")

    voices = list_voices()
    voice_options = ["Default"]
    voice_id_map = {"Default": None}
    for v in voices:
        label = f"{v['name']} ({v['gender']})"
        voice_options.append(label)
        voice_id_map[label] = v["id"]

    selected_voice_label = st.sidebar.selectbox("Voice", voice_options, index=0)
    rate = st.sidebar.slider("Rate (words per minute)", min_value=80, max_value=260, value=180, step=10)
    volume = st.sidebar.slider("Volume", min_value=0.1, max_value=1.0, value=1.0, step=0.05)

    text = st.text_area("Enter text to speak", height=200)

    error_placeholder = st.empty()
    audio_placeholder = st.empty()

    if st.button("Generate Speech"):
        is_valid, error = validate_text(text)
        if not is_valid:
            error_placeholder.error(error)
        else:
            error_placeholder.empty()

            voice_id = voice_id_map.get(selected_voice_label)

            # Use a temporary file, then load into memory for playback
            tmp_dir = "generated_audio"
            os.makedirs(tmp_dir, exist_ok=True)
            file_path = os.path.join(tmp_dir, "speech.wav")

            synthesize_to_file(
                text=text,
                output_path=file_path,
                voice_id=voice_id,
                rate=rate,
                volume=volume,
            )

            with open(file_path, "rb") as f:
                audio_bytes = f.read()

            audio_placeholder.audio(audio_bytes, format="audio/wav")


if __name__ == "__main__":
    main()


