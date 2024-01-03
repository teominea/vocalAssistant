import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os
import pyjokes
from translate import Translator
import webbrowser
from urllib.parse import quote
import threading
import time
import tkinter as tk
import snake
wikipedia.set_lang("en")

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
no_of_calls = 0

word_to_int = {
    'five': 5,
    'ten': 10,
    'fifteen': 15,
    'thirty': 30
}
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source,duration=1)
            print('listening...')
            voice = listener.listen(source)
            c = listener.recognize_google(voice)
            c = c.lower()
            return c
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return 'nothing'
    except Exception as e:
        print(f"Error during recognition: {e}")
        return 'nothing'

def run_assistant():
    with open('C:\\Users\\Minea\\PycharmProjects\\pythonProject\\nickname.txt', 'r') as file:
        # Read a line from the file
        nickname = file.readline()
    file.close()

    global no_of_calls
    if no_of_calls == 0:
        talk('hello ' + nickname)
        no_of_calls = 1

    while True:
        command = take_command()
        if command == 'exit':
            talk('Turning off')
            os._exit(1000)


        elif command == 'what is the time':
            time_curr = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time_curr)


        elif command == 'i want to learn':
            talk('about what ?')
            subject =take_command()
            summary=wikipedia.summary(subject,sentences = 3)
            talk(summary)

        elif command == 'translate':
            talk('what?')
            sentence=take_command()
            talk('to what language')
            language=take_command()
            translator=Translator(to_lang=language)
            translation=translator.translate(sentence)
            talk(translation)

        elif command == 'tell me a joke':
            joke = pyjokes.get_joke('en')
            talk(joke)

        elif command == 'set nickname':
            talk('what nickname would you like')
            nickname = take_command()
            with open("nickname.txt",'w') as file :
                file.write(nickname)
            file.close()

        elif command == 'play youtube':
            # nu stie sa se mai intoarca dupa ce da play
            talk("What should i play")
            video = take_command()
            youtube_url = "https://www.youtube.com/results?search_query="
            search_url = youtube_url + quote(video)
            webbrowser.open(search_url)

        elif command == 'set a reminder':
            talk("For how many minutes? 5, 10, 15 or 30?")
            # minutes = take_command()
            minutes = word_to_int.get(take_command().lower(), None)
            seconds = minutes * 60
            time.sleep(seconds)

            def display_reminder():
                root = tk.Tk()
                root.title("Reminder")
                label = tk.Label(root, text=f"Time's up! {minutes} minutes have passed.")
                label.pack(padx=10, pady=10)
                root.mainloop()

            # Create a thread to display the reminder
            reminder_thread = threading.Thread(target=display_reminder)
            reminder_thread.start()

        elif command == 'play snake':
            snake.main()
        elif command == 'nothing':
            print("no input detected")
        elif command == 'thank you':
            talk('you are welcome')


