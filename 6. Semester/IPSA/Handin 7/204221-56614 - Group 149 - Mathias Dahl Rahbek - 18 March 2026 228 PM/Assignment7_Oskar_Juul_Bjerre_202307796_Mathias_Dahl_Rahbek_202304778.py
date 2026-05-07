"""
HANDIN 7 (convex hull)

202307796 Oskar Juul Bjerre
202304778 Mathias Dahl Rahbek

Reflection upon solution:
We implemented an assert statement in the random_points function to check that
the user inputs a valid n. Then we made the choice to artificially insert the
starting point again in the plot function, so that the convex_hul don't return
the same point twice. To test the convex_hull function using doctest we added
some tests in the docstring of the function. We would have liked to do tests in
a different way. Namely importing the Convexhull function from scipy.spatial
and checking that our function returns the same set of points. But we did not
know how to implement the doctest module using this method.
"""

import matplotlib.pyplot as plt

import random

def random_points(n):
    assert isinstance(n, int) and 1 <= n <= 100, f'{n = } must be between 1 and 100 and an interger.'
    points = []
    for _ in range(n):

        point = (round(random.random(), 5), 
                 round(random.random(), 5)) # We round to 5 decimals
        points.append(point)
    return points

def plot_hull(points, polygon):
    for x, y in points:
        plt.plot(x, y, 'go')

    polygon_xs = [x for x, y in polygon]
    polygon_ys = [y for x, y in polygon]

    polygon_xs.append(polygon_xs[0])
    polygon_ys.append(polygon_ys[0])

    plt.plot(polygon_xs, polygon_ys, 'r-')
    plt.plot(polygon_xs, polygon_ys, 'r.')
    plt.show()

def left_turn(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]) >= 0


def convex_hull(points):
    '''Function to find the convex hull of a list of points [(x,y), (v, w), ...]
    
    Examples:
    >>> len(convex_hull([(3,2), (1,1), (2,3), (2,2), (1.5, 2.25), (2.5, 2.25), (2, 1.25), (1, 1.5)]))
    5
    >>> convex_hull([(1, 1), (2, 2)])
    [(1, 1), (2, 2)]
    >>> convex_hull([(3,2), (1,1), (2,3), (2,2), (1.5, 2.25), (2.5, 2.25), (2, 1.25), (1, 1.5)])
    [(1, 1), (1, 1.5), (2, 3), (3, 2), (2, 1.25)]
    '''
    points = sorted(points)
    if len(points) <= 2: # Check that we have more than two points
        return points
    
    upper = []
    for p in points:
        while len(upper) >= 2 and left_turn(upper[-2], upper[-1], p):
            upper.pop()
        upper.append(p)
    
    lower = []
    for p in reversed(points):
        while len(lower) >= 2 and left_turn(lower[-2], lower[-1], p):
            lower.pop()
        lower.append(p)
    
    return upper[:-1] + lower[:-1]

import doctest
doctest.testmod(verbose = True)
