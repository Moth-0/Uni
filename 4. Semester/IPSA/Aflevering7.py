"""
HANDIN 7 - convex hull

This handin is done by: 
    202307989 Mikkel Moth Billing 

Reflection upon solution: 
    
"""
from random import random
import matplotlib.pyplot as plt

def left_turn(p, q, r):
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
    assert isinstance(points, list)
    assert isinstance(polygon, list)
    
    x, y = zip(*points)
    px, py = zip(*polygon)
    plt.plot(x, y, "o")
    plt.plot(px + (px[0],), py + (py[0],), "k-") # adds first point again to complete ploygon
    plt.show()

def convex_hull(points): 
    return

plot_hull(random_points(4), [(0,0), (0.5,0), (0.5,0.5), (0, 0.5)])