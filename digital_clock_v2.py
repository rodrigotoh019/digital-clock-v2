import tkinter as tk
import tkinter.font as tkFont
import os
from tkinter import colorchooser
from datetime import datetime

# Create main window
root = tk.Tk()
root.title("Bibi Time ❤️") # This is the name at the window when you open the .exe
root.geometry("300x100")  # Default size of the window
root.resizable(True, True)  # Adjustable window
root.attributes('-topmost', True)  # Stay on top

# Font Family
fonts = {
    "Default": "DS-DIGI.TTF",
    "Squares": "square_sans_serif_7.ttf",
    "Comic": "Sophiecomic-Regular.ttf",
    "Round": "Bartino-Regular.ttf",
    "Sunshine": "A little sunshine.ttf"
}

loaded_fonts = {}   # Storing nicknames for existing paths
for name, path in fonts.items():    # Unpacking nickname (name) and file name (path) of the font family
    if os.path.exists(path):        # Using .path.exists() method of os to check if the path/file really exists
        font_obj = tkFont.Font(file=path, size=32)  # file=path is saying I have customized fonts at font family, and size=32 is the font size
        loaded_fonts[name] = font_obj   # Getting the "name" or nickname of each corresponding "path" or files in font family
    else:
        print(f"Font '{name}' not found. The file '{path}' may be missing or needs to be re-installed.")    # Error-handling message that caters for both user and dev for easier troubleshooting

# Time label
time_label = tk.Label(root, text="", font=loaded_fonts["Default"])
time_label.pack()

# Date label
date_label = tk.Label(root, text="", font=loaded_fonts["Default"])
date_label.pack()

# Function to update time & date
def update_clock():
    now = datetime.now()
    time_str = now.strftime("hh:mm:ss")  # Hint: You want HH:MM:SS
    date_str = now.strftime("dd/mm/yyyy")  # Hint: Day, Month Day, Year

    time_label.config(text=__________)
    date_label.config(text=__________)

    root.after(1000, update_clock)

# Start updating
update_clock()

# Run the window
root.________()
