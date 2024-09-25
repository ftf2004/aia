import numpy as np
from itertools import product

def solve(grid, words):
    if not words: return True
    word = words[0]
    for r, c in product(*map(range, grid.shape)):
        for dr, dc in [(0, 1), (1, 0)]:  # Horizontal (0, 1) and vertical (1, 0)
            if all(0 <= r + i * dr < grid.shape[0] and 0 <= c + i * dc < grid.shape[1] and
                   (grid[r + i * dr, c + i * dc] == '-' or grid[r + i * dr, c + i * dc] == word[i]) 
                   for i in range(len(word))):
                for i in range(len(word)): grid[r + i * dr, c + i * dc] = word[i]
                if solve(grid, words[1:]): return True
                for i in range(len(word)): grid[r + i * dr, c + i * dc] = '-'
    return False

grid = np.array([list("+++++++++-"), list("-++++++++-"), list("-------++-"), list("-++++++++-"),
                 list("-++++++++-"), list("-++++-----"), list("------+++-"), list("-++++++++-"),
                 list("+---------"), list("++++++++++")])

words = ["CIVICS", "HISTORY", "GEOGRAPHY", "CHEMISTRY", "PHYSICS", "MATHS"]

solve(grid, words)
print('\n'.join(map(''.join, grid)))