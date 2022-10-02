import logging

from PIL import ImageFilter


class BuiltInFilter():
    def __init__(self, name, function, params):
        self.name = name
        self.function = function
        self.params = params

    def __call__(self, **kwargs):
        for key, value in self.params.items():
            if key not in kwargs.keys():
                logging.debug(f"Param {key} not in Filter's params")
            elif type(kwargs.get(key)).__name__ != value:
                logging.debug(f"Param {key}'s type should be {value}, not {type(kwargs.get(key))}")
        return self.function(**kwargs)
    
    def __repr__(self):
        return f"<FILTER: {self.name}, {self.params}>"


filters = [
    BuiltInFilter("Gaussian Blur", ImageFilter.GaussianBlur, {"radius": "int"}),
    BuiltInFilter("Median Filter", ImageFilter.MedianFilter, {"size": "int"}),
    BuiltInFilter("Min Filter", ImageFilter.MinFilter, {"size": "int"}),
    BuiltInFilter("Max Filter", ImageFilter.MaxFilter, {"size": "int"}),
    BuiltInFilter("Mode Filter", ImageFilter.ModeFilter, {"size": "int"}),
    BuiltInFilter("Unsharp Mask", ImageFilter.UnsharpMask, {"radius": "int", "percent": "int", "threshold": "int"}),
]

filters[0](radius=5)