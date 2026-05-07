'''
HANDIN 10 (Random Walks)

202307796 Oskar Juul Bjerre
202304778 Mathias Dahl Rahbek

Reflection upon solution:
The idea of this solution was first to define the starting point (0,0). 
From there, we want to make the function infinte with the "while True"
statement. Then, picking at random the 4 possible choices for the possible 
set of points, i.e up/down in x and up/down in y. Then, updating these
indicies, and saving the previous point. Then, defining the iterator such that
we can call "next" on it 1000 times, since otherwise it would print a bunch of
(0,0). Lastly, we used hist2d to plot these points, since this is what we are
more familiar with. You could probably optimize the generating data part. 
'''
#a)
import random
# Define starting condition, so point (0,0)
def random_walk(start_x=0,start_y=0):

    x,y = start_x,start_y

    yield (x,y)

    # Make function infinite 
    while True: 

        # Define all possible scenarios 
        idx_x, idx_y = random.choice([(0,1),(0,-1),(1,0),(-1,0)])

        # Update variables
        x += idx_x
        y += idx_y 

        # return variables 
        yield (x,y)

# Define iterator
it = random_walk()

#b)
import matplotlib.pyplot as plt
 
# Make data 
n=1000

xs,ys = [],[]
for _ in range(n):
    x,y=next(it)

    xs.append(x)
    ys.append(y)

# Plot data
plt.hist2d(xs,ys)
plt.colorbar()
plt.show()

