# 🎙️ Speak Smart System - AI-Powered Voice Assistant

Speak Smart System is a desktop-based AI voice assistant built with Python that enables users to interact through natural voice commands. The assistant captures speech in real time, converts it to text, processes user queries using AI-powered Natural Language Processing (NLP), and responds with human-like speech.

## 🚀 Features

- 🎤 Real-time voice input using SpeechRecognition
- 🤖 AI-powered query understanding with Cohere API
- 🔊 Natural text-to-speech responses using pyttsx3
- 🖥️ Interactive desktop GUI built with PyQt5
- 🧠 Context-aware response generation
- ⚙️ Modular architecture for easy scalability and maintenance

## 🛠️ Tech Stack

- **Programming Language:** Python
- **GUI Framework:** PyQt5
- **Speech Recognition:** SpeechRecognition
- **Text-to-Speech:** pyttsx3
- **Natural Language Processing:** Cohere API

## 📂 Project Structure

```text
Speak-Smart-System/
│
├── gui/
│   ├── main_window.py
│
├── speech/
│   ├── speech_to_text.py
│   ├── text_to_speech.py
│
├── nlp/
│   ├── cohere_service.py
│
├── assets/
│
├── main.py
├── requirements.txt
└── README.md
```

## ⚡ How It Works

1. User speaks through the microphone.
2. SpeechRecognition converts speech into text.
3. The query is sent to the Cohere NLP model.
4. Cohere processes the query and generates an intelligent response.
5. pyttsx3 converts the response into spoken audio.
6. The response is displayed in the PyQt5 interface and spoken aloud.

## 📸 Key Functionalities

- Voice Command Processing
- Speech-to-Text Conversion
- AI-Based Question Answering
- Text-to-Speech Synthesis
- User-Friendly Desktop Interface

## 🔧 Installation

### Clone the Repository

```bash
git clone https://github.com/kashishsrivas/speak-smart-system.git
cd speak-smart-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

```bash
python main.py
```

## 👨‍💻 Author

**Kashish Srivastava**

