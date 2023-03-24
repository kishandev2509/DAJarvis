import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()