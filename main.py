

# standard libs
from threading import Thread

# 3rd-party libs

# custom libs
from src.gui.run import run_gui


if __name__ == "__main__":
    gui_thread = Thread(target=run_gui)
    gui_thread.start()

    # other processing here
    #
    #

    gui_thread.join()
