# 🎙️ Speak Smart System - AI-Powered Voice Assistant

Speak Smart System is a Python-based desktop voice assistant that enables users to interact with an intelligent AI system through voice commands. The application converts speech to text, processes user queries using Natural Language Processing (NLP), and responds with synthesized speech through an interactive graphical user interface.

## 🚀 Features

- Real-time speech recognition using SpeechRecognition
- AI-powered response generation using Cohere API
- Text-to-speech functionality using pyttsx3
- User-friendly desktop GUI built with PyQt5
- Voice input and spoken output interaction
- Modular frontend and backend architecture
- Easy to extend with additional commands and features

---

## 🛠️ Tech Stack

- Python
- PyQt5
- SpeechRecognition
- pyttsx3
- Cohere API
- Threading
- File-based data storage

---

## 📂 Project Structure

```text
Speak-Smart-System/
│
├── Frontend/
│   ├── GUI.py
│   ├── files/
│   │   ├── Database.data
│   │   ├── Mic.data
│   │   ├── Responses.data
│   │   └── Status.data
│   │
│   └── images/
│       ├── Chat.png
│       ├── Home.png
│       ├── mic.png
│       ├── mute.png
│       ├── atlas.gif
│       └── other UI assets
│
├── backend/
│   └── Backend functionality modules
│
├── data/
│   └── Application data and configuration files
│
├── Main.py
├── Requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. The user speaks through the microphone.
2. SpeechRecognition converts the speech into text.
3. The query is sent to the Cohere API for processing.
4. The NLP model generates a context-aware response.
5. pyttsx3 converts the response into speech.
6. The response is displayed in the GUI and spoken back to the user.

---

## 🔧 Installation

### Clone the Repository

```bash
git clone https://github.com/kashishsrivas/Speak-Smart-System.git
cd Speak-Smart-System
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### Install Required Dependencies

```bash
pip install -r Requirements.txt
```

---

## ▶️ Running the Application

Run the application using:

```bash
python Main.py
```

---

## 💡 Key Capabilities

- Voice-based user interaction
- Intelligent question answering
- AI-driven conversational responses
- Speech synthesis for natural communication
- Desktop GUI for seamless user experience

---

## 👨‍💻 Author

**Kashish Srivastava**
