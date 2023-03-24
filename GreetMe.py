import datetime
from Speak import speak
def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour >= 12 and hour < 16:
        print("Good afternoon!")
        speak("Good afternoon!")

    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("I am jarvis Sir, Please tell me how may I help you!\n")
    speak("I am jarvis Sir, Please tell me how may I help you!")
