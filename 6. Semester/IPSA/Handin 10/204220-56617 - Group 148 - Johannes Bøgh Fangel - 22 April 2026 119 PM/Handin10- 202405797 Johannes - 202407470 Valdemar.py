#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HANDIN 10 (Random Walk)

This handin is done by:

    202405797 Johannes Bøgh Fangel
    202407470 Valdemar Scheel

Reflection upon solution:
    Hard Parts: Choosing how we should determine the walk: which way to go, was 
    hard. We ended up creating a list with the next positions you could go to 
    from the current position, and then draw a random index of this list using 
    the random module from the numpy-package. We also started by making the 
    position a list with the x- and y-values. This ended up being a problem as 
    lists are mutable, we therefore, when wanting to get our steps, got a list 
    where all the steps were at the same position. To counter this we used 
    tuples for the position instead, as tuples are immutable.
"""

from numpy import random
import matplotlib.pyplot as plt
from itertools import islice

# a) 
def random_walk():  
    position = (0, 0)
    
    while True:
        yield position
        choices = [(position[0] - 1, position[1]), 
                   (position[0], position[1] + 1),
                   (position[0] + 1, position[1]),
                   (position[0], position[1] - 1)
                   ]
        position = choices[random.randint(0, 4)]
        
walk_seq = list(islice(random_walk(), 1000))

# b)
fig, ax = plt.subplots()
im = ax.hist2d([pos[0] for pos in walk_seq], [pos[1] for pos in walk_seq], 39, 
               range=[[-20, 20],[-20, 20]], cmap='gray')
fig.colorbar(im[3], ax=ax)
ax.set_aspect('equal')

# Alternative Solution:
# Part a -----------------------
import random
import matplotlib.pyplot as plt
from itertools import islice

def random_walk():

    position = (0,0)

    while True:

        yield position

        direction = random.randint(0,3)
            
        if direction == 0:
            # Up
            position = (position[0],position[1] + 1)
        elif direction == 1:
            # Down
            position = (position[0],position[1] - 1)
        elif direction == 2:
            # Left
            position = (position[0]-1,position[1])
        elif direction == 3:
            # Right
            position = (position[0]+1,position[1])


# Part b -----------------------
walk = list(islice(random_walk(),10000))

im = plt.hist2d([walk1[0] for walk1 in walk],[walk2[1] for walk2 in walk],bins=40,range=[[-20,20],[-20,20]],cmap="gray")
plt.colorbar(im[3])
plt.show()


