from local.keyutils.typing import Number, Iterable # PROBLEM
from kgui.object import UIObject

from pygame import Surface, surfarray, SRCALPHA
from numpy import array, ndarray, insert, ones, uint8
import PIL.Image

def rgba2surface(rgb: ndarray, alpha: None|ndarray|Number = None) -> Surface:
    surf = surfarray.make_surface(rgb).convert_alpha()
    if alpha is None: return surf
    a = surfarray.pixels_alpha(surf)
    match alpha:
        case ndarray(shape=(w,h)): transparency = alpha 
        case alpha if type(alpha) in Number.types: transparency = ones(rgb.shape[:2], dtype=uint8) * uint8(alpha)
        case _: raise ValueError(f"This aint right! -> type(alpha)={type(alpha)}")
    a = transparency 
    del a
    return surf

class Color:
    def __init__(self, *args):
        match args:
            case ("clear",): return 0,0,0,0
            case (str(x),): pass 
            case (int(r), int(g), int(b)): return r,g,b,256

class Image(UIObject):
    def __init__(self, loader):
        match loader:
            case str(x) if x.endswith((".jpg", ".png")): 
                raw = array(PIL.Image.open(x))
                self.size = raw.shape[:2]
                self.width, self.height, channels = raw.shape
                self.rgb = raw[:, :, :3]
                self.a = raw[:, :, 3] if channels==4 else None
                self.surface = rgba2surface(self.rgb, alpha=self.a)
            case Surface(): 
                self.surface = loader 
            case ndarray(shape=(w, h, channels)):
                self.width, self.height = self.size = w, h
                self.rgb = loader[:, :, :3]
                self.a = loader[:, :, 3] if channels==4 else None 
                self.surface = rgba2surface(self.rgb, alpha=self.a)
            case ndarray(shape=(w, h)):
                self.width, self.height = self.size = w, h 
                self.rgb = loader # make it loader but 3 times for the rgb 
                self.a = None 
                self.surface = rgba2surface(self.rgb, alpha=None)
