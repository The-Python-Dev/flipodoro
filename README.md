# Flipodoro 🍅

A minimal, beautiful flip clock Pomodoro timer for Windows.

![Version](https://img.shields.io/badge/version-1.0.0-red)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

![Flipodoro](https://github.com/user-attachments/assets/b3a07134-11c0-4322-a1e3-96a271be03de)

---

## Download

**[Download Flipodoro.exe (Latest Release)](https://github.com/The-Python-Dev/flipodoro/releases/latest)**

No installation required. No Python needed. Double click and go.

---

## Features

- Flip clock display with satisfying flip animation on every tick
- Three session types: **Focus**, **Short Break**, and **Long Break**
- Fully customisable session durations (1–99 minutes)
- Session dots indicator showing progress through your Pomodoro cycle
- Session-based accent colors (red / teal / purple)
- Focus mode: fullscreen, distraction-free (ESC to exit)
- Dark theme easy on the eyes for long sessions
- Keyboard shortcuts for quick control
- Settings persist between sessions
- Zero third-party dependencies — pure Python standard library
- Offline-first: no accounts, no cloud, just a timer
- Standalone `.exe`: send to friends, they double click, it works

### Three focus modes

<img src="https://github.com/user-attachments/assets/9e75d785-9115-4c11-830f-334b2a2c66a4" alt="Focus, Short Break, and Long Break modes" width="400">

---

## How It Works

Pick a session type, hit `Space`, and get to work. When the timer completes, Flipodoro moves you to the next session automatically. Focus, break, focus, break — the Pomodoro rhythm, without the noise.

Press `F` to enter Focus Mode for fullscreen distraction-free work. Press `ESC` to exit.

---

## Keyboard Shortcuts

| Key       | Action              |
|-----------|---------------------|
| `Space`   | Start / Pause       |
| `R`       | Reset               |
| `S`       | Skip session        |
| `F`       | Toggle focus mode   |
| `Esc`     | Exit focus mode     |
| `Ctrl + ,`| Open settings       |

---

## Run From Source

Requires Python 3.10 or later. No dependencies to install — Tkinter ships with Python.

```bash
git clone https://github.com/The-Python-Dev/flipodoro.git
cd flipodoro
python run.py
```

![Running from source](https://github.com/user-attachments/assets/ed21596b-c3d7-4d1d-9a64-3919caa996b6)

---

## Build Your Own EXE

```bash
pip install pyinstaller
python -m PyInstaller --onefile --windowed --name Flipodoro --icon=src/assets/icon.ico --add-data "src/assets;assets" run.py
```

Output: `dist/Flipodoro.exe`

---

## Project Structure

```
flipodoro/
├── run.py                    # Entry point
├── src/
│   ├── core/                 # Business logic (no UI)
│   │   ├── timer.py
│   │   ├── settings.py
│   │   └── constants.py
│   ├── ui/                   # All visual components
│   │   ├── app.py
│   │   ├── timer_view.py
│   │   ├── settings_view.py
│   │   ├── flip_clock.py
│   │   └── theme.py
│   └── assets/
│       └── icon.ico
├── requirements.txt
├── CHANGELOG.md
├── README.md
├── LICENSE
└── .gitignore
```

See [CHANGELOG.md](CHANGELOG.md) for release history.

---

## Architecture Highlights

- **100% separation of business logic from UI** — `core/` contains zero Tkinter imports
- **Wall-clock accurate timing** — drift-free even on long sessions
- **Custom flip clock widget** — built from Tkinter Canvas primitives, no image assets
- **Defensive settings loading** — corrupt settings file? falls back to defaults, never crashes
- **All constants centralized** — no magic numbers, no hardcoded colors outside `theme.py`

---

## Known Issues (v1.0.0)

- Custom icon does not appear in taskbar/title bar while app is running (Windows caching quirk)
- Maximum practical duration is 99 minutes (display limit)
- Flip clock does not scale with window resize

All fixes planned for **v1.1**.

---

## Roadmap

**v1.1**
- Fix custom icon in taskbar/title bar
- Support durations above 99 minutes
- Custom completion sound
- Multiple theme options (light mode + more)
- Tick sound on flip animation

**v1.2**
- Responsive flip clock scaling
- System tray support
- Always-on-top toggle

---

## Built With

- **Python 3**
- **Tkinter** (standard library)
- **PyInstaller** (for the `.exe`)

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

## Author

Made by **Om Dautkhani** ([@The-Python-Dev](https://github.com/The-Python-Dev))

*Built in one 11-hour focused session.* 🔥
