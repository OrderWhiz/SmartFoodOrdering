import speech_recognition as sr
import pyttsx3


def stt():
    # create a speech recognition object
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # handle ambient noise
        r.adjust_for_ambient_noise(source)

        # read the audio data from the default microphone
        print("Recording...")
        audio_data = r.record(source, duration=30)

        #listen to the mic
        #audio_data = r.listen(source)

        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        tts(text)  # should be replaced by call to RASA


def tts(text):
    engine = pyttsx3.init()
    engine.say(text)

