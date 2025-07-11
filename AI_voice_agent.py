import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

recognizer = sr.Recognizer()
engine = pyttsx3.init()

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()

print("🤖 Gemini Voice Assistant is ready. Say something!")

while True:
    try:
        with sr.Microphone() as source:
            print("🎙️ Listening...")
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio)
            print("You said:", user_input)

            if user_input.lower() in ["exit", "quit", "bye"]:
                engine.say("Goodbye!")
                engine.runAndWait()
                break

            reply = ask_gemini(user_input)
            print("Gemini:", reply)

            engine.say(reply)
            engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I didn’t understand that.")
    except sr.RequestError:
        print("Speech Recognition error.")
    except Exception as e:
        print("Error:", e)
