'''
HANDIN 10 (random walk)

This handin is done by (study ids and names of up to three students):

    202405584 Victor Kvist Loft Pedersen
    202405681 William Malmberg
    202404925 Josefine Ella Luci Sandy Dorothea Wendt

    Reflections upon solutions
    We first tried a version where we used random.randint and a bunch of if statements to 
    choose the direction of the walk. We then discovered random.choice which could severely reduce the
    code length and complexity.
    We also had a version where we yielded the initial position before entering the while-loop and then yielding again
    at the end of the while loop.
    We changed this to just yield at the beginning of the while loop which had the same effect as the other version but
    it was much neater to read.
'''

import random
import matplotlib.pyplot as plt
from itertools import islice

def random_walk():
    pos = (0, 0)
    while True:
        yield pos # Return position
        step = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)]) # Choose direction
        pos = (pos[0]+step[0], pos[1]+step[1]) # Walk the walk


length = 100000
gen = islice(random_walk(), length)

plt.hist2d(*zip(*gen), bins=100)
plt.colorbar()
plt.show()