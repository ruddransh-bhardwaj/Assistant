import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import wikipedia
import datetime

# Voice engine
engine = pyttsx3.init()
engine.setProperty('rate',170)

recognizer = sr.Recognizer()

# Speak
def speak(text):
    print("\nAI:", text)
    engine.say(text)
    engine.runAndWait()

# Listen
def listen():

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=0.5
        )

        audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=8
        )

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text.lower()

    except:
        return ""

# Commands
def process(command):

    # Exit
    if "stop" in command or "exit" in command:
        speak("Goodbye")
        return False

    # Open websites
    elif "youtube" in command:
        webbrowser.open(
            "https://youtube.com"
        )
        speak("Opening YouTube")

    elif "google" in command:
        webbrowser.open(
            "https://google.com"
        )
        speak("Opening Google")

    elif "github" in command:
        webbrowser.open(
            "https://github.com"
        )
        speak("Opening GitHub")

    elif "linkedin" in command:
        webbrowser.open(
            "https://linkedin.com"
        )
        speak("Opening LinkedIn")

    elif "twitter" in command:
        webbrowser.open(
            "https://twitter.com"
        )
        speak("Opening Twitter")

    # Apps
    elif "calculator" in command:
        subprocess.Popen("calc")
        speak("Opening Calculator")

    elif "notepad" in command:
        subprocess.Popen("notepad")
        speak("Opening Notepad")

    elif "whatsapp" in command:
        subprocess.Popen("whatsapp")
        speak("Opening WhatsApp")

    elif "spotify" in command:
        subprocess.Popen("spotify")
        speak("Opening Spotify")

    elif "vscode" in command:
        subprocess.Popen("code")
        speak("Opening Visual Studio Code")

    elif "chrome" in command:
        subprocess.Popen("chrome")
        speak("Opening Google Chrome")

    elif "edge" in command:
        subprocess.Popen("msedge")
        speak("Opening Microsoft Edge")

    elif "firefox" in command:
        subprocess.Popen("firefox")
        speak("Opening Mozilla Firefox")

    elif "discord" in command:
        subprocess.Popen("discord")
        speak("Opening Discord")

    elif "file explorer" in command:
        subprocess.Popen("explorer")
        speak("Opening File Explorer")

    # Time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    # Wikipedia AI-like answer
    else:

        try:
            result = wikipedia.summary(
                command,
                sentences=2
            )
            speak(result)

        except:
            speak(
                "Sorry, I could not find information."
            )

    return True

# Main
def main():

    print("===== JARVIS READY =====")

    speak("Assistant ready")

    running = True

    while running:

        command = listen()

        if command:
            running = process(command)

if __name__ == "__main__":
    main()