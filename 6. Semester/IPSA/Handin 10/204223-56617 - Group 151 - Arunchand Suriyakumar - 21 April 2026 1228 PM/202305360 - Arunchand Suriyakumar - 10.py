#%%
#Exercise 20.9 - handin 10 (random walk)


'''
HANDIN 10 (Handin 10 -  random walk)

This handin is done by 
    202305360: Arunchand Suriyakumar

Reflection upon solution:
    The random walk function is made by taking two
    random integers, one chosing if moving in positive or negative
    direction and the other chosing which coordinate. 

    The plot is made using hist2d and by approiate use of
    slicing, zipping and *, the random walk is plotted. 
 
'''

#%%
from random import randint
import matplotlib.pyplot as plt
from itertools import islice

def random_walk():
    current_point = (0,0)
    yield current_point
    while True:
        distance = randint(0, 1)
        if distance == 0:
            distance = -1
        direction = randint(0, 1)

        current_point = list(current_point)
        current_point[direction] += distance

        yield tuple(current_point)


# %%
cells = islice(random_walk(), 1000)
plt.hist2d(*zip(*cells))
plt.colorbar()

