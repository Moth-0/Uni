'''
HANDIN 10 (Random walk)

This handin is done by Mathias Lystlund, id: 202408483:

Reflection upon solution:
In my implementation of the random walk generator, I focused on using yield to produce an infinite sequence 
of positions step by step. I found it intuitive to update the current position by randomly choosing one of the 
four neighboring points, which ensured the walk followed the problem constraints. Using islice to extract a finite 
number of steps made the generator both flexible and efficient. One thing I became more aware of is how generators 
differ from regular functions, especially in how they maintain state between iterations.

'''

import random
import matplotlib.pyplot as plt
import numpy as np
from itertools import islice
def random_walk():
    start = (0, 0)
    yield start
    while True:
        
        p = random.choice([(start[0]-1, start[1]), (start[0]+1, start[1]),
                            (start[0], start[1]-1), (start[0], start[1]+1)])
        
        start = p
        yield p


points = list(islice(random_walk(), 10000))


xs = [x for x, y in points]
ys = [y for x, y in points]

xmin, xmax = min(xs), max(xs)
ymin, ymax = min(ys), max(ys)

width = xmax - xmin + 1
height = ymax - ymin + 1

grid = np.zeros((height, width))

for x, y in points:
    grid[y - ymin, x - xmin] += 1
    

plt.imshow(grid, origin='lower', extent=[xmin, xmax, ymin, ymax], cmap='hot')
plt.colorbar()
plt.show()