"""
A simple setup script to create an executable using PyQt5. This also
demonstrates the method for creating a Windows executable that does not have
an associated console.
PyQt5app.py is a very simple type of PyQt5 application
Run the build process by running the command 'python setup.py build'
If everything works well you should find a subdirectory in the build
subdirectory that contains the files needed to run the application
"""
import sys
from cx_Freeze import setup, Executable

from pathlib import Path
import os

SOURCE = "main.py"
OUTPUT = None
PYTHONPATH = sys.argv[2]

base = "Win32GUI" if sys.platform == "win32" else None

include_files = [fr"{PYTHONPATH}\Lib\site-packages\PyQt5\Qt5\plugins\platforms\qwindows.dll"]

build_exe_options = {
    "excludes": [],
    "include_files": include_files,
}

bdist_mac_options = {
    "bundle_name": "Test",
}

bdist_dmg_options = {
    "volume_label": "TEST",
}

# executables = [Executable(SOURCE, base=base, target_name=f"{OUTPUT}{'.exe' if (sys.platform == 'win32') and not OUTPUT.endswith('.exe') else ''}")]
executables = [Executable(SOURCE, base=base, target_name=OUTPUT)]

setup(
    name="simple_PyQt5",
    version="0.2",
    description="Sample cx_Freeze PyQt5 script",
    options={
        "build_exe": build_exe_options,
        "bdist_mac": bdist_mac_options,
        "bdist_dmg": bdist_dmg_options,
    },
    executables=executables,
)

NEW_PATH = OUTPUT if OUTPUT else 'main'

Path(os.path.join(os.path.abspath(__file__), f"build/exe.win-amd64-3.9/{NEW_PATH}.exe")).rename(os.path.join(os.path.abspath(__file__), NEW_PATH))