from Listen import listen, sListen
from AIBrain import getResponse
from GreetMe import greetMe
from Speak import speak
from PyQt5 import QtCore
from translator import translate
from MailSender import sendEmail
import wikipedia
import webbrowser
import pywhatkit
import random
import pyjokes
import wolframalpha
import psutil
import os
import sys
import datetime
import pyautogui

app = wolframalpha.Client("TWTKXX-TELTXEY6QK")

intro, intro_reply, intro2,intro2_reply ,hru ,hru_reply, ability, ability_reply, emotion, emotion_reply, siri, siri_reply , create , punjabi , slow , temprature , app , Battery , vol1, vol2 ,vol_mute, dict_app, temprature,create , punjabi , science , close , cal= []

class MainThread(QtCore.QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.wakeup()

    def wakeup(self):
        while True:
            print("......")
            query = sListen().lower()
            if "hey jarvis" in query:
                self.main()
            else:
                continue

    def main(self):
        greetMe()
        while True:
            try:
                query = listen().lower()

                match query:
                    case "goodbye jarvis":
                        self.wakeup()

                    case _ if 'wikipedia' in query:
                        speak('Searching Wikipedia...')
                        self.query = self.query.replace("wikipedia", "")
                        results = wikipedia.summary(self.query, sentences=2)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)

                    case _ if 'open youtube' in query:
                        RES = webbrowser.open("youtube.com")
                        speak("Alright sir!!,opening Youtube")

                    case _ if 'open google' in query:
                        RES = webbrowser.open("google.com")
                        speak("Alright sir!!,opening Google")
                            
                    case _ if 'on youtube' in self.query:
                        OPEN = self.query.replace("search","")
                        OPEN = self.query.replace("jarvis","")
                        OPEN = self.query.replace("play","")
                        pywhatkit.playonyt(OPEN)
                        speak("Alright Sir...I Found Something")

                    case _ if query in intro:
                        speak(random.choice(intro_reply))

                    case _ if query in intro2:
                        speak(random.choice(intro2_reply))

                    case _ if query in hru:
                        speak(random.choice(hru_reply))

                    case _ if query in ability:
                        speak(random.choice(ability_reply))

                    case _ if query in emotion:
                        speak(emotion_reply)

                    case _ if query in siri:
                        speak(siri_reply)
                        
                    case _ if query in create:

                        speak("Sir Mr. Jegmeet Singh Created Me With The Help Of Mr. Dettinder...I Appericiate Their Hard Work...I Was Successfully Developed After Many Failures Faced By Them...Mr. Jegmeet And Datitnder...If You Are Listening...I LOVE YOU 3000")

                    case _ if query in punjabi:

                        speak("MAINNU PUNJABI NAAHI AUNDDI MMAHAARRAJJ....It Will Take Some Time For Me To Learn Punjabi")    

                    case _ if query in slow:

                        speak("Sir I am Processing Slow Because Internet Connection is NOT Stable...I Apologize For That ")
                    
                    case _ if self.query in temprature:
                        try:
                            speak("Please tell the name of city...Please Say Temperature in And Give The City Name")
                            print("Please tell me The name of city")
                            tempra = self.takeCommand().lower()
                            tempra_res = app.query(tempra)
                            speak(next(tempra_res.results).text)
                            print(next(tempra_res.results).text)

                        except:
                            speak("sorry i could NOT fetch your data")

                    case _ if 'joke' in self.query:
                        joke = pyjokes.get_joke()
                        print(joke)
                        speak(joke)

                    case _ if  'google search' in self.query:
                        import wikipedia as googleScrap

                        self.query = self.query.replace("jarvis", "")
                        self.query = self.query.replace("google search", "")
                        self.query = self.query.replace("google", "")
                        self.query = self.query.replace("about", "")
                        speak("This Is What I Found On The Web!")
                        print("This Is What I Found On The Web!")
                        pywhatkit.search(self.query)
                        try:

                            result = googleScrap.summary(self.query, 3)
                            speak(result)
                        except:
                            speak("sorry...i did not found anything")

                    case _ if  'open stackoverflow' in self.query:
                        webbrowser.open("stackoverflow.com")

                    case _ if  'say good about me' in self.query:
                        speak("I believe you will become python developer one day...keep it up i am with you")

                    case _ if  self.query in Battery:
                        battery = psutil.sensors_battery()
                        percentage= battery.percent
                        if percentage>=75:
                            speak(f"Sir Our System Have {percentage} Percent battery...That's Quite Enough...You Have Enough Power...Please Continue Your Work")
                        elif percentage>=45 and percentage<=75:
                            speak(f"Sir Our System Have {percentage} % Percent battery...You Need To Charge The Device Soon...But We Can Do Some Tasks For Sometime")
                        elif percentage>=15 and percentage<=30:
                            speak(f"Sir Our System Have {percentage} percent battery...We Don't HAve Enough POwer To Work...You Should Charge Your Device" )
                        else:
                            speak(f"Sir Our System Have {percentage} Percent battery...Battery Will Die Soon...You Need Charge Your Device As Soon AS Possible ")

                    case _ if  'play music' in self.query:
                        music_dir = 'C:\\Users\\DELL\\Music\\Playlists'
                        songs = os.listdir(music_dir)
                        print(songs)
                        os.startfile(os.path.join(music_dir, songs[0]))

                    case _ if  'the time' in self.query:
                        strTime = datetime.datetime.now().strftime("%I:%M:%p")
                        speak(f"Sir, the time is {strTime}")



                    case _ if  self.query in vol1:
                        speak("OK SIR!,Increasing Volume")
                        pyautogui.press("volumeup")

                    case _ if  self.query in vol2:
                        speak("Alright Sir!...Deacreasing Volume")
                        pyautogui.press("volumedown")

                    case _ if  self.query in vol_mute:
                        speak("OK Sir...Going Mute")
                        pyautogui.press("volumemute")

                    case _ if  'email to me' in self.query:
                        try:
                            speak("What should I say?")
                        
                            content = self.takeCommand()
                            to = "sidhugurjant587@gmail.com"
                            sendEmail(to, content)
                            speak("Email has been sent!")
                            print("Email has been sent!")
                        except Exception as e:
                            print(e)
                            speak("Sorry my friend . I am not able to send this email")

                    case _ if  self.query in cal:

                        try:
                            speak("what should i calculate")
                            print("what should i calculate")
                            CAL=self.takeCommand().lower()
                            RES=app.query(CAL)
                            speak(next(RES.results).text)
                            print(next(RES.results).text)

                        except:
                            speak("sorry i could NOT fetch your data")

                    case _ if  self.query in science:
                        try:
                            speak("Please Tell me...What's The Question")
                            print("Please Tell me...What's The Question")
                            qs=self.takeCommand().lower()
                            ans=app.query(qs)
                            speak(next(ans.results).text)
                            print(next(ans.results).text)
                        except:
                            speak("sorry i could not process your data")

                    case _ if  self.query in close:
                        speak("Aright Sir... I AM Going Offline...You Can Call Me Anytime")
                        sys.exit()
                    case _  if  '.com' in self.query or '.org' in self.query or '.in' in self.query:
                        if  '.com' in self.query or '.org' in self.query or '.in' in self.query:
                            self.query = self.query.replace('open', '')
                            self.query = self.query.replace('jarvis', '')
                            self.query = self.query.replace('launch', '')
                            self.query = self.query.replace(' ', '')
                            webbrowser.open(self.query)
                            speak(f"Alright Sir opening {self.query}")
                        else:
                            apps = list(dict_app.keys())
                            for ap in apps:
                                if ap in self.query:
                                    os.system(f"start {dict_app[ap]}")
                                    speak(f"Alright Sir opening {ap}")
                                    print(f"Alright Sir opening {ap}")

                    case _ if query != "none":
                        answer = getResponse(translate(query).text)
                        print(f"{answer}\n")
                        speak(answer)


                    case _ :
                        continue


            except:
                continue



            # query = listen().lower()
            # try:
            #     # if query == "goodbye jarvis":
            #     #     self.wakeup()
            #     # case _ if  query != "None":
            #     #     answer = getResponse(translate(query).text)
            #     #     print(f"{answer}\n")
            #     #     speak(answer)

                    
            #     # if 'wikipedia' in self.query:
            #     #     speak('Searching Wikipedia...')
            #     #     self.query = self.query.replace("wikipedia", "")
            #     #     results = wikipedia.summary(self.query, sentences=2)
            #     #     speak("According to Wikipedia")
            #     #     print(results)
            #     #     speak(results)

            #     # elif 'open youtube' in self.query:
            #     #     RES = webbrowser.open("youtube.com")
            #     #     speak("Alright sir!!,opening Youtube")

            #     # elif 'on youtube' in self.query:
            #     #     OPEN = self.query.replace("search","")
            #     #     OPEN = self.query.replace("jarvis","")
            #     #     OPEN = self.query.replace("play","")
            #     #     pywhatkit.playonyt(OPEN)
            #     #     speak("Alright Sir...I Found Something")


            #     # elif 'open google' in self.query:
            #     #     webbrowser.open("google.com")
            #     #     speak("Alright sir!!,opening Google")

            #     # elif self.query in intro:
            #     #     speak(random.choice(intro_reply))

            #     # elif self.query in intro2:
            #     #     speak(random.choice(intro2_reply))

            #     # elif self.query in hru:
            #     #     speak(random.choice(hru_reply))

            #     # elif self.query in ability:
            #     #     speak(random.choice(ability_reply))

            #     # elif self.query in emotion:
            #     #     speak(emotion_reply)

            #     # elif self.query in siri:
            #     #     speak(siri_reply)

            #     # elif self.query in create:

            #     #     speak("Sir Mr. Jegmeet Singh Created Me With The Help Of Mr. Dettinder...I Appericiate Their Hard Work...I Was Successfully Developed After Many Failures Faced By Them...Mr. Jegmeet And Datitnder...If You Are Listening...I LOVE YOU 3000")

            #     # elif self.query in punjabi:

            #     #     speak("MAINNU PUNJABI NAAHI AUNDDI MMAHAARRAJJ....It Will Take Some Time For Me To Learn Punjabi")    

            #     # elif self.query in slow:

            #     #     speak("Sir I am Processing Slow Because Internet Connection is NOT Stable...I Apologize For That ")

            #     # elif self.query in temprature:
            #         try:
            #             speak("Please tell the name of city...Please Say Temperature in And Give The City Name")
            #             print("Please tell me The name of city")
            #             tempra = self.takeCommand().lower()
            #             tempra_res = app.query(tempra)
            #             speak(next(tempra_res.results).text)
            #             print(next(tempra_res.results).text)

            #         except:
            #             speak("sorry i could NOT fetch your data")

            #         if 'joke' in self.query:
            #             joke = pyjokes.get_joke()
            #             print(joke)
            #             speak(joke)

            #         elif 'google search' in self.query:
            #             import wikipedia as googleScrap

            #             self.query = self.query.replace("jarvis", "")
            #             self.query = self.query.replace("google search", "")
            #             self.query = self.query.replace("google", "")
            #             self.query = self.query.replace("about", "")
            #             speak("This Is What I Found On The Web!")
            #             print("This Is What I Found On The Web!")
            #             pywhatkit.search(self.query)
            #             try:

            #                 result = googleScrap.summary(self.query, 3)
            #                 speak(result)
            #             except:
            #                 speak("sorry...i did not found anything")

            #         elif 'open stackoverflow' in self.query:
            #             webbrowser.open("stackoverflow.com")

            #         elif 'say good about me' in self.query:
            #             speak("I believe you will become python developer one day...keep it up i am with you")

            #         elif self.query in Battery:
            #             battery = psutil.sensors_battery()
            #             percentage= battery.percent
            #             if percentage>=75:
            #                 speak(f"Sir Our System Have {percentage} Percent battery...That's Quite Enough...You Have Enough Power...Please Continue Your Work")
            #             elif percentage>=45 and percentage<=75:
            #                 speak(f"Sir Our System Have {percentage} % Percent battery...You Need To Charge The Device Soon...But We Can Do Some Tasks For Sometime")
            #             elif percentage>=15 and percentage<=30:
            #                 speak(f"Sir Our System Have {percentage} percent battery...We Don't HAve Enough POwer To Work...You Should Charge Your Device" )
            #             else:
            #                 speak(f"Sir Our System Have {percentage} Percent battery...Battery Will Die Soon...You Need Charge Your Device As Soon AS Possible ")

            #         elif 'play music' in self.query:
            #             music_dir = 'C:\\Users\\DELL\\Music\\Playlists'
            #             songs = os.listdir(music_dir)
            #             print(songs)
            #             os.startfile(os.path.join(music_dir, songs[0]))

            #         elif 'the time' in self.query:
            #             strTime = datetime.datetime.now().strftime("%I:%M:%p")
            #             speak(f"Sir, the time is {strTime}")



            #         elif self.query in vol1:
            #             speak("OK SIR!,Increasing Volume")
            #             pyautogui.press("volumeup")

            #         elif self.query in vol2:
            #             speak("Alright Sir!...Deacreasing Volume")
            #             pyautogui.press("volumedown")

            #         elif self.query in vol_mute:
            #             speak("OK Sir...Going Mute")
            #             pyautogui.press("volumemute")

            #         elif 'email to me' in self.query:
            #             try:
            #                 speak("What should I say?")
                        
            #                 content = self.takeCommand()
            #                 to = "sidhugurjant587@gmail.com"
            #                 sendEmail(to, content)
            #                 speak("Email has been sent!")
            #                 print("Email has been sent!")
            #             except Exception as e:
            #                 print(e)
            #                 speak("Sorry my friend . I am not able to send this email")

            #         elif self.query in cal:

            #             try:
            #                 speak("what should i calculate")
            #                 print("what should i calculate")
            #                 CAL=self.takeCommand().lower()
            #                 RES=app.query(CAL)
            #                 speak(next(RES.results).text)
            #                 print(next(RES.results).text)

            #             except:
            #                 speak("sorry i could NOT fetch your data")

            #         elif self.query in science:
            #             try:
            #                 speak("Please Tell me...What's The Question")
            #                 print("Please Tell me...What's The Question")
            #                 qs=self.takeCommand().lower()
            #                 ans=app.query(qs)
            #                 speak(next(ans.results).text)
            #                 print(next(ans.results).text)
            #             except:
            #                 speak("sorry i could not process your data")

            #         elif self.query in close:
            #             speak("Aright Sir... I AM Going Offline...You Can Call Me Anytime")
            #             sys.exit()
            #         elif '.com' in self.query or '.org' in self.query or '.in' in self.query:
            #             self.query = self.query.replace('open', '')
            #             self.query = self.query.replace('jarvis', '')
            #             self.query = self.query.replace('launch', '')
            #             self.query = self.query.replace(' ', '')
            #             webbrowser.open(self.query)
            #             speak(f"Alright Sir opening {self.query}")
            #         else:
            #             apps = list(dict_app.keys())
            #             for ap in apps:
            #                 if ap in self.query:
            #                     os.system(f"start {dict_app[ap]}")
            #                     speak(f"Alright Sir opening {ap}")
            #                     print(f"Alright Sir opening {ap}")

            # except:
            #     print("Please say that again\n")
            #     speak("Please say that again\n")
    



if __name__ == "__main__":
    from PyQt5.QtWidgets import *
    from sys import argv, exit
    Gui_App = QApplication(argv)
    startfunc = MainThread()
    startfunc.start()
    exit(Gui_App.exec_())
    