from kgui.coordinates import PixelPosition
class UIObject:
    surface = None 
    position = PixelPosition(0, 0)
    update = lambda self, dt, event_list: None
    collides = lambda self, x, y: False

    def __getstate__(self):
       """Used for serializing instances"""
       
       # start with a copy so we don't accidentally modify the object state
       # or cause other conflicts
       state = self.__dict__.copy()

       # remove unpicklable entries
    #    del state['f']
       return state

    def __setstate__(self, state):
        """Used for deserializing"""
        # restore the state which was picklable
        self.__dict__.update(state)
        
        # restore unpicklable entries
        # f = open(self.filename)
        # self.f = f