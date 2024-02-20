import speech_recognition as sr
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Define a function to perform actions
def perform_action(command):
    if "open notepad" in command:
        os.system("notepad")
    elif "open calculator" in command:
        os.system("calc")
    elif "search Google" in command:
        search_query = command.replace("search Google", "")
        os.system(f"start https://www.google.com/search?q={search_query}")
    else:
        print("Command not recognized.")

# Main loop
while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        command = recognizer.recognize_google(audio).lower()
        print("You said: " + command)
        perform_action(command)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition; {0}".format(e))
