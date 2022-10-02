import logging
from importlib.machinery import SourceFileLoader


def run_custom_before(data, image):
    with open("./tmp.py", "w") as f:
        f.write(data)
    try:
        foo = SourceFileLoader("", "./tmp.py").load_module()
        return foo.before(image)
    except Exception as e:
        print(e)
        logging.warning("Failed to run a `before(image)` function")
        return image

def run_custom_after(data, image):
    with open("./tmp.py", "w") as f:
        f.write(data)
    try:
        foo = SourceFileLoader("", "./tmp.py").load_module()
        return foo.after(image)
    except Exception as e:
        print(e)
        logging.warning("Failed to run a `after(image)` function")
        return image