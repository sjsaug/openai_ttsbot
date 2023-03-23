import openai
import pyttsx3
import speech_recognition as sr
import os
from dotenv import load_dotenv

load_dotenv()
OAI_KEY = os.getenv('OAI_KEY')

openai.api_key = OAI_KEY

engine = pyttsx3.init()

counter = 0

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except: 
        print("Skipping unknown error")

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{'role': 'user', 'content': prompt}],
        temperature = 0
    )
    return response["choices"][0]["message"]["content"]

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

counter = 0
def main():
    while True:
        print("Say hey sophiebear")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "hey sophiebear" or "hey sophie bear":
                    filename = "input.wav"
                    print("Yo")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit = None, timeout = None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                    text = transcribe_audio_to_text(filename)
                    if text:
                        user_print = f"User : {text}"
                        print(user_print)
                        speak_text(user_print)
                
                        response = generate_response(text)
                        response_print = f"Sophiebear : {response}"
                        print(response_print)                
                        speak_text(response_print)
            except Exception as e:
                print("An error occured : {}".format(e))

if __name__ == "__main__":
    main()
