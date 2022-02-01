from ast import Or
from grid import Grid
from orientation import Orientation
from word import Word

words = [
    Word("fancy", Orientation.ACROSS),
    Word("solidary", Orientation.UP, True),
    Word("blinker", Orientation.DIAG),
    Word("missippi", Orientation.DIAG),
    Word("onomatopoeia", Orientation.ACROSS, False),
    Word("economical", Orientation.UP),
    Word("blighted", Orientation.ACROSS, False),
    Word("egotistical", Orientation.UP, True),
    Word("distopian", Orientation.ACROSS),
    Word("elliptical", Orientation.DIAG, True)
]

grid = Grid()
for word in words:
    grid.add(word)
grid.fill()
print(grid)