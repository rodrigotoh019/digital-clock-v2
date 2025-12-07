import customtkinter as ctk     # More flexible and modern tkinter
import tkinter.font as tkFont   # To be able to use text in a tkinter window
import os
from tkinter import colorchooser
from datetime import datetime
import pytz     # This gives us access to different timezone
import pyglet   # We're only using the font registration feature (customized .ttf fonts)
from fontTools.ttLib import TTFont  # Can accurately check your customized font's family name

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")     # Options: "dark", "light", "system"
ctk.set_default_color_theme("blue") # Options: "blue", "green", "dark-blue"

# Create main window
root = ctk.CTk()
root.title("Baby-lou ❤️") # This is the name at the window when you open the .exe
root.geometry("280x100")  # Default size of the window
root.resizable(False, False)  # True = resizable, False = not resizable window
root.attributes('-topmost', True)  # Stay on top

# Font Dict and Family
fonts = {
    "Default": {                    # Nickname/Name
        "filename": "DS-DIGI.TTF",  # File Name/Path
        "family": "DS-Digital",     # Family/Real Name
    },
    "Squares": {
        "filename": "square_sans_serif_7.ttf",
        "family": "Squre Sans Serif 7",
    },
    "Comic": {
        "filename": "Sophiecomic-Regular.ttf",
        "family": "Sophiecomic",
    },
    "Round": {
        "filename": "Bartino-Regular.ttf",
        "family": "Bartino",
    },
    "Sunshine": {
        "filename": "A little sunshine.ttf",
        "family": "font18",
    }
}

# OS path compiler
base_path = os.path.dirname(__file__)

loaded_fonts = {}   # Storing nicknames for existing paths
for name, font_data in fonts.items():   # Unpacking nickname (name) = key, and filename and family name = values of the font family
    filename = font_data["filename"]    # Assigning filename/path value
    family_name = font_data["family"]   # Assigning real name/family name value
    font_path = os.path.join(base_path, "assets", "fonts", filename)    # Manually directing where to see the assets (fonts) - Relative-related path
    if os.path.exists(font_path):       # Using .path.exists() method of os to check if the path/file really exists
        pyglet.font.add_file(font_path)
        font_obj = tkFont.Font(family=family_name)
        loaded_fonts[name] = font_obj   # Getting the "name" or nickname of each corresponding "path" or files in font family
        print(f"Loaded Font: {name} - {family_name}")
    else:
        print(f"Font '{name}' not found. The file '{filename}' may be missing or needs to be re-installed.")    # Error-handling message that caters for both user and dev for easier troubleshooting
print("All fonts successfully loaded")

font_names = list(loaded_fonts.keys())  # Getting font's nicknames

# Font index for changing font
current_time_font_index = 0
current_date_font_index = 0

# Changing time fonts
def change_time_fonts(direction):
    global current_time_font_index
    if direction == "next":
        current_time_font_index = (current_time_font_index + 1) % len(font_names)
    else:
        current_time_font_index = (current_time_font_index - 1) % len(font_names)
    font_nicknames = font_names[current_time_font_index]
    font_family = loaded_fonts[font_nicknames].actual("family")
    time_label.configure(font=(font_family, 32))
    print(f"Time changed to: {font_nicknames}")

# Changing date fonts
def change_date_fonts(direction):
    global current_date_font_index
    if direction == "next":
        current_date_font_index = (current_date_font_index + 1) % len(font_names)
    else:
        current_date_font_index = (current_date_font_index - 1) % len(font_names)
    font_nicknames = font_names[current_date_font_index]
    font_family = loaded_fonts[font_nicknames].actual("family")
    date_label.configure(font=(font_family, 16))
    print(f"Date changed to: {font_nicknames}")

# Time arrows
time_left = ctk.CTkButton(root, text="<", width=20, command=lambda: change_time_fonts("prev"))
time_left.place(x=10, y=15)
time_right = ctk.CTkButton(root, text=">", width=20, command=lambda: change_time_fonts("next"))
time_right.place(x=245, y=15)

# Date arrows
date_left = ctk.CTkButton(root, text="<", width=20, command=lambda: change_date_fonts("prev"))
date_left.place(x=10, y=62)
date_right = ctk.CTkButton(root, text=">", width=20, command=lambda: change_date_fonts("next"))
date_right.place(x=245, y=62)


# Timezone label
ph_timezone = pytz.timezone("Asia/Manila")  # Philippines Timezone

#Time and Date font
time_font = (loaded_fonts["Default"].actual("family"),32)   # ctk's way of loading fonts
date_font = (loaded_fonts["Sunshine"].actual("family"),16)

# Time and Date label
time_label = ctk.CTkLabel(root, text="", font=time_font, text_color="light green")
time_label.pack(pady=(10,0))    # pady lets time widget be pushed 10 pixel down from the top of the window

date_label = ctk.CTkLabel(root, text="", font=date_font, text_color="light green")
date_label.pack(pady=(20,0))

# Function to update time & date
def update_clock():
    now = datetime.now(ph_timezone)     # This clock's timezone is set as GMT+8 or PHT / You can leave it blank if you want to this to be based on the timezone of your computer
    time_str = now.strftime("%I:%M:%S %p")  # HH:MM:SS AM/PM
    date_str = now.strftime("%A, %B %d, %Y")  # Day, Month Day, Year

    # when the clock is updating, .config keeps the format of the widgets aka time and date intact
    time_label.configure(text=time_str) # from .config(), you need to change this to .configure() for ctk
    date_label.configure(text=date_str)

    root.after(1000, update_clock)  # 1000ms = 1 sec. This line enable to "loop" the update_clock function every 1 second

# Start updating
update_clock()  # This make the looping reflect to the GUI = clock ticking

# Run the window
(root.mainloop())