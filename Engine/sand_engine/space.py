import numpy as np
from .chunk_data import Chunk
from .procedual import Basic
import pygame as pg
from .material import get_pixel_color
from numba import jit
from typing import Protocol

class World(Protocol):
    def get_surface():
        ...


class Space:
    chunk_size:int=16
    vert_chunks:int=2
    horizontal_chunks:int=2

    def __init__(self, horizontal_chunks, vert_chunks):
        self.horizontal_chunks = horizontal_chunks
        self.vert_chunks = vert_chunks

        self.world_data = np.zeros((horizontal_chunks, vert_chunks), dtype=Chunk)
        self.init_chunks()
        transform = Basic()
        transform.generate_terrain(self.world_data)

    def init_chunks(self):
        for x in range(self.horizontal_chunks):
            for y in range(self.vert_chunks):
                self.world_data[x, y] = Chunk((x, y))

    def get_surf(self, camera_x, camera_y, zoom):
        chunk_data = self.combine_chunks(camera_x, camera_y, 2, 2)
        map_data = map_colors_to_id(chunk_data)
        surface = pg.Surface((map_data.shape[0], map_data.shape[1]))
        pg.surfarray.blit_array(surface, map_data)
        return scale_relative(surface, zoom)
    
    def combine_chunks(self, x_off, y_off, width, height):
        min_x = x_off
        min_y = y_off
        max_x = x_off + width
        max_y = y_off + height

        chunks = []
        for y in range(min_x, max_x):
            vertical_slice = []
            for x in range(min_y, max_y):
                vertical_slice.append(self.world_data[y, x].get_chunk_data())
            chunks.append(np.vstack(vertical_slice))

        return np.hstack(chunks)
      
    
def scale_relative(surface:pg.Surface, scalar:float):

    original_size = surface.get_size()
    new_size = (int(original_size[0] * scalar), int(original_size[1] * scalar))
    return pg.transform.scale(surface, new_size)

def map_colors_to_id(original_array) -> np.ndarray:
    vectorized_determine_rgb_tuple = np.vectorize(get_pixel_color, otypes=[object])
    new_arrray = vectorized_determine_rgb_tuple(original_array)
    return np.array(new_arrray.tolist(), dtype=np.uint8)
