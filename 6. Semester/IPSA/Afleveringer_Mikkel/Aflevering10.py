"""
HANDIN 10 - Random Walk

This handin is done by: 
    202307989 Mikkel Moth Billing 

Reflection upon solution: 
    I Think i did fine this exercise, i don't know if using random.choice() was the intended way, but it works :)
    I'm not sure why we want it to be an infinite generator, when we want a non infinite number of steps. 
    It could just be a function with number of steps as argument, it would skip the islice line. 
"""
from random import choice
import matplotlib.pyplot as plt
from itertools import islice

def random_walk(): 
    pos = (0,0)
    yield pos
    while True:
        dx, dy = choice([(1,0), (-1,0), (0, 1), (0,-1)])
        pos = (pos[0] + dx, pos[1] + dy)
        yield pos

infinite_walk = random_walk()

length = 1000
walk = list(islice(infinite_walk, 0, length))

x = [step[0] for step in walk]
y = [step[1] for step in walk]

plt.hist2d(x, y, bins=[max(x)- min(x), max(y)-min(y)], cmap="hot")
plt.colorbar()
plt.title(f"Random Walk of length {length}")
plt.show()