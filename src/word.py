"""This module houses the Word class"""
from dataclasses import dataclass
from orientation import Orientation

@dataclass
class Word:
    """Represents a word in a crossword puzzle"""
    text: str
    orientation: Orientation = Orientation.ACROSS
    reverse: bool = False

    @property
    def length(self):
        """Number of characters in the word"""
        return len(self.text)

    @property
    def width(self):
        """Horizontal size of the word"""
        return self.length if not self.orientation == Orientation.UP else 1

    @property
    def height(self):
        """Vertical size of the word"""
        return self.length if not self.orientation == Orientation.ACROSS else 1

    @property
    def rendered(self):
        """Word in direction order (i.e., reversed if so configured)"""
        return self.text[::-1 if self.reverse else 1]

    def __str__(self):
        return f'text={self.text} orientation={self.orientation} reverse={self.reverse}' 
