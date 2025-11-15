import tkinter as tk
import tkinter.font as tkFont
import os
from tkinter import colorchooser
from datetime import datetime
import pytz     # This gives us access to different timezone
import pyglet   # For font registration (customized .ttf fonts)
from fontTools.ttLib import TTFont  # Can accurately check your customized font's family name

# Create main window
root = tk.Tk()
root.title("Baby-lou ❤️") # This is the name at the window when you open the .exe
root.geometry("400x110")  # Default size of the window
root.resizable(False, False)  # True = resizable, False = not resizable window
root.attributes('-topmost', True)  # Stay on top

# Font Dict, font paths/file name
fonts = {
    "Default": "DS-DIGI.TTF",
    "Squares": "square_sans_serif_7.ttf",
    "Comic": "Sophiecomic-Regular.ttf",
    "Round": "Bartino-Regular.ttf",
    "Sunshine": "A little sunshine.ttf"
}

# Font family, names that tkinter can read
font_family = {
    "Default": "DS-Digital",
    "Squares": "Square Sans Serif 7",
    "Comic": "Sophiecomic",
    "Round": "Bartino",
    "Sunshine": "font18"
}

# OS path compiler
base_path = os.path.dirname(__file__)

loaded_fonts = {}   # Storing nicknames for existing paths
for name, filename in fonts.items():    # Unpacking nickname (name) and file name (path) of the font family
    font_path = os.path.join(base_path, "assets", "fonts", filename)
    if os.path.exists(font_path):        # Using .path.exists() method of os to check if the path/file really exists
        pyglet.font.add_file(font_path)
        family_name = font_family[name]
        font_obj = tkFont.Font(family=family_name)
        loaded_fonts[name] = font_obj   # Getting the "name" or nickname of each corresponding "path" or files in font family
        print(f"Loaded Font: {name} - {family_name}")
    else:
        print(f"Font '{name}' not found. The file '{filename}' may be missing or needs to be re-installed.")    # Error-handling message that caters for both user and dev for easier troubleshooting
print("All fonts successfully loaded")

# Window background
root.config(bg="black")

# Timezone label
ph_timezone = pytz.timezone("Asia/Manila")  # Philippines Timezone

#Time and Date font
time_font = tkFont.Font(family=loaded_fonts["Default"].actual("family"), size=32)
date_font = tkFont.Font(family=loaded_fonts["Sunshine"].actual("family"), size=16)

# Time and Date label
time_label = tk.Label(root, text="", font=(time_font), fg="white", bg="black")
time_label.pack(pady=(10,0))    # pady lets time widget be pushed 10 pixel down from the top of the window

date_label = tk.Label(root, text="", font=(date_font), fg="lightgray", bg="black")
date_label.pack()

# Function to update time & date
def update_clock():
    now = datetime.now(ph_timezone)     # This clock's timezone is set as GMT+8 or PHT / You can leave it blank if you want to this to be based on the timezone of your computer
    time_str = now.strftime("%I:%M:%S %p")  # HH:MM:SS AM/PM
    date_str = now.strftime("%A, %B %d, %Y")  # Day, Month Day, Year

    # when the clock is updating, .config keeps the format of the widgets aka time and date intact
    time_label.config(text=time_str)
    date_label.config(text=date_str)

    root.after(1000, update_clock)  # 1000ms = 1 sec. This line enable to "loop" the update_clock function every 1 second

# Start updating
update_clock()  # This make the looping reflect to the GUI = clock ticking

# Run the window
(root.mainloop())