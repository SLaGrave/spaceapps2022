from PIL import Image

def combine_rgb(filename_base: str, mode: str = "RGB", scale: tuple = (1, 1 ,1)) -> Image:
    red = Image.open(f"{filename_base}-red.png").point(lambda q: q*scale[0])
    green = Image.open(f"{filename_base}-green.png").point(lambda q: q*scale[1])
    blue = Image.open(f"{filename_base}-blue.png").point(lambda q: q*scale[2])
    return Image.merge(mode, (red, green, blue))
