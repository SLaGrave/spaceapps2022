from PIL import Image, ImageFilter

def apply_gaussian_blur(img: Image, radius=2) -> Image:
    """
    Parameters
    ----------
    img: `Image` for blur to be applied to
    radius: `int` for the radius of the blur

    Returns
    -------
    `Image` with applied blur
    """
    return img.filter(ImageFilter.GaussianBlur(radius))