from typing import Callable, Type
from noise import pnoise1
from abc import ABC, abstractmethod
from .chunk_data import Chunk
import numpy as np

class Terrain(ABC):
    ...

    def generate_terrain(self, matrix_chunks:np.ndarray):
        print(matrix_chunks.shape)
        size_x, size_y = matrix_chunks.shape
        for x in range(size_x):
            for y in range(size_y):
                for index in range(len(matrix_chunks[x, y].chunk_data)):
                    matrix_chunks[x, y].chunk_data[index] = self.get_pixel_block_id(*matrix_chunks[x, y].array_space_to_chunk_space(index))

    @abstractmethod
    def get_pixel_block_id(x, y) -> int:
        ...

class Basic(Terrain):
    amplitude:float = 5
    period:float = 5

    def get_pixel_block_id(self, chunk_x, chunk_y) -> int:
        if y + np.sin(x/self.period) * self.amplitude - 20 < 0:
            return 1
        else:
            return 0
    