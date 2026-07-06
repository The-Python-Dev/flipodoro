"""
main.py
-------
Configures logging and launches the application.
"""

import logging
import sys


def configure_logging() -> None:
    import os
    is_frozen = getattr(sys, "frozen", False)

    if is_frozen:
        app_data = os.environ.get("APPDATA") or os.path.expanduser("~/.config")
        log_dir = os.path.join(app_data, "Flipodoro")
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, "flipodoro.log")
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            handlers=[logging.FileHandler(log_path, encoding="utf-8")],
        )
    else:
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            handlers=[logging.StreamHandler(sys.stdout)],
        )


def main() -> None:
    configure_logging()
    logger = logging.getLogger(__name__)
    try:
        from src.ui.app import App
        app = App()
        app.run()
    except Exception as exc:
        logger.critical("Unhandled exception: %s", exc, exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()