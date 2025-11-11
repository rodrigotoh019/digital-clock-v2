import tkinter as tk
import tkinter.font as tkFont
import os
from tkinter import colorchooser
from datetime import datetime
import pytz     # This gives us access to different timezone

from Projects.digital_clock_v1.digital_clock_v1 import ph_timezone

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
        font_obj = tkFont.Font(file=path)  # file=path is saying I have customized fonts at font family
        loaded_fonts[name] = font_obj   # Getting the "name" or nickname of each corresponding "path" or files in font family
    else:
        print(f"Font '{name}' not found. The file '{path}' may be missing or needs to be re-installed.")    # Error-handling message that caters for both user and dev for easier troubleshooting

# Timezone label
ph_timezone = pytz.timezone("Asia/Manila")  # Philippines Timezone

#Time and Date font
time_font = tkFont.Font(family=loaded_fonts["Default"].actual("family"), size=32)
date_font = tkFont.Font(family=loaded_fonts["Default"].actual("family"), size=14)

# Time and Date label
time_label = tk.Label(root, text="", font=(time_font), fg="white", bg="black")
time_label.pack(pady=(10,0))    # pady lets time widget be pushed 10 pixel down from the top of the window

date_label = tk.Label(root, text="", font=(date_font), fg="lightgray", bg="black")
date_label.pack()

# Function to update time & date
def update_clock():
    now = datetime.now(ph_timezone)     # This clock's timezone is set as GMT+8 or PHT / You can leave it blank if you want to this to be based on the timezone of your computer
    time_str = now.strftime("%I:%M:%S %p")  # HH:MM:SS AM/PM
    date_str = now.strftime("%A,%B %d, %Y")  # Day, Month Day, Year

    # when the clock is updating, .config keeps the format of the widgets aka time and date intact
    time_label.config(text=time_str)
    date_label.config(text=date_str)

    root.after(1000, update_clock)  # 1000ms = 1 sec. This line enable to "loop" the update_clock function every 1 second

# Start updating
update_clock()  # This make the looping reflect to the GUI = clock ticking

# Run the window
(root.mainloop())
