import sys, os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {
    "packages": ["pygame", "pygame_menu"], 
    "excludes": [], 
    "include_files": ["assets/"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

sha = os.getenv('DRONE_COMMIT_SHA')
build = os.getenv('DRONE_BUILD_NUMBER')
if sha == "" or sha is None or build == "" or build is None:
    version = "0.0"
else:
    version = "0." + build + "(" + sha + ")"

setup(
    name="Éscape",
    version=version,
    description="A game from the game jam \"Game Off 2022\"!",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)