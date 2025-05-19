import speech_recognition as sr
from gtts import gTTS
from deep_translator import GoogleTranslator
import gradio as gr
import tempfile

def recognize_speech_from_audio(file_path, source_lang="ta-IN"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language=source_lang)
    except sr.UnknownValueError:
        return "[Could not understand the audio]"
    except sr.RequestError as e:
        return f"[Google API error: {e}]"

def translate_text(text, src='ta', dest='en'):
    try:
        translated = GoogleTranslator(source=src, target=dest).translate(text)
        return translated
    except Exception as e:
        print("Translation error:", e)
        return "[Translation failed]"

def text_to_speech(text, lang='en'):
    if not text:
        return None
    try:
        tts = gTTS(text=text, lang=lang)
        temp_mp3 = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_mp3.name)
        return temp_mp3.name
    except Exception as e:
        print("TTS error:", e)
        return None

def process_audio(audio):
    # audio is a dict with 'name' key (from gr.Audio with type="filepath")
    temp_wav_path = audio
    tamil_text = recognize_speech_from_audio(temp_wav_path)
    english_text = translate_text(tamil_text)
    english_audio_path = text_to_speech(english_text)

    return english_audio_path, tamil_text, english_text

interface = gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(type="filepath", label="Upload Tamil Audio (.wav)"),
    outputs=[
        gr.Audio(type="filepath", label="Translated English Audio"),
        gr.Textbox(label="Tamil Text"),
        gr.Textbox(label="English Translation")
    ],
    title="Speech-to-Speech Translator (Tamil ➜ English)",
    description="Upload a Tamil .wav audio file. It will be transcribed, translated, and converted into English audio."
)

if __name__ == "__main__":
    interface.launch()
