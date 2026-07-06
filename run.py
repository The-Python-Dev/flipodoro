"""
run.py
------
Entry point. Run this to start Flipodoro.

Usage:
    python run.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from src.main import main

if __name__ == "__main__":
    main()