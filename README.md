# 🕰️ Digital Clock v2 – Tkinter Edition

A customizable digital clock app built using Python's Tkinter GUI library. Designed for simplicity, customization, and future extensibility.

---

## ✨ Features (v2 – In Progress)

* ⏰ **12-hour time format with AM/PM indicator**
* 🖋️ **Custom font support** using `.ttf` files
* 📂 **Font loader** with friendly-named dictionary (e.g., "Comic", "Digital")
* ⚠️ **Missing font fallback**: alerts dev and uses default font
* 🖍️ **Scalable font sizing** (presets per widget planned)
* 🎨 **UI customization groundwork** (color, background, layout presets)
* 📐 Resizable and always-on-top toggle (coming soon)

---

## 🚧 Planned Features (v2.x – Post-Release)

* 🎚️ Font size presets: Small, Medium, Large
* 🧭 Layout presets: date below, left/right aligned, centered
* 🌈 Background customization (solid colors or image uploads)
* 🖍️ Font color selector (basic palette)
* 🎨 Theme presets: Modern, Retro, Neon, Minimalist
* 👀 **Font Tester** GUI (preview fonts/sizes before applying)
* 🧪 `try-except` logic for robust font loading
* 📘 User-friendly error prompts and troubleshooting guide

---

## 🌟 Future Features (v3+ Wishlist)

> Ambitious upgrades for full customization and smart features.

* ⏸️ Pause/Resume time display
* ⏰ Basic alarm or reminder alerts
* 🌗 Light/Dark theme toggle
* 🖱️ Drag-and-drop layout positioning
* 📱 Mobile app or network control panel
* 📸 Export layout as image / screenshot
* 🔧 Settings editor GUI (font, color, layout, themes)

---

## 📌 What's New (v2 Highlights)

* ✅ Switched from 24-hour to **12-hour time**
* ✅ Integrated **named font loading** system
* ✅ Added initial **fallback handling** for missing fonts
* ✅ Structured code for layout and theme customization
* ✅ Planned v2.x & v3 features based on feedback & future vision

---

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🧠 Notes for Developers

* Font files should be placed in the same directory or a dedicated `/fonts/` folder
* New fonts must be added to the `fonts = {}` dictionary using a friendly key name
* Error handling is logged for developer debugging; future versions will include user prompts

---

## 🙌 Credits

Created with Python, Tkinter, and way too much coffee ☕

Mentored and guided by **Beemo**, your AI coding buddy 💡