import tkinter as tk
import logging
import sys
import os
from src.core.timer import PomodoroTimer
from src.core.settings import Settings
from src.core.constants import (
    APP_NAME,
    APP_VERSION,
    WINDOW_DEFAULT_WIDTH,
    WINDOW_DEFAULT_HEIGHT,
    WINDOW_MIN_WIDTH,
    WINDOW_MIN_HEIGHT,
)
from src.ui.theme import PALETTE
from src.ui.timer_view import TimerView
from src.ui.settings_view import SettingsView

logger = logging.getLogger(__name__)


class App:

    def __init__(self):
        self._settings = Settings()
        self._timer = PomodoroTimer(
            study_minutes=self._settings.study_minutes,
            short_break_minutes=self._settings.short_break_minutes,
            long_break_minutes=self._settings.long_break_minutes,
            sessions_before_long_break=self._settings.sessions_before_long_break,
        )
        self._root = self._create_root_window()
        self._timer_view = self._create_timer_view()
        self._timer_view.pack(fill=tk.BOTH, expand=True)
        self._root.protocol("WM_DELETE_WINDOW", self._on_close)
        self._bind_shortcuts()
        logger.info("%s v%s started.", APP_NAME, APP_VERSION)

    def run(self):
        self._root.mainloop()

    def _create_root_window(self):
        root = tk.Tk()
        root.title(APP_NAME)
        root.configure(bg=PALETTE.bg_primary)
        root.geometry(f"{WINDOW_DEFAULT_WIDTH}x{WINDOW_DEFAULT_HEIGHT}")
        root.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        root.resizable(True, True)

        try:
            if getattr(sys, "frozen", False):
                base = sys._MEIPASS
            else:
                base = os.path.join(os.path.dirname(__file__), "..", "assets")
            icon_path = os.path.join(base, "icon.ico")
            if os.path.exists(icon_path):
                root.iconbitmap(icon_path)
        except Exception:
            pass

        return root

    def _create_timer_view(self):
        return TimerView(
            parent=self._root,
            timer=self._timer,
            settings=self._settings,
            on_open_settings=self._open_settings,
        )

    def _open_settings(self):
        SettingsView(
            parent=self._root,
            settings=self._settings,
            on_save=self._on_settings_saved,
        )

    def _on_settings_saved(self):
        self._timer_view.on_settings_applied()

    def _on_close(self):
        self._timer_view.stop_tick_loop()
        self._settings.save()
        self._root.destroy()

    def _bind_shortcuts(self):
        self._root.bind("<space>", lambda e: self._timer_view._on_start_pause())
        self._root.bind("<r>", lambda e: self._timer_view._on_reset())
        self._root.bind("<R>", lambda e: self._timer_view._on_reset())
        self._root.bind("<s>", lambda e: self._timer_view._on_skip())
        self._root.bind("<S>", lambda e: self._timer_view._on_skip())
        self._root.bind("<f>", lambda e: self._timer_view._toggle_focus_mode())
        self._root.bind("<F>", lambda e: self._timer_view._toggle_focus_mode())
        self._root.bind("<Control-comma>", lambda e: self._open_settings())