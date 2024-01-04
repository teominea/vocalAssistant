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
import tetris
import doodle_jump
from set_reminder import set_reminder
from celebrity import search_actress_images_on_google
from movie import get_recipe
import customtkinter
wikipedia.set_lang("en")

no_of_calls = 0

def main():
    global no_of_calls
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    no_of_calls = 0

    word_to_int = {
        'one': 1,
        'five': 5,
        'ten': 10,
        'fifteen': 15,
        'thirty': 30
    }

    def talk(text):
        engine.say(text)
        engine.runAndWait()

    def update_interface(command, output_text):
        output_text = f"\n{output_text}\n"
        text_widget.insert(tk.END, output_text)

    def take_command():
        try:
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source, duration=1)
                print('listening...')
                update_interface("", "listening...")
                voice = listener.listen(source)
                c = listener.recognize_google(voice)
                c = c.lower()
                return c
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            update_interface("", "Sorry, I could not understand what you said.")
            return 'nothing'
        except Exception as e:
            print(f"Error during recognition: {e}")
            return 'nothing'

    def run_assistant():

        global text_widget
        with open('C:\\Users\\Minea\\PycharmProjects\\pythonProject\\nickname.txt', 'r') as file:
            # Read a line from the file
            nickname = file.readline()
        file.close()

        global no_of_calls
        if no_of_calls == 0:
            talk('hello ' + nickname)
            update_interface("", f"Hello {nickname}")
            no_of_calls = 1

        while True:
            command = take_command()
            if command == 'exit':
                talk('Turning off')
                update_interface(command, "Assistant turned off")
                os._exit(1000)


            elif command == 'what is the time':
                time_curr = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is ' + time_curr)
                update_interface(command, f"Current time is {time_curr}")


            elif command == 'i want to learn':
                talk('about what ?')
                update_interface(command, "About what?")
                subject = take_command()
                summary = wikipedia.summary(subject, sentences=3)
                talk(summary)
                update_interface(command, summary)

            elif command == 'translate':
                talk('what?')
                update_interface(command, "What?")
                sentence = take_command()
                talk('to what language?')
                update_interface(command, "To what language?")
                language = take_command()
                translator = Translator(to_lang=language)
                translation = translator.translate(sentence)
                talk(translation)
                update_interface(command, translation)

            elif command == 'tell me a joke':
                joke = pyjokes.get_joke('en')
                talk(joke)
                update_interface(command, joke)

            elif command == 'set nickname':
                talk('what nickname would you like')
                update_interface(command, "What nickname would you like?")
                nickname = take_command()
                with open("nickname.txt", 'w') as file:
                    file.write(nickname)
                file.close()
                update_interface(command, f"Nickname set to {nickname}")

            elif command == 'search on google':
                talk("What should i search?")
                update_interface(command, "What should I search?")
                video = take_command()
                google_url = "https://www.google.com/search?q="
                search_url = google_url + quote(video)
                update_interface(command, f"Searching for {video} on Google")
                webbrowser.open(search_url)
                os._exit(1000)

            elif 'play' in command:
                song = command.replace('play', '')
                talk('playing' + song)
                update_interface(command, f"Playing {song}")
                pywhatkit.playonyt(song)
                os._exit(1000)

            elif command == 'set a reminder':
                talk("For how many minutes? 1, 5, 10, 15 or 30?")
                # minutes = take_command()
                minutes = word_to_int.get(take_command().lower(), None)
                set_reminder(minutes)
                reminder_thread = threading.Thread(target=set_reminder, args=(minutes,))
                reminder_thread.start()
                # run_assistant()
                talk(f"Reminder set for {minutes} minutes")
                update_interface(command, f"Reminder set for {minutes} minutes")

            elif command == 'launch snake':
                talk("Launching Snake game")
                snake.main()
                update_interface(command, "Snake game played")

            elif command == 'launch tetris':
                talk("Launching Tetris game")
                tetris.main()
                update_interface(command, "Tetris game played")

            elif command == 'launch doodle jump':
                talk("Launching Doodle Jump game")
                doodle_jump.main()
                update_interface(command, "Doodle Jump game played")

            elif command == 'take a note':
                talk("What should the note be ?")
                update_interface(command, "What should the note be?")
                note = take_command()

                def add_to_notes(content):
                    with open("C:\\Users\\Minea\\PycharmProjects\\pythonProject\\mynotes.txt", 'a') as file_for_notes:
                        file_for_notes.write(content + '\n')

                add_to_notes(note)
                update_interface(command, "Note added")

            elif command == 'read my notes':
                with open("C:\\Users\\Minea\\PycharmProjects\\pythonProject\\mynotes.txt",
                          'r') as file_for_reading_notes:
                    content = file_for_reading_notes.read()
                talk(content)
                update_interface(command, content)

            elif command == 'clear my notes':
                with open("C:\\Users\\Minea\\PycharmProjects\\pythonProject\\mynotes.txt", 'w') as file_for_wipe:
                    file_for_wipe.truncate()
                update_interface(command, "Notes cleared")

            elif command == 'nothing':
                print("no input detected")
                update_interface(command, "No input detected")

            elif command == 'thank you':
                talk('you are welcome')
                update_interface(command, "You are welcome")

            elif command == 'search celebrity':
                talk("Which celebrity would you like to search?")
                update_interface(command, "Which celebrity would you like to search?")
                actress_name = take_command()
                images_result = search_actress_images_on_google(actress_name)
                update_interface(command, images_result)
                talk(images_result)
                os._exit(1000)

            elif command == 'search movie':
                talk("What movie should I search for?")
                update_interface(command, "What movie should I search for?")
                movie_name = take_command()

                # Construiește URL-ul de căutare pentru Google
                search_url = f"https://www.imdb.com/find?q={movie_name}&s=tt"

                # Deschide browser-ul web cu URL-ul de căutare
                webbrowser.open(search_url)
                talk(f"Searching for {movie_name} on IMDb.")
                update_interface(command, f"Searching for {movie_name} on IMDb.")
                os._exit(1000)

            elif command == 'search recipe':
                talk("What recipe should I search for?")
                update_interface(command, "What recipe should I search for?")
                recipe_name = take_command()
                search_url = f"https://tasty.co/search?q={recipe_name}&sort=popular"
                webbrowser.open(search_url)
                talk("Searching for {recipe_name} on Tasty.")
                update_interface(command, f"Searching for {recipe_name} on Tasty.")
                os._exit(1000)

            elif command == 'how is the weather':
                talk("What city should I search for?")
                update_interface(command, "What city should I search for?")
                city_name = take_command()
                search_url = f"https://www.weather-forecast.com/locations/{city_name}/forecasts/latest"
                webbrowser.open(search_url)
                update_interface(command, f"Searching for {city_name} on Weather Forecast.")
                os._exit(1000)

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    root = customtkinter.CTk()
    root.geometry("500x400")
    root.title("Vocal Assistant Interface")

    text_widget = customtkinter.CTkTextbox(root, height=400, width=500)
    text_widget.pack()

    assistant_thread = threading.Thread(target=run_assistant)
    assistant_thread.start()

    root.mainloop()
