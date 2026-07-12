"""
Build script for Flipodoro EXE
Run: python build.py
"""

import subprocess
import sys
import os

print("=" * 60)
print("  Building Flipodoro.exe")
print("=" * 60)

cmd = [
    sys.executable, "-m", "PyInstaller",
    "--name=Flipodoro",
    "--onefile",
    "--windowed",
    "--clean",
    "--noconfirm",

    # Bundle assets INTO the EXE
    "--add-data=src/assets;assets",

    # Hidden imports
    "--hidden-import=src",
    "--hidden-import=src.core",
    "--hidden-import=src.core.constants",
    "--hidden-import=src.core.settings",
    "--hidden-import=src.core.timer",
    "--hidden-import=src.ui",
    "--hidden-import=src.ui.app",
    "--hidden-import=src.ui.flip_clock",
    "--hidden-import=src.ui.settings_view",
    "--hidden-import=src.ui.theme",
    "--hidden-import=src.ui.timer_view",
]

# Add icon
icon_path = os.path.join("src", "assets", "icon.ico")
if os.path.exists(icon_path):
    cmd.append(f"--icon={icon_path}")
    print(f"Using icon: {icon_path}")

cmd.append("src/main.py")

print("\nBuilding... this will take 2-3 minutes\n")

result = subprocess.run(cmd)

if result.returncode == 0:
    exe_path = os.path.join("dist", "Flipodoro.exe")
    if os.path.exists(exe_path):
        size_mb = os.path.getsize(exe_path) / (1024 * 1024)
        print("\n" + "=" * 60)
        print("  SUCCESS!")
        print(f"  Your EXE is at: {os.path.abspath(exe_path)}")
        print(f"  Size: {size_mb:.1f} MB")
        print("=" * 60)
else:
    print("\n  BUILD FAILED")