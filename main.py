import openai
import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv

load_dotenv()
OAI_KEY = os.getenv('OAI_KEY')

openai.api_key = OAI_KEY

engine = pyttsx3.init()

recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized {text}")

    except sr.UnknownValueError():

        recognizer = sr.Recognizer()
        continue
