from PIL import Image

def combine_rgb(filename_base: str, file_name, mode: str = "RGB", scale: tuple = (0.7, 0.7, 1)) -> Image:
    red = Image.open(f"{filename_base}/{file_name.replace('raw', 'red')}").point(lambda q: q*scale[0])
    green = Image.open(f"{filename_base}/{file_name.replace('raw', 'green')}").point(lambda q: q*scale[1])
    blue = Image.open(f"{filename_base}/{file_name.replace('raw', 'blue')}").point(lambda q: q*scale[2])
    return Image.merge(mode, (red, green, blue))
