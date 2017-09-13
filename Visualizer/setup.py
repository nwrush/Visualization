# Nikko Rush
# 9/12/2017

# Run "python setup.py build" to create exe, can't be run from within a virtualenv

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

additional_mods = ['numpy.core._methods', 'numpy.lib.format']

options = {
    'build_exe': {'includes': additional_mods}
}

setup(name="Visualizer",
      version="0.1",
      description="Visualizer",
      options=options,
      executables=[Executable("main.py", base=base)])
