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
