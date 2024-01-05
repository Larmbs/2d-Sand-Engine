import numpy as np
import pygame as pg


class Chunk: #World Chunk Class
    chunk_width:int=32
    chunk_height:int=32

    def __init__(self, pos):
        self.pos = pos
        self.chunk_data = np.zeros(self.chunk_width*self.chunk_height, dtype=np.int8)
        self.surface = pg.Surface((self.chunk_height, self.chunk_width), pg.SRCALPHA)

    """Getter and Setter Helpers"""
    def get_value_x_y(self, x, y):
        index = self.chunk_space_to_array_space(x, y)
        return self.chunk_data[index]
    def set_value_x_y(self, x, y, value):
        index = self.chunk_space_to_array_space(x, y)
        self.chunk_data[index] = value

    """Converisions in chunk_space"""
    def chunk_space_to_world_space(self, x, y) -> int:
        return x + y * self.chunk_width
    def world_space_to_chunk_space(self, index) -> tuple[int, int]:
        return divmod(index, self.chunk_width)
    
    """World Space Conversion"""
    
    """2d Matrix of values"""
    def get_chunk_data(self) ->  np.ndarray:
        return self.chunk_data.reshape((self.chunk_height, self.chunk_width))
