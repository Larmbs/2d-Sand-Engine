from abc import ABC
import numpy as np
from enum import Enum, auto

RGBA = np.ndarray

class Types(Enum):
    WALL=auto()
    SAND=auto()
    LIQUID=auto()

"""Materials types with stats"""
class Material(ABC):
    color:RGBA

class Air(Material):
    color:RGBA = np.array([20, 20, 20])

class Sand(Material):
    color:RGBA = np.array([227, 219, 143])

class Dirt(Material):
    color:RGBA = np.array([54, 36, 22])

class Stone(Material):
    color:RGBA = np.array([65, 65, 69])

class Water(Material):
    color:RGBA = np.array([0, 0, 255])
    mat_type:str = ""


BLOCK_LOOKUP:dict[int, Material] = {
    0:Air(),
    1:Sand(),
    2:Dirt(),
    3:Stone(),
}

"""Pixel Color Getter"""
def get_pixel_color(block_id:int) -> RGBA:
    res = BLOCK_LOOKUP.get(block_id, Air()).color
    return res

"""Pixel Physics Type Getter"""
def get_block_type(block_id:int) -> str:
    ...
    
    