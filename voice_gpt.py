import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr
import uuid

api_key = 'Chat_GPT API key here'

lang = 'en'
r = sr.Recognizer()
openai.api_key = api_key

guy = ""  # Initialize the 'guy' variable outside the loop

while True:
    def get_audio():
      #  r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:  # Corrected the syntax error
                print("Listening")
                audio = r.listen(source)
                said = ''
                said = r.recognize_google(audio)
                print(said)
                guy = said
                if 'Friday' in said:
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": said}])

                    text = completion.choices[0].message.content
                    speech = gTTS(text=text, lang=lang, tld="com.au", )
                    file_name = f"welcome_{str(uuid.uuid4())}.mp3"
                    speech.save(file_name)
                    playsound.playsound(file_name, block=True)
        except Exception as e:
            print("Exception:", e)
        return said
    get_audio()
