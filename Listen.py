import speech_recognition as sr

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source,0,6)
    return audio

def recogniser(audio):
    try:
        query = r.recognize_google(audio,language='en-in')
    except Exception as e:
        return "None"
    return query