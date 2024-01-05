import pygame as pg
from .space import Space
from .world_camera import Camera

class Display:
    pixel_size:int = 4
    win_width:int = 800
    win_height:int = 600

    def __init__(self, space:Space, camera:Camera):
        self.space = space
        self.camera = camera

    def set_size(self, width, height, pixel_size):
        self.win_width = width
        self.win_height = height
        self.pixel_size = pixel_size

    def get_surface(self) -> pg.Surface:
        return pg.transform.flip(self.space.get_surf(self.camera.x, self.camera.y, self.camera.zoom), flip_x=False, flip_y=True)
