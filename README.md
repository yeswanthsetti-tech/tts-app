## Text-to-Speech (TTS) Demo

This project provides:

- **Core TTS module** (`tts_engine.py`) using `pyttsx3`
- **Text validation** (`validation.py`) with **unit tests** (`tests/test_validation.py`)
- **Command-line tool** (`tts_cli.py`) to convert text to speech and save audio
- **Web application** (`web_app.py`) built with **Streamlit** to input text, choose voice, rate, and volume, and play audio in the browser

### 1. Installation

From the `task1` directory:

```bash
pip install -r requirements.txt
```

On Windows, it is recommended to use a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Basic TTS via CLI

Run:

```bash
python tts_cli.py "Hello, this is a test."
```

- **Output file**: `output.wav` (default)
- **Change output path**:

```bash
python tts_cli.py "Hello" -o my_speech.wav
```

- **List available voices**:

```bash
python tts_cli.py --list-voices "dummy"
```

- **Select voice, rate, and volume**:

```bash
python tts_cli.py "Custom voice" --voice "Microsoft David" --rate 200 --volume 0.8
```

### 3. Web Application (Streamlit)

Start the web app from the `task1` directory:

```bash
streamlit run web_app.py
```

Then open the URL shown in the terminal (usually `http://localhost:8501`) in your browser.

In the UI you can:

- **Enter text** in the text area
- Choose **voice**, **speech rate**, and **volume** in the sidebar
- Click **“Generate Speech”** to create audio and **play it directly** in the browser

### 4. Text Validation and Tests

Validation rules (`validation.py`):

- Text must **not be empty**
- Text length must be **≤ 5000 characters**
- Text must contain at least **one alphanumeric character**
- Text must **not contain control characters** (other than standard whitespace)

Run unit tests with:

```bash
pytest
```

