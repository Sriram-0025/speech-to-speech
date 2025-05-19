🗣️ Tamil ➜ English Speech-to-Speech Translator

This project is a simple speech translation tool that allows users to upload a **Tamil audio file (.wav)** and receive:

* Transcribed **Tamil text**
* Translated **English text**
* Synthesized **English audio**

Built with Python, this system leverages Google’s speech, translation, and text-to-speech APIs, and provides a user-friendly interface using **Gradio**.

📌 Features

* 🎙️ **Speech Recognition**: Converts Tamil audio to text using Google Speech Recognition.
* 🌐 **Translation**: Translates Tamil text to English using Deep Translator (Google Translate backend).
* 🔊 **Text-to-Speech**: Generates English audio using gTTS (Google Text-to-Speech).
* 🖥️ **Web Interface**: Simple Gradio interface for quick testing and interaction.


🚀 How It Works

1. User uploads a **Tamil audio file** (`.wav` format).
2. The system transcribes the speech to Tamil text.
3. Transcribed Tamil text is translated into English.
4. English text is converted into speech and returned as downloadable audio.


🧪 Example
Input Audio (Tamil)**:

> "காலை வணக்கம்! இன்று நீங்கள் எப்படி இருக்கிறீர்கள்?"

Output**:

* Tamil Text**: காலை வணக்கம்! இன்று நீங்கள் எப்படி இருக்கிறீர்கள்?
* English Translation**: Good morning! How are you doing today?
* English Audio**: \[🎧 Generated via gTTS]


📂 Project Structure

```bash
├── app.py                  # Main application code
├── requirements.txt        # Python dependencies
├── README.md               # Project description and usage
```

---

⚙️ Installation

1. Clone the Repository

```bash
git clone https://github.com/Sriram-0025/speech-to-speech.git
cd speech-to-speech
```

2. Install Dependencies

Ensure Python 3.7+ is installed, then run:

```bash
pip install -r requirements.txt
```

3. Run the App

```bash
python app.py
```

Gradio will launch a local web interface in your browser.


✅ Requirements

* Python 3.7 or higher
* Internet connection (for Google APIs)
* .wav audio files recorded in Tamil
* Microphone & speaker (if live testing is added)


📌 Limitations

* Depends on internet for all major tasks (STT, translation, TTS)
* Struggles with heavy background noise
* Uses standard Tamil; may not support regional dialects
* Not optimized for long audio (>30 seconds)


🧭 Future Enhancements

* Add **live microphone input**
* Support **offline speech and translation models**
* Extend to **other Indian languages**
* Build **Android/iOS apps**
* Add **context-aware translation and dialogue mode**



📚 References

* [Google Speech Recognition](https://cloud.google.com/speech-to-text)
* [Google Translate API](https://cloud.google.com/translate)
* [gTTS - Text to Speech](https://pypi.org/project/gTTS/)
* [Gradio](https://www.gradio.app/)
* [Deep Translator](https://pypi.org/project/deep-translator/)



