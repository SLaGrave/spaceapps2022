from pyray import *


MAIN_COLOR = ORANGE
BG_COLOR = DARKGRAY
TEXT_COLOR = SKYBLUE


def loop():
    """Loop indefinitely, drawing UI elements."""
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    msg = load_file_text("assets/greeting.txt")


    rect_top =  Rectangle(5, 5, SCREEN_WIDTH- 10, SCREEN_HEIGHT//2 - 10)
    rect_bot1 = Rectangle(5, SCREEN_HEIGHT//2 + 5, SCREEN_WIDTH//2- 10, SCREEN_HEIGHT//2 - 50)
    rect_bot2 = Rectangle(SCREEN_WIDTH//2 + 5,  SCREEN_HEIGHT//2 + 5, SCREEN_WIDTH//2- 10, SCREEN_HEIGHT//2 - 50)

    rect_img = Rectangle(0, 0, rect_top.width//2 - 50, rect_top.height - 60)
    vec_img1  = Vector2(rect_top.x + 30, rect_top.y + 30)
    vec_img2  = Vector2((rect_top.x + rect_top.width)//2 + 30, rect_top.y + 30)

    rect_txt  = Rectangle(30, SCREEN_HEIGHT - 120, SCREEN_WIDTH//2- 60, 50) # command input text box


    # extract images from assets folder
    rick1 = load_image("assets/rick2.png")
    rick2 = load_image("assets/rick1.png")

    # copy the ricks, resize them, and pass them to the texture handler
    img1 = image_copy(rick1)
    img2 = image_copy(rick2)
    image_resize(img1, int(rect_img.width), int(rect_img.height))
    image_resize(img2, int(rect_img.width), int(rect_img.height))
    texture1 = load_texture_from_image(img1)
    texture2 = load_texture_from_image(img2)


    while not window_should_close():
        
        # If the user resizes the screen, resize the UI elements to match
        if(get_screen_height() != SCREEN_HEIGHT or get_screen_width() != SCREEN_WIDTH):
            SCREEN_HEIGHT = get_screen_height()
            SCREEN_WIDTH = get_screen_width()

            # re-draw rectangles in new screen
            rect_top =  Rectangle(5, 5, SCREEN_WIDTH- 10, SCREEN_HEIGHT//2 - 10)
            rect_bot1 = Rectangle(5, SCREEN_HEIGHT//2 + 5, SCREEN_WIDTH//2- 10, SCREEN_HEIGHT//2 - 50)
            rect_bot2 = Rectangle(SCREEN_WIDTH//2 + 5,  SCREEN_HEIGHT//2 + 5, SCREEN_WIDTH//2- 10, SCREEN_HEIGHT//2 - 50)
            rect_txt  = Rectangle(30, SCREEN_HEIGHT - 120, SCREEN_WIDTH//2- 60, 50) # command input text box

            rect_img = Rectangle(0, 0, rect_top.width//2 - 50, rect_top.height - 60)
            vec_img1  = Vector2(rect_top.x + 30, rect_top.y + 30)
            vec_img2  = Vector2((rect_top.x + rect_top.width)//2 + 30, rect_top.y + 30)

            # copy the ricks, resize them, and pass them to the texture handler
            img1 = image_copy(rick1)
            img2 = image_copy(rick2)
            image_resize(img1, int(rect_img.width), int(rect_img.height))
            image_resize(img2, int(rect_img.width), int(rect_img.height))
            texture1 = load_texture_from_image(img1)
            texture2 = load_texture_from_image(img2)


        begin_drawing()

        # ======== SET UP BACKGROUND UI =======
        clear_background(BG_COLOR)
        draw_rectangle_lines_ex(rect_top, 10, MAIN_COLOR)
        draw_rectangle_lines_ex(rect_bot1, 10, MAIN_COLOR)
        draw_rectangle_lines_ex(rect_bot2, 10, MAIN_COLOR)

        draw_texture_rec(texture1, rect_img, vec_img1, WHITE)
        draw_texture_rec(texture2, rect_img, vec_img2, WHITE)


        # ======== DRAW SAMPLE IMAGES =======



        # ======== SET UP TEXT INPUT =======

        draw_rectangle_lines_ex(rect_txt, 10, TEXT_COLOR)


        draw_text(msg, (SCREEN_WIDTH//2) - 5*len(msg), SCREEN_HEIGHT - 30, 20, TEXT_COLOR)

        end_drawing()