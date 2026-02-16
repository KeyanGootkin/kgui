from kgui.object import UIObject

from pygame import KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION, MOUSEWHEEL

class Button(UIObject):
    def __init__(self, left_click_function, right_click_function=None, down_function=None, hover_function=None):
        self.on_left_click = left_click_function
    def update(self, dt, event_list):
        for event in event_list:
            match event:
                case MOUSEBUTTONDOWN(pos=(x, y)): self.on_down()
                case MOUSEBUTTONUP(pos=(x, y)) if self.collides(x, y): self.on_left_click()
                case _: pass
    def on_hover(self): pass
    def on_down(self): pass
    def on_right_click(self): pass