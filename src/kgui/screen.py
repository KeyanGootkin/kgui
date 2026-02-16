from kgui.visuals import Image

from pygame import Color, Surface, QUIT, quit

class Window(Surface):
    def __init__(self, x): 
        Surface.__init__(self, x.get_size())
    def __getstate__(self) -> None: return self.__dict__.copy()
    def __setstate__(self, state): self.__dict__.update(state)

class Screen(Surface):
    """
    Screens cover the entire game window, kinda like a 'level' conceptually
    """
    def __init__(self, window, background="#002D23") -> None:
        self.width, self.height = self.size = window.get_size()
        self.window = Window(window)
        Surface.__init__(self, self.size)
        self.background = background 
        self.construct_background()
        self.children = [] # every child needs an update method, a surface, and a position

    def construct_background(self) -> None:
        match self.background:
            case str(x) if x.startswith("#"): self.fill(Color(self.background))
            case str(x) if x.endswith((".jpg",".png")): self.blit(Image(self.background).surface, (0,0))
            case tuple(): self.fill(self.background)

    def update(self, dt: float, event_list: list, mul=10) -> None:
        for event in event_list:
            if event.type==QUIT: quit()
        # update components
        self.construct_background()
        for child in self.children: 
            child.update(dt, event_list)
        # draw components
        for child in self.children:
            self.blit(child.surface, (child.position.x, child.position.y))
