import logging
from importlib.machinery import SourceFileLoader


def run_custom_before(filepath, image):
    foo = SourceFileLoader("", filepath).load_module()
    try:
        return foo.before(image)
    except AttributeError:
        logging.warning("Failed to run a `before(image)` function")
        return image

def run_custom_after(filepath, image):
    foo = SourceFileLoader("", filepath).load_module()
    try:
        return foo.after(image)
    except AttributeError:
        logging.warning("Failed to run a `after(image)` function")
        return image