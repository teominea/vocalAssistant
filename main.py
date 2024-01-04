import customtkinter
import main_voice
import threading

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x350")

def run():
    print("Vocal assistant activated!")
    main_voice.main()

def clicked():
    run()

def get_commands():

    commands_window = customtkinter.CTk()
    commands_window.geometry("500x400")
    commands_window.title("Commands")

    commands_label = customtkinter.CTkLabel(master=commands_window, text="Commands:", font=("Times New Roman", 18))
    commands_label.pack(pady=10)

    commands_list = customtkinter.CTkLabel(master=commands_window, font=("Times New Roman", 14),
                                                text="1. Search celebrity\n2. Search movie\n3. Search recipe\n4. What is the time\n5. I want to learn\n"+
                                                     "6. Translate\n7. Tell me a joke\n8. Set nickname\n9. Search on Google\n10. Play a song\n11. Set a reminder\n"+
                                                    "12.Launch a game (Tetris/Snake/Doodle Jump)\n13. Take a note\n14. Read/Clear my notes\n15. How is the weather?")
    commands_list.pack(pady=5)

    close_button = customtkinter.CTkButton(master=commands_window, text="Close", command=commands_window.destroy)
    close_button.pack(pady=10)

    commands_window.mainloop()
def help():
    # customtkinter.messagebox.showinfo("Title", "Message")
    help_window = customtkinter.CTk()
    help_window.geometry("300x200")
    help_window.title("Help")

    help_label = customtkinter.CTkLabel(master=help_window, text="Instructions on using the assistant:", font=("Times New Roman", 18))
    help_label.pack(pady=10)

    instructions_label = customtkinter.CTkLabel(master=help_window, font=("Times New Roman", 14),
                                                text="1. Speak clearly into the microphone.\n2. Click 'Activate Assistant' to trigger the assistant.")
    instructions_label.pack(pady=5)

    close_button = customtkinter.CTkButton(master=help_window, text="Close", command=help_window.destroy, font=("Times New Roman", 15))
    close_button.pack(pady=10)

    command_button = customtkinter.CTkButton(master=help_window, text="Commands", command=get_commands, font=("Times New Roman", 15))
    command_button.pack(pady=20, padx=10)

    help_window.mainloop()

frame = customtkinter.CTkFrame(master = root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master = frame, text="Voice Assistant", font=("Times New Roman", 20))
label.pack(pady=20, padx=10)

button = customtkinter.CTkButton(master = frame, text="Activate Assistant", command=clicked, font=("Times New Roman", 15))
button.pack(pady=20, padx=10)

help_button = customtkinter.CTkButton(master = frame, text="Help", command=help, font=("Times New Roman", 15))
help_button.pack(pady=12, padx=10)

root.mainloop()
