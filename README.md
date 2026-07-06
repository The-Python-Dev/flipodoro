# Flipodoro

> A minimal, beautiful flip clock Pomodoro timer for Windows.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Download

**[Download Flipodoro.exe (Latest Release)](https://github.com/The-Python-Dev/flipodoro/releases/latest)**

No installation required. No Python needed. Double click and go.

---

## Features

- Flip clock display with satisfying flip animation on every tick
- Three session types: Focus, Short Break, and Long Break
- Fully customisable session durations
- Dark theme easy on the eyes for long sessions
- Focus mode: fullscreen, distraction-free (ESC to exit)
- Keyboard shortcuts for quick control
- Offline-first: no accounts, no cloud, just a timer
- Standalone .exe: send to friends, they double click, it works

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| Space | Start / Pause |
| R | Reset |
| S | Skip |
| F | Toggle focus mode |
| Esc | Exit focus mode |
| Ctrl + , | Open settings |

---

## Run From Source

Requires Python 3.10 or later.

    git clone https://github.com/The-Python-Dev/flipodoro.git
    cd flipodoro
    python run.py

No third-party dependencies. Standard library only.

---

## Build Your Own EXE

    pip install pyinstaller
    python -m PyInstaller --onefile --windowed --name Flipodoro --icon=src/assets/icon.ico --add-data "src/assets;assets" run.py

Output: `dist/Flipodoro.exe`

---

## Project Structure

    flipodoro/
    ├── run.py
    ├── src/
    │   ├── core/
    │   │   ├── timer.py
    │   │   ├── settings.py
    │   │   └── constants.py
    │   ├── ui/
    │   │   ├── app.py
    │   │   ├── timer_view.py
    │   │   ├── settings_view.py
    │   │   ├── flip_clock.py
    │   │   └── theme.py
    │   └── assets/
    │       └── icon.ico
    └── .gitignore

---

## Known Issues (V1.0.0)

- Custom icon does not appear in taskbar/title bar while app is running
- Maximum practical duration is 99 minutes (display limit)
- Flip clock does not scale with window resize

All fixes planned for V1.1.

---

## Roadmap

**V1.1**
- Fix taskbar/title bar icon
- Support durations above 99 minutes
- Responsive flip clock scaling
- Custom completion sound

**V1.2**
- System tray support
- Always-on-top toggle

---

## Built With

- Python 3
- Tkinter (standard library)
- PyInstaller (for the .exe)

---

## License

MIT License

---

## Author

Made by [Om Dautkhani](https://github.com/The-Python-Dev)

Built in one 11-hour focused session.
