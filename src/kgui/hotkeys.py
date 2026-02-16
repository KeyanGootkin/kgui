
class Hotkeys:
    def __init__(self, bindings: dict):
        self.bindings = bindings
    def __len__(self) -> int: return len(self.bindings.keys())
    def __getitem__(self, key):
        return self.bindings[key]
    def __call__(self, key): self.__getitem__(key)
    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        if self.index < len(self):
            i = self.index
            self.index += 1
            return self.keys[i]
        else: raise StopIteration
    
    @property
    def keys(self): return list(self.bindings.keys())