import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from pydub import AudioSegment
import os

def recognize_speech_from_audio(file_path, source_lang="ta-IN"):
    """Converts speech to text using Google Speech Recognition."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        print("[INFO] Listening to audio...")
        audio = recognizer.record(source)

    try:
        print("[INFO] Recognizing speech...")
        text = recognizer.recognize_google(audio, language=source_lang)
        print("[INFO] Recognized Text:", text)
        return text
    except sr.UnknownValueError:
        print("[ERROR] Could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"[ERROR] Google Speech API error: {e}")
        return ""

def translate_text(text, src='ta', dest='en'):
    """Translate the text to another language using Google Translate."""
    if not text:
        return ""
    print("[INFO] Translating text...")
    translator = Translator()
    try:
        translated = translator.translate(text, src=src, dest=dest)
        print("[INFO] Translated Text:", translated.text)
        return translated.text
    except Exception as e:
        print(f"[ERROR] Translation failed: {e}")
        return ""

def text_to_speech(text, output_path, lang='en'):
    """Converts translated text to speech and saves it."""
    if not text:
        print("[ERROR] No text to convert to speech.")
        return
    print("[INFO] Converting text to speech...")
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(output_path)
        print(f"[INFO] Saved output audio to {output_path}")
    except Exception as e:
        print(f"[ERROR] TTS failed: {e}")

def main():
    input_audio = "/content/drive/MyDrive/T & s/generated-audio.wav" 
    output_audio = "output_audio.mp3"   

    tamil_text = recognize_speech_from_audio(input_audio)

    english_text = translate_text(tamil_text, src='ta', dest='en')

    text_to_speech(english_text, output_audio, lang='en')

    print("[INFO] Playing output audio...")
    AudioSegment.from_mp3(output_audio).export("output_audio.wav", format="wav")
    os.system("start output_audio.wav") 

if __name__ == "__main__":
    main()
