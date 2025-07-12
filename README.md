
# 🤖 DaJarvis - Personal AI Assistant

DaJarvis is a standalone desktop-based virtual AI assistant inspired by Marvel's Jarvis. It utilizes voice commands, AI-powered conversations, system automation, and a user-friendly PyQt5 GUI to offer an intelligent desktop experience for daily tasks.

> **"I am Jarvis, Sir. Your personal assistant, ready to serve."**

---

## 📂 Project Structure

```
DaJarvis/
├── AIBrain.py               # Handles OpenAI interaction and chat history
├── Functions.py             # Main assistant logic and command handling
├── GreetMe.py               # Time-based greeting system
├── GuiStart.py              # PyQt5 GUI startup
├── Listen.py                # Speech recognition using Google Speech API
├── MailSender.py            # SMTP-based email sending
├── Main.py                  # Entry point for the GUI-based app
├── Speak.py                 # Text-to-speech (TTS) responses
├── Translatr.py             # Google Translate integration
├── UI.py                    # GUI layout and widgets (PyQt5)
└── database/
    └── chat_log.txt         # Stores chat history for continuity
```

---

## 🧠 Features

- 🎤 **Voice Interaction** using Google Speech Recognition
- 🔊 **Text-to-Speech** with natural-sounding responses (pyttsx3)
- 💬 **Conversational AI** using OpenAI's GPT (text-davinci-002)
- 📧 **Email Sending** using SMTP
- 🌐 **Web Automation** (Google search, YouTube play, Stack Overflow)
- 🗣️ **Language Translation** with Google Translate
- 🎭 **Humor and Personality** (jokes, emotions, custom replies)
- 🔋 **Battery Monitoring** using `psutil`
- 🎵 **Music Playback** from local storage
- 🧠 **Self-learning Chat Log** stored in `chat_log.txt`
- 🧱 **Graphical User Interface** built with PyQt5
- 🛠️ **Application Launcher** (Notepad, Paint, Chrome, etc.)

---

## 🖼️ GUI Preview

The GUI is minimalistic and animated using `.gif` backgrounds to simulate Jarvis-like interface aesthetics.

> 📌 Located in `GuiStart.py` and `UI.py`

---

## 🚀 Installation

### Prerequisites

Install the following Python dependencies:

```bash
pip install -r requirements.txt
```

### `requirements.txt` content:

```txt
openai
python-dotenv
pyttsx3
SpeechRecognition
pywhatkit
wikipedia
pyjokes
psutil
pyautogui
googletrans==3.1.0a0
PyQt5
```

---

## 🔐 Setup Environment Variables

Create a `.env` file in the root directory with the following content:

```env
OPENAI_API_KEY=your_openai_api_key
UMAIL=your_email_address
NTMP=your_app_password  # Gmail App Password
```

---

## 🧪 Running the Application

```bash
python Main.py
```

Once launched:

1. Press the `START` button on the GUI.
2. Say **"Hey Jarvis"** to activate the assistant.
3. Speak commands such as:
   - "Open YouTube"
   - "Search Python on Google"
   - "What's the battery percentage?"
   - "Play music"
   - "Send email to me"
   - "Tell me a joke"
   - "Introduce yourself"
   - "Volume up"

---

## 🔐 Security Note

Do **not** expose your `.env` file or credentials in public repositories.

---

## 💡 Future Enhancements

- Add support for **multi-language conversation**
- Integrate **calendar/reminder** features
- Add **face recognition** login or wake-up
- Enhance **chat memory** with database like SQLite
- Dockerize the application for cross-platform compatibility

---

## 👩‍💻 Developed By

**Kishan Dev** and Team  
Special contributions by [@kishandev2509](https://github.com/kishandev2509)

---
<!--
## 📜 License

This project is licensed under the [MIT License](LICENSE)

--->

## 📷 Screenshots

_Add screenshots of the GUI interface and responses here (optional)_

---

## 🌐 Connect with Me

- 💼 GitHub: [kishandev2509](https://github.com/kishandev2509)
- 📧 Email: kishandevprajapati4@gmail.com

---

## 🌟 Show Your Support

If you liked this project, consider giving it a ⭐ on [GitHub](https://github.com/kishandev2509/DAJarvis)!
