from pyray import *

from .loop import loop

def run_gui():
    """Initialize the GUI and start the loop."""
    set_config_flags(FLAG_WINDOW_RESIZABLE)
    init_window(1920, 1080, "Hello")
    loop()
    close_window()