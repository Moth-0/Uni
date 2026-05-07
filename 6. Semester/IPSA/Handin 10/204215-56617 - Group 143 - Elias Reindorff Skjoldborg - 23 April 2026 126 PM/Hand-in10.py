import random as rd
import numpy as np
import matplotlib.pyplot as plt

'''
HANDIN 10 (random walk)

This handin is done by:

    202106248 Matilde E. Hansen
    202105331 Elias R. Skjoldborg

Reflection upon solution:
There were no major problems in the solving of this handin. We solved the problem by defining the possible steps, and then making a generator class that updates
the current position by randomely taking one of the pre-defined steps.

We use hist2d to visualize the random walk, since we from previous experience have found that this is one of the easier ways to make a heat-map.
'''

steps = [(1,0),(-1,0),(0,1),(0,-1)]     # We define all possible steps our random walker can take.

class random_walk ():                   # We make our random walker class

    def __init__(self,n):               # When initializing the class we set how many steps to take and define the first coordinate to be 0,0
        self.n = n
        self.x = 0
        self.y = 0

    def __iter__(self):                 # We take our random steps by making an iterator
        yield (self.x,self.y)           # The first thing to return is the start point
        N = self.n
        while N > 0:                    # We use N to make sure the loop terminates after we have taken all the needed steps
            N-=1
            step = rd.choice(steps)     # We choose a random element from the possible steps that can be taken
            self.x += step[0]           # We update our current position with the new step
            self.y += step[1]
            yield (self.x, self.y)      # We return the new position

Mikkel = random_walk(1000)              # We define our random walker
Mikkeliter = iter(Mikkel)
ha = [x for x in Mikkeliter]            # We generate a list of all the coordinates visited by our random walker
print(ha)

X = [i[0] for i in ha]
Y = [i[1] for i in ha]


plt.hist2d(X,Y, bins=[np.arange(min(X)-1,max(X)+1,1),np.arange(min(Y)-1,max(Y)+1,1)]) # We make a heat map of all coordinates visited by our random walker
plt.show()
