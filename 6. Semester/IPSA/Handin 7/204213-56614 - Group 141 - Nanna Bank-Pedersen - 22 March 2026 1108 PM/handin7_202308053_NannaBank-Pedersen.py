'''
HANDIN 7 (convex hull)

This handin is done by:
    202308053 Nanna Bank-Pedersen

Reflection upon solution:
Jeg synes det var svært at forstå convex hull konceptet, og det tog lang tid at finde ud af hvordan man kunne implementere det. 
Det var også lidt udfordrende at få det til at fungere med både random points og plot funktionen da jeg ikke lige har prøvet at køre plots gennem terminal før. 
Jeg sorterer punkterne og derefter bygger hull ved at tjekke for left turns. Jeg har også brugt hjælpefunktionen left_turn. Jeg antager at input er gyldige punkter 
i form af tuples (x, y), og har ikke lavet nogen begrænsninger på det i koden. Jeg havde også lidt svært ved at bruge doctest, da det også er første gang jeg 
bruger det, så jeg var nødt til at finde ud af hvordan man formaterer det.
'''
# a) random points function
from random import random
import matplotlib.pyplot as plt


def random_points(n):
    assert 1 <= n <= 100
    points = []
    
    for i in range(n):
        x = round(random(), 5)
        y = round(random(), 5)
        points.append((x, y))
        
    return points

"""
print(random_points(5))
"""

# b) plot hull function
def plot_hull(points, polygon):
    x_points, y_points = zip(*points)
    plt.plot(x_points, y_points, 'go')

    poly = polygon + [polygon[0]]
    x_poly, y_poly = zip(*poly)
    plt.plot(x_poly, y_poly, 'r-')

    plt.show()

"""
points = [(3,2), (1,1), (2,3), (2,2), (1.5,2.25), (2.5,2.25), (2,1.25), (1,1.5)]
polygon = [(1,1), (3,2), (2,3), (1,1.5)]
plot_hull(points, polygon)
plt.plot([0,1,2], [0,1,4], 'ro-')
plt.show()
"""

# hjælpefunktion left-turn
def left_turn(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]) >= 0

# c) & d) convex hull funktion og doctest assert
def convex_hull(points):
    """
    Compute the convex hull of a set of points.

    >>> convex_hull([(0,0), (1,0), (1,1), (0,1)])
    [(0, 0), (1, 0), (1, 1), (0, 1)]

    >>> convex_hull([(0,0), (1,0), (1,1), (0,1), (0.5,0.5)])
    [(0, 0), (1, 0), (1, 1), (0, 1)]

    >>> convex_hull([(0,0), (2,0), (1,1)])
    [(0, 0), (2, 0), (1, 1)]
    """
    assert len(points) >= 3
    lower = []
    pts = sorted(points)

    for p in pts:
        while len(lower) >= 2 and left_turn(lower[-2], lower[-1], p):
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and left_turn(upper[-2], upper[-1], p):
            upper.pop()
        upper.append(p)

    CH = lower[:-1] + upper[:-1]
    #CH.reverse()

    min_index = CH.index(min(CH))
    CH = CH[min_index:] + CH[:min_index]
    
    return CH


if __name__ == "__main__":
    import doctest
    doctest.testmod()

print(convex_hull([(3,2), (1,1), (2,3), (2,2), (1.5,2.25), (2.5,2.25), (2,1.25), (1,1.5)]))
