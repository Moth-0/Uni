"""
HANDIN 10

This handin is done by:

202407098 Johanne Stubkjær
202408622 Magnus Overgaard
202405571 Jonas Ullgren

Reflection upon solution:

We discussed how best to solve the exercise and first wanted to to make a function. First we thought that with each iteration we would
make a list containing the actual 4 "direction"-points around the point we were at and then pick one of those points, but this seemed very 
annoying. We then realized it was unnecessary because we could just choose a direction and go 1 step-length in that direction. Then we used 
yield and turned it into an actual generator.
Then we made a way to create the path when the generator was used, and also had to split the points up in x- and y-coordinates so they could
be plotted, which we did using hist2d as one of the suggestions in the exercise.
"""


import matplotlib.pyplot as plt
import random


steplength = 1000 # Number of points in the random walk

# Generator function which creates a point based on the previous one
def random_walk():
    x, y = 0, 0 
    yield x, y  # First point (0, 0) must be included according to the exercise

    # Generates new points forever
    while True: 
        # Randomly pick one of the possible directions
        direction = random.choice(['left', 'right', 'up', 'down'])

        # Move one step in the above chosen direction
        if direction == 'right':
            x += 1
        elif direction == 'left':
            x -= 1
        elif direction == 'up':
            y += 1
        elif direction == 'down':
            y -= 1
            
        yield x, y # Returns the new point


# Uses the generator function with the amount of points specified in 
# the start to create a path of length steplength.
walker = random_walk()
path = []
for _ in range(steplength):
    path.append(next(walker))


# Splits the points into x- and y-coordinates in lists to use for plotting
xs = [p[0] for p in path]
ys = [p[1] for p in path]


# Finds the largest distance from 0 in either x- or y-direction, which is 
# used to make the plot range include the whole walk on the actual plot.
combined = xs + ys
biggest_value = max(abs(value) for value in combined)


# Plots how often each grid point was "walked" on in the random walk
plt.hist2d(xs, ys, 
    cmap = 'gray', 
    bins = biggest_value * 2 + 1,  # Makes roughly one bin per interger coordinate
    range = [[-biggest_value, biggest_value], [-biggest_value, biggest_value]])
plt.colorbar() 
plt.show()
