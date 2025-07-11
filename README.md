# 🎙️ Gemini Voice Assistant (Python)

An interactive **voice assistant** powered by **Google Gemini** that listens to your voice, understands it, and responds back using text-to-speech.  
Perfect for exploring the potential of **AI + Python + Voice Tech**! 🚀

---

## 🧠 Features

- 🎤 Speech recognition using `speech_recognition`
- 🧠 AI-powered responses via **Gemini (Google Generative AI)**
- 🔊 Text-to-speech replies using `pyttsx3`
- 🔐 Secure API key handling with `.env`
- 🛑 Exit command support: say `"exit"`, `"quit"`, or `"bye"`

---

## ⚙️ Tech Stack

| Tool           | Role                              |
|----------------|-----------------------------------|
| Python         | Core programming language         |
| Google Gemini  | Generates AI-powered responses    |
| speech_recognition | Converts voice to text         |
| pyttsx3        | Converts text back to voice       |
| python-dotenv  | Handles API keys securely         |

---

## 📁 Project Structure

```bash
Gemini-Voice-Assistant/
┣ 📜 gemini_voice.py
┣ 📜 .env # (not uploaded to GitHub)
┣ 📜 .gitignore
┗ 📜 README.md
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

Make sure you have Python installed. Then install the required packages:

```bash
pip install google-generativeai
pip install pyttsx3
pip install SpeechRecognition
pip install python-dotenv
```

🛡️ API Key Setup
Create a .env file in the root directory and add your Gemini API key:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

▶️ How to Run
Simply run the script:
```bash
python gemini_voice.py
```
Then speak into your mic when prompted. Try asking:

"Tell me a joke"

"What's the weather like?"

"Who is Alan Turing?"

Say "exit" or "bye" or "quit" to end the assistant.

📸 Demo Preview
```bash
🤖 Gemini Voice Assistant is ready. Say something!
🎙️ Listening...
You said: Hello Gemini
Gemini: Hello! How can I assist you today?
```
🙋‍♀️ About Me
Hi, I'm Kissa Zehra 👋
CS Undergrad @ NUCES-FAST, passionate about building smart & helpful tools through code.
Exploring AI, Machine Learning, and Real-World Automation.

