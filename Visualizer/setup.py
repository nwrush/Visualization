# Nikko Rush
# 9/12/2017

# Run "python setup.py build" to create exe, can't be run from within a virtualenv

import glob
import os
import os.path
import shutil
import sys

from cx_Freeze import setup, Executable

# Create a dist version of idea_relations
if not os.path.isdir("../idea_rel_dist"):
    os.mkdir("../idea_rel_dist")

for file in glob.glob("../idea_relations/*.py") + glob.glob("../idea_relations/*.sh") + glob.glob(
        "../idea_relations/*.bat"):
    shutil.copy2(file, "../idea_rel_dist/")

base = None
if sys.platform == "win32":
    base = "Win32GUI"

additional_mods = ['numpy', 'numpy.core._methods', 'numpy.lib.format', 'scipy', 'nltk', 'scipy.interpolate', 'scipy.special']


options = {
    'build': {'build_exe': "../build"},
    'build_exe': {'includes': additional_mods,
                  'include_files': [('../idea_rel_dist', 'idea_relations'), "Vis.ico"]
                  },
}

setup(name="Visualizer",
      version="1.0",
      description="Visualizer",
      options=options,
      executables=[Executable("main.py", targetName="Visualizer", base=base, icon="Vis.ico")],
      )
