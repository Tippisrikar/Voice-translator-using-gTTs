import speech_recognition as spr
from gtts import gTTS
from googletrans import Translator
import asyncio
import os

# Function to detect language asynchronously
async def detect_language(text):
    translator = Translator()
    detected_language = await translator.detect(text)
    return detected_language.lang

# Function to translate text asynchronously
# Function to translate text asynchronously
async def translate_text(text, target_lang):
    translator = Translator()
    # Translate using correct language code
    translated = await translator.translate(text, dest=target_lang.lower())  # Ensure lowercase language code
    return translated.text

# Initialize speech recognizer
r = spr.Recognizer()

# Function to listen and recognize speech
def listen_speech():
    with spr.Microphone() as source:
        print("Speak now for language detection and translation...")
        audio = r.listen(source)
        return audio

# Function to recognize and translate speech
async def recognize_and_translate():
    try:
        # Listen to speech
        audio = listen_speech()

        # Recognize speech
        MyText = r.recognize_google(audio)
        print(f"Recognized Text: {MyText}")

        # Detect language asynchronously
        language = await detect_language(MyText)
        print(f"Detected language: {language}")

        # Ask for the target language
        target_lang = input("Enter the target language (e.g., 'Hindi', 'Telugu', 'Tamil'): ")

        # Translate text asynchronously
        translated_text = await translate_text(MyText, target_lang)
        print(f"Translated Text: {translated_text}")

        # Convert translated text to speech
        tts = gTTS(text=translated_text, lang=target_lang, slow=False)
        tts.save("C:/Users/tippi/Downloads/translated_audio.mp3")
        os.system("C:/Users/tippi/Downloads/translated_audio.mp3")

    except Exception as e:
        print(f"Error: {e}")

# Run the translation process
asyncio.run(recognize_and_translate())
