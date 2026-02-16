import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from pygame.font import SysFont, init
init()
from kgui.object import UIObject
from kgui.coordinates import PixelPosition


class Font:
    def __init__(self, name, size=12, color='white', AA=True) -> None:
        self.pgFont = SysFont(name, size=size)
        self.color: str = color 
        self.AA: bool = AA
    def __setattr__(self, attr, value):
        self.__dict__[attr] = value
        match attr:
            case "name"|"size": 
                self.pgFont = SysFont(self.name, self.size)
    def __call__(self, text: str):
        return self.pgFont.render(text, self.AA, self.color)
    def __repr__(self) -> str: return self.name
    def __getstate__(self) -> None: return self.__dict__.copy()
    def __setstate__(self, state): self.__dict__.update(state)

DefaultFont = Font('victormono')

class Text(UIObject):
    def __init__(self, text, position, font:Font=DefaultFont) -> None:
        self.string = str(text)
        self.position = PixelPosition(position)
        self.font = font
        self.surface = font(self.string)
        self.width, self.height = self.size = self.surface.get_size()
    def __repr__(self) -> str: return "Text: "+self.string
    def append(self, other: str):
        self.string += other
        self.surface = self.font(self.string)


        