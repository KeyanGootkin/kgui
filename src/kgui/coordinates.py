from kbasic.vectors import Vector 

class PixelPosition(Vector):
    def __init__(self, x=0, y=0) -> None:
        #organize args 
        xi = x if type(x)!=tuple else x[0]
        yi = y if type(x)!=tuple else x[1]
        Vector.__init__(self, xi, yi)
        self.x = xi
        self.y = yi
    def __repr__(self) -> str: return f"x = {self.x}; y = {self.y}"
    def __getattribute__(self, name):
        value = Vector.__getattribute__(self, name)
        match name:
            #can assign subpixel values to x or y but only ever get integers out of it
            case 'x'|'y': return int(value//1)
            case 'components': return self.x, self.y
            case _: return value
    def __tuple__(self) -> tuple: return self.x, self.y
