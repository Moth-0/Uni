"""
HANDIN 7 - convex hull

This handin is done by: 
    202307989 Mikkel Moth Billing 

Reflection upon solution: 
    Overall the assignment went well, i used a lot of time finding out, how to compute the convex hull. 
    I feel like my tests are good, i feel like it is unnecessary to check the output, when they are all lists. 
"""
from random import random
import matplotlib.pyplot as plt

def left_turn(p, q, r):
    '''
    Find if point r is to the left of the line between p and q
    '''
    return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]) >= 0

def random_points(n): 
    ''' 
    Returns a list of n random points with x- and y- coordinates in [0,1)
    takes inter 1 ≤ n ≤ 100
    '''

    assert isinstance(n, int)
    assert n >= 1
    assert n <= 100

    return [(random(), random()) for _ in range(n)]

def plot_hull(points, polygon): 
    ''' 
    Takes two lists of tuple-points. 
    Plots the given points of the first list and the polygon of points from the second.
    '''
    # Check if both lists are filled with tuple-points
    assert isinstance(points, list)
    assert isinstance(polygon, list)
    assert all(isinstance(p, tuple) and all(isinstance(coord, (int, float)) 
                                            for coord in p) for p in points)
    assert all(isinstance(p, tuple) and all(isinstance(coord, (int, float)) 
                                            for coord in p) for p in polygon)
    
    x, y = zip(*points)
    px, py = zip(*polygon)
    plt.plot(x, y, "o") # All points
    plt.plot(px + (px[0],), py + (py[0],), "k-") # adds first point again to complete ploygon
    plt.plot(px + (px[0],), py + (py[0],), "r.") # Red point in hull
    plt.show()

def convex_hull(points): 
    ''' 
    Finds the points for the convex hull
    Takes a list of tuple-points and returns list of tuple-points
    '''
    # Check for types
    assert isinstance(points, list)
    assert all(isinstance(p, tuple) and all(isinstance(coord, (int, float)) 
                                            for coord in p) for p in points)
    
    points = sorted(points) # Sort list of points with lowest x, if same x then lowest y
    lower = []
    upper = []
    
    # Check if point is to the left of the two first points,
    # if not replaces the last point.
    # Does this for both lower and upper part by going the other way around
    for p in points:
        while len(lower) >= 2 and not left_turn(lower[-2], lower[-1], p):
            lower.pop()
        lower.append(p)

    for p in points[::-1]:
        while len(upper) >= 2 and not left_turn(upper[-2], upper[-1], p):
            upper.pop()
        upper.append(p)

    # Return the list of points but remove the duplicates that come from both lists. 
    return lower[:-1] + upper[:-1]

# Plot an example 
points = random_points(20)
plot_hull(points, convex_hull(points))

# Use scipy to see if we get the right list
from scipy.spatial import ConvexHull
hull_test = [points[idx] for idx in ConvexHull(points).vertices]

assert set(hull_test) == set(convex_hull(points))