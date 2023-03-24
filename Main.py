from Listen import listen, recogniser
from AIBrain import getResponse
from GreetMe import greetMe
from Speak import speak
from PyQt5 import QtCore
from translator import translate



class MainThread(QtCore.QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.wakeup()

    def wakeup(self):
        while True:
            audio = listen()
            query = recogniser(audio).lower()
            if "none" == query:
                continue
            elif "hey jarvis" in query:
                self.main()

    def main(self):
        greetMe()
        while True:
            print("Listening...")
            audio = listen()
            print("recognising...\n")
            query = recogniser(audio)
            try:
                if query.lower() == "goodbye jarvis":
                    self.wakeup()
                elif query != "None":
                    print(f"You said: {query}\n") 
                    answer = getResponse(translate(query.lower()).text)
                    print(f"{answer}\n")
                    speak(answer)
            except:
                print("Please say that again\n")
                speak("Please say that again\n")
    



if __name__ == "__main__":
    from PyQt5.QtWidgets import *
    from sys import argv, exit
    Gui_App = QApplication(argv)
    startfunc = MainThread()
    startfunc.start()
    exit(Gui_App.exec_())
    