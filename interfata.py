import tkinter as tk
from tkinter import messagebox
import main_voice

def call_vocal_assistant():
    # Înlocuiește această linie cu codul tău pentru asistentul vocal
    messagebox.showinfo("Vocal Assistant", "Se apelează asistentul vocal...")
    main_voice.run_assistant()

# Crează fereastra principală
root = tk.Tk()
root.title("Buton Asistent Vocal")

# Calculează 1/8 din lățimea ecranului
# button_width = root.winfo_screenwidth() / 8
button_width = 120
# Stabilește o dimensiune minimă pentru fereastră
root.minsize(120, 100)

# Crează un buton cu lățimea calculată și culoarea albă
button = tk.Button(root, text="Apelează Asistent Vocal", command=call_vocal_assistant, width=button_width, bg="white")

# Plasează butonul în fereastră
button.pack(pady=20)

# Rulează bucla principală de evenimente
root.mainloop()