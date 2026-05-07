#%%
#Exercise 14.2 (convex hull)

'''
HANDIN 7 (Handin 7 - convex hull)

This handin is done by 
    202305360: Arunchand Suriyakumar

Reflection upon solution:
    A: The random point are found using random() which gives number in [0, 1)

    B: We unpack the points using zip and *. The they are plotted

    C: To find the points in the convex hull, we first notice that all the points in the convex hull set
    satisfy that when running anti-clocwise through the them, ALL the rest of the points are to the left
    of the line drawn between each convex-hull point and the next. This means that:

    A point is a convex hull point if and only if left_turn(p, q, r) is True for all r in the remaining points

    Now the idea is then to start at the lexiographically lowest point and for each other point
    we check if the condition above is satisfied. If it is satisfied, we save it and jump to that point
    and repeats the process, until we return back to start at which the loop is ended. 

    D: We have ussed assert statements througout the code. Finally, a docstring has been added
    such that doctest can be run. We have taken the example from the exercise along with a 
    random example as a visual test


'''

#%%
from random import random #random() generates random number in [0,1)
import matplotlib.pyplot as plt
import doctest


def random_points(n):
    assert 1<= n <= 100, 'n should be between 1 and 100'
    
    points = [(random(), random()) for _ in range(n)]

    return points

#%%
def plot_hull(points, polygon):
    x_values, y_values = zip(*points)

    x_values_poly, y_values_poly = zip(*polygon)

    plt.plot(x_values, y_values, 'go')
    plt.plot(x_values_poly, y_values_poly, 'r')
    plt.plot((x_values_poly[-1], x_values_poly[0]), 
             (y_values_poly[-1], y_values_poly[0]), 'r')


def left_turn(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]) >= 0

#%%
def convex_hull(points):
    '''Convex hull solutions for a random set of points.
    Examples:
    Using the one from the exercise itself
    >>> convex_hull([(3,2), (1,1), (2,3), (2,2), (1.5, 2.25), (2.5, 2.25), (2, 1.25), (1, 1.5)])
    [(1, 1), (1, 1.5), (2, 3), (3, 2), (2, 1.25)]

    Visual tests
    >>> q = random_points(60)
    >>> plot_hull(q, convex_hull(q))
    '''

    convex = []
    points = sorted(points)
    p = points[0] 
    while p != None: 
        for q in points: #p is our standing point, and we want to check if q is a CH-point
            if q != p:
                check = [left_turn(p,q,r) for r in points if r != p and r !=q]
                if all(check):
                    convex.append(q)
                    if q != points[0]:
                        p = q   #We jump to next point and repeat loop
                    else:
                        p = None #Now we are back at the start, hence breaking the loop
                        break
    convex.reverse() #To get clockwise order
    assert len(convex) != 0, 'No convex hull found. Something wrong in code'
    return  convex 



doctest.testmod()
