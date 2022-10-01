import logging
logging.getLogger().setLevel(logging.DEBUG)

from src import *

from pyray import *

request_juno_cam_img("https://www.missionjuno.swri.edu/junocam/processing?id=13926")

init_window(800, 450, "Hello")
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    draw_text("Hello world", 190, 200, 20, VIOLET)
    end_drawing()
close_window()