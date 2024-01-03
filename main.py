# import main_voice
# main_voice.run_assistant()
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
from tkinter import messagebox  # Import messagebox module
import main_voice

# Rest of your functions...

def activate_assistant():
    # Function to activate the vocal assistant (You can add your functionality here)
    print("Vocal assistant activated!")
    main_voice.run_assistant()

def show_description():
    # Function to show a brief description of the assistant
    description = "Buna ziua si bine ati venit la olarit cu brad pitt"
    messagebox.showinfo("Assistant Description", description)


def resize_and_mask_image(image_path, size):
    # Resize the image to fit the circular button and apply a circular mask
    img = Image.open(image_path)
    img = img.resize((size, size), Image.BICUBIC)

    # Create a circular mask
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    # Apply the circular mask to the image
    masked_image = ImageTk.PhotoImage(Image.composite(img, Image.new('RGB', (size, size), 'white'), mask))

    return masked_image
def create_main_window():
    root = tk.Tk()
    root.title("Voice Assistant")

    # Define the desired width and height for the button image
    button_width = 50
    button_height = 50

    # Customize colors
    bg_color = "#f0f0f0"  # Light gray background
    button_bg = "#4CAF50"  # Green button background
    button_fg = "white"    # Text color for buttons

    # Set window background color
    root.configure(bg=bg_color)

    # Resize the image to fit the button
    resized_image = resize_and_mask_image("C:\\Users\\Minea\\PycharmProjects\\pythonProject\\qm.png", button_width)  # Replace with your image path

    # Button to activate the vocal assistant
    activate_button = tk.Button(root, text="Activate Assistant", command=activate_assistant, width=20, bg=button_bg, fg=button_fg)
    activate_button.pack(padx=20, pady=20)

    # Button with resized image for assistant description
    description_button = tk.Button(root, image=resized_image, command=show_description, width=button_width, height=button_height, bg=button_bg)
    description_button.image = resized_image  # To prevent image garbage collection
    description_button.pack(pady=10)

    root.mainloop()

# Create the main window
create_main_window()
# def create_main_window():
#     root = tk.Tk()
#     root.title("Voice Assistant")
#
#     # Define the desired width and height for the button image
#     button_width = 50
#     button_height = 50
#
#     # Resize the image to fit the button
#     resized_image = resize_image("C:\\Users\\Minea\\PycharmProjects\\pythonProject\\qm.png", button_width, button_height)  # Replace with your image path
#
#     # Button to activate the vocal assistant
#     activate_button = tk.Button(root, text="Activate Assistant", command=activate_assistant, width=20)
#     activate_button.pack(padx=20, pady=30)
#
#     # Button with resized image for assistant description
#     description_button = tk.Button(root, image=resized_image, command=show_description, width=button_width, height=button_height)
#     description_button.image = resized_image  # To prevent image garbage collection
#     description_button.pack(pady=10)
#
#     root.mainloop()
#
# # Create the main window
# create_main_window()
