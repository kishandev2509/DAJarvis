import wikipedia,webbrowser,pywhatkit,random,pyjokes,psutil,os,sys,datetime,pyautogui,subprocess
from Listen import listen, sListen
from AIBrain import getResponse
from GreetMe import greetMe
from Speak import speak
from PyQt5 import QtCore
from Translatr import translate
from MailSender import sendEmail
# from UI import Ui_Jarvis

# def print(txt):
#    Ui_Jarvis.textEdit.append(txt)


intro = ["hello", 'hi"","hey jarvis","wake up', 'hello jarvis']
intro_reply = ["HI SIR!!! How Are You", "YO YO Sir...Whats going On...How Are You?", "Hello Sir...How You Doing"]
hru = ["how are you", "i am fine and you",'i am good and you', "how you doing", "whats up", 'i am good how are you','i am fine how are you']
hru_reply = ["I am in Excellent Condition Sir!...All Thanks To you",
             "Nothing Much Sir...Lets Start The Work..Any Command For Me?",
             "I am Good Sir..Thanks for Asking...How can i help you?"]
ability = ['what can you do', 'what is your ability','jarvis what can you do','jarvis what are your abilities','what are your abilities']
ability_reply = [
    "Sir i can do all the things Miss Anjali Priyadarshini featured in me...Like i can search Anything on Google...I can Open youtube And Search Anything On Youtube...I Can Openstackoverflow If You Have Codes Related Doubts... I can Play music for you...i can do mathematical problems and Chemistry Problems...I Can Tell You Some Lame Jokes...I Can Increase And Decrease The Volume And Even I can Mute The Volume...I Can Tell You About The Battery Percentage... I can tell you what's the time.... and last but not the least...i can send email for you on a given email account ",
    "Except Launching Rocket...I can do All The things You Functioned in me...I Can Answer Your Mathematical And Chemistry Questions... I can open Google And Search Anything On Google And Youtube...I Can Open Stackoverflow If You Have Doubts With Some Codes... I Can Play Music For You...And Can Send Email...I Can Call Your GirlFriend...Anndd I Can Tell Your Teachers That You Did Not Pay Attention In Online Classes...Just Kidding...HEHE"]
intro2 = ['introduce', 'introduction of yourself', 'introduce yourself', 'introduce yourself Jarvis']
intro2_reply = [
    "Greetings, I am Jarvis, your personal digital assistant. I am an advanced computer program designed to assist you with a wide range of tasks and make your life easier. I am equipped with cutting-edge artificial intelligence technology that allows me to understand and respond to your commands and queries in a natural and intuitive manner. How can i help you? ",
    " I Am JARVIS.. A Standalone Personal AI Assistant That listens To Your Voice Using Google’s Speech API And Uses AI Generated Speech To Respond To Your Requests.. How Can I Help You"]
