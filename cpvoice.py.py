import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
import datetime
import wolframalpha
from gtts import gTTS


r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if(ask):
            cutiepie_speak(ask)
        print('Listening.....')
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            cutiepie_speak('Sorry, I did not get that')
        except sr.RequestError:
            cutiepie_speak('Sorry, i can not do this')
        return voice_data

def cutiepie_speak(audio_string):
    tts = gTTS(text=audio_string, lang = 'en', slow=False)
    r = random.randint(1,1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'who are you' or 'describe about yourself' in voice_data:
        cutiepie_speak("I'm Cutiepie  I'm Ragul's personal assistant")
    if 'what is your name' in voice_data:
        cutiepie_speak('My name is cutiepie')
    if 'what time is it' in voice_data:
        cutiepie_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        cutiepie_speak('Here is what i found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('what is the location')
        url = 'https://google.com/maps/place/' + location
        webbrowser.get().open(url)
        cutiepie_speak('Here is the location ' + location)
    if 'exit' in voice_data:
        cutiepie_speak('thank you ! have a nice day')
        exit()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 10 and currentH < 3:
        cutiepie_speak('Hi Sir,Good Morning!\n How can i help you ?')

    if currentH >= 3 and currentH < 15:
        cutiepie_speak('Hi Sir,Good Afternoon!\n How can i help you ?' )

    if currentH >= 15 and currentH !=19:
        cutiepie_speak('Hi Sir,Good Evening! \n How can i help you ?')

    if currentH >= 19 and currentH !=10:
        cutiepie_speak('Good Night sir! It is night \n How can i help you ?')


time.sleep(1)
greetMe()
while 1:
    voice_data = record_audio()
    respond(voice_data)
