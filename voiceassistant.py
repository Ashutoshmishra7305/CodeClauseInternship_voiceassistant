import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "goodbye" in command or "bye" in command:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("I'm sorry, I don't understand that command.")

if _name_ == "_main_":
    speak("Hello! I'm your voice assistant.")
    
    while True:
        command = listen()
        process_command(command)
