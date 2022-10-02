def before(image):
    # Code to be run before filters goes here
    print(" Before")
    return image

def after(image):
    return image.rotate(45)