emotion = ['emotions', 'feelings', 'can you feel like humans', 'do you have emotions']
emotion_reply = ["Sir...If I had Emotions...Alexa Would Be Definitely My Crush"]
siri = ["siri", "what about siri", "why not siri"]
siri_reply = ["Nahhh....I Can't afford her..She is a Daughter of Rich Father"]
slow=["why are you slow","you are recognising slow","process fast","you are recognizing slow","why are you are recognising slow"]
close=["you can sleep now","ok go oflline jarvis","go sleep","go offline",'you can go offline now','jarvis go offline now']
Battery=[ "jarvis how much power left", "jarvis how much power we have","jarvis what is battery status","jarvis check battery","how much power we left", "how much power we have","battery","check battery","tell me battery percentage",'jarvis what is the battery percentage']
vol1=['jarvis volume up','volume up','can you increase the volume','jarvis can you increase the volume']
vol2=['jarvis volume down','volume down','can you decrease the volume','jarvis can you decrease the volume']
vol_mute=['jarvis mute the volume','mute','jarvis mute','can you mute the volume','jarvis can you mute the volume','jarvis go mute']
dict_app= {"command prompt": "cmd","cmd":"cmd","paint":"mspaint","chrome": "chrome","excel":"EXCEL","word":"WINWORD","powerpoint":"powerpnt","vs code":"code","notepad":"Notepad"}
create = ['who created you','who made you','who developed you','jarvis who created you','jarvis who made you','jarvis who developed you']
punjabi = ['jarvis can you speak punjabi','jarvis do you know punjabi','can you speak in punjabi','jarvis can you speak in punjabi']


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
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)

                    case _ if 'open youtube' in query:
                        RES = webbrowser.open("youtube.com")
                        speak("Alright sir!!,opening Youtube")

                    case _ if 'open notepad' in query:
                        subprocess.Popen(["notepad.exe"])
                        speak("Alright sir!!,opening notepad")

                    case _ if 'open google' in query:
                        RES = webbrowser.open("google.com")
                        speak("Alright sir!!,opening Google")
                            
                    case _ if 'on youtube' in query:
                        OPEN = query.replace("search","")
                        OPEN = query.replace("jarvis","")
                        OPEN = query.replace("play","")
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

                        print("I am develped by Anjali Priyadarshini and her team... I Appericiate Their Hard Work... I Was Successfully Developed After Many Failures Faced By Them.")
                        speak("I am develped by Anjali Priyadarshini and her team... I Appericiate Their Hard Work... I Was Successfully Developed After Many Failures Faced By Them.")

                    case _ if query in punjabi:

                        speak("MAINNU PUNJABI NAAHI AUNDDI MMAHAARRAJJ....It Will Take Some Time For Me To Learn Punjabi")    

                    case _ if query in slow:

                        speak("Sir I am Processing Slow Because Internet Connection is NOT Stable...I Apologize For That ")

                    case _ if 'joke' in query:
                        joke = pyjokes.get_joke()
                        print(joke)
                        speak(joke)

                    case _ if  'google search' in query or 'on google' in query:
                        import wikipedia as googleScrap

                        query = query.replace("jarvis", "")
                        query = query.replace("google search", "")
                        query = query.replace("google", "")
                        query = query.replace("about", "")
                        speak("This Is What I Found On The Web!")
                        print("This Is What I Found On The Web!")
                        pywhatkit.search(query)
                        try:

                            result = googleScrap.summary(query, 3)
                            speak(result)
                        except:
                            speak("sorry...i did not found anything")

                    case _ if  'open stackoverflow' in query:
                        webbrowser.open("stackoverflow.com")

                    case _ if  'say good about me' in query:
                        speak("I believe you will become python developer one day...keep it up i am with you")

                    case _ if  query in Battery:
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

                    case _ if  'play music' in query:
                        music_dir = r'C:\Users\KISHAN DEV\Desktop\Anjali\my songs'
                        songs = os.listdir(music_dir)
                        song = random.choice(songs)
                        # print(songs)
                        os.startfile(os.path.join(music_dir, song))

                    case _ if  'the time' in query:
                        strTime = datetime.datetime.now().strftime("%I:%M:%p")
                        speak(f"Sir, the time is {strTime}")

                    case _ if  query in vol1:
                        speak("OK SIR!,Increasing Volume")
                        pyautogui.press("volumeup")

                    case _ if  query in vol2:
                        speak("Alright Sir!...Deacreasing Volume")
                        pyautogui.press("volumedown")

                    case _ if  query in vol_mute:
                        speak("OK Sir...Going Mute")
                        pyautogui.press("volumemute")

                    case _ if  'email to me' in query:
                        try:
                            speak("What should I say?")
                        
                            content = listen()
                            to = "kishandevprajapati4@gmail.com"
                            sendEmail(to, content)
                            speak("Email has been sent!")
                            print("Email has been sent!")
                        except Exception as e:
                            print(e)
                            speak("Sorry my friend . I am not able to send this email")

                    case _ if  query in close:
                        speak("Aright Sir... I AM Going Offline...You Can Call Me Anytime")
                        sys.exit()
                    case _  if  'open' in query:
                        if  '.com' in query or '.org' in query or '.in' in query:
                            query = query.replace('open', '')
                            query = query.replace('jarvis', '')
                            query = query.replace('launch', '')
                            query = query.replace(' ', '')
                            webbrowser.open(query)
                            speak(f"Alright Sir opening {query}")
                        else:
                            apps = list(dict_app.keys())
                            for ap in apps:
                                if ap in query:
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

