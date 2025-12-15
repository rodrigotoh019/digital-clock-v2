# 🕰️ Baby-lou Clock – Digital Clock v2

A small always-on-top desktop clock built with Python, [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter), and a set of custom fonts.

The app shows the current **time and date in Asia/Manila (GMT+8)**, with simple controls to switch fonts for the time and date separately. User choices are saved so your preferred look is restored on every launch.

---

## ✨ Current Features

- ⏰ **12-hour time format** (HH:MM:SS AM/PM)
- 📅 **Full date display**  
  `Day, Month DD, YYYY` (for example: `Monday, January 01, 2025`)
- 🌏 **Timezone fixed to Asia/Manila (Philippines)**  
  Great for a “desk clock” on a secondary monitor.
- 🖋️ **Custom fonts for time and date**
  - Fonts loaded from `assets/fonts/`
  - Currently included:
    - `Default` → `DS-DIGI.TTF` (digital clock style)
    - `Comic` → `Sophiecomic-Regular.ttf`
    - `Round` → `Bartino-Regular.ttf`
    - `Sunshine` → `A little sunshine.ttf`
- 🔁 **Per-widget font switching**
  - Change **time font** with the top `<` / `>` buttons
  - Change **date font** with the bottom `<` / `>` buttons
- 💾 **Settings persistence**
  - Selected time font and date font are stored in `clock_config.json`
  - On next launch, the app restores your last-used fonts automatically
- 🧱 **Simple, compact window**
  - Title: `Baby-lou ❤️`
  - Default size: `300 x 100`
  - Non-resizable
  - Always on top of other windows
- 🎨 **Dark theme**
  - CustomTkinter dark mode
  - Time & date text in light green

---

## 📂 Project Structure

```text
digital_clock_v2/
├─ assets/
│  └─ fonts/
│     ├─ A little sunshine.ttf
│     ├─ Bartino-Regular.ttf
│     ├─ DS-DIGI.TTF
│     └─ Sophiecomic-Regular.ttf
├─ clock_config.json       # Created/updated at runtime (user font choices)
├─ digital_clock_v2.py     # Main application
├─ font_name_finder.py     # Helper script (optional)
├─ requirements.txt
└─ README.md
```
🔎 clock_config.json is created automatically on first run if it doesn’t exist.

---
## 🧑‍💻 Running from Source (Python)

Recommended if you’re comfortable with Python and want to tweak the code.

**1. Clone the repo**
```text
git clone https://github.com/<your-username>/digital_clock_v2.git
cd digital_clock_v2
```
**2. Create and activate a virtual environment (optional but recommended)**
```text
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
# source venv/bin/activate
```
**3. Install dependencies**
```text
pip install -r requirements.txt
```
**4. Run the app**
```text
python digital_clock_v2.py
```
The clock window should appear, always on top, showing PH time and date. `<` /`>` buttons to cycle through fonts for the time and date.

---
## 💻 Windows Executable (Non-dev Friendly)
If you've built and uploaded a `Baby-lou CLock.exe` to a GitHub Release:
1. Download `Baby-lou Clock.exe` from **Releases** section.
2. Place it in a folder where it can create/write `clock_config.json`.
3. Double-click the `.exe`, copy `clock_config.json` with it to keep your saved preferences.

---
## ⚙️ Configuration Details
The file `clock_config.json` stores the current font choices:
```text
{
  "time_font": "Default",
  "date_font": "Default"
}
```
Valid values (as of v2):
- `Default`
- `Comic`
- `Round`

You can edit this file manually while the app is closed if you want to force a specific font on next launch.

---
## 🧭 Roadmap / Ideas
These are not implemented yet, but are planned or considered for future revisions:
- 🎨 Change text color and/or background color
- 🌐 Switchable timezone (system time vs. fixed Asia/Manila)
- 🎚️ Font size presets (Small / Medium / Large)
- 🎭 Theme presets (Retro, Neon, Minimalist, etc.)
- 🪟 Optional resizable window and layout presets
---
## 🙌 Credits
Built with:
- Python
- CustomTkinter
- tkinter.font
- pytz
- pyglet

Created as a personal micro-tool and learning project.
Mentored by my coding buddies, **Beemo/ChatGPT** and **Claude**.

---
### 📄 `LICENSE` (MIT License)

This project is licensed under the [MIT License.](LICENSE)
