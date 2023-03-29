import speech_recognition as sr

r = sr.Recognizer()

def listen():
    print("Listening...")
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source,0,6)
        
    print("recognising...\n")
    try:
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n") 
    except Exception as e:
        return "None"
    return query

def sListen():
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source,0,6)
        
    try:
        query = r.recognize_google(audio,language='en-in')
    except Exception as e:
        return "None"
    return query