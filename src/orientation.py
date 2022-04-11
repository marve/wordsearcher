"""Module that contains the orientation class"""
from enum import IntEnum

class Orientation(IntEnum):
    """Represents the possible orientations for a word in a word search"""
    UP = 1
    ACROSS = 2
    DIAG = 3
