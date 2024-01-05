from typing import Protocol
from dataclasses import dataclass

@dataclass
class World_Object:
    x:float=0
    y:float=0

class Camera:
    zoom_in_sens:float = 1.1
    zoom_out_sens:float = 0.9

    def __init__(self, obj:World_Object=None, zoom:float=1):
        self.obj = obj if obj is not None else World_Object()
        self.zoom = zoom
    
    """Zoom Funcs"""
    def zoom_in(self):
        self.zoom *= self.zoom_in_sens
    def zoom_out(self):
        self.zoom *= self.zoom_out_sens

    @property
    def x(self):
        return self.obj.x
    @property
    def y(self):
        return self.obj.y