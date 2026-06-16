# Source - https://stackoverflow.com/a/13790741
# Posted by max, modified by community. See post 'Timeline' for change history
# Retrieved 2026-06-08, License - CC BY-SA 3.0
import os 
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)