import random as rd
import matplotlib.pyplot as plt
import numpy as np

'''
HANDIN 7 (convex hull)

This handin is done by:

    202106248 Matilde E. Hansen
    202105331 Elias R. Skjoldborg

Reflection upon solution: 

The method used for collecting the correct points for the convex hull was to, from an appropriate starting point (lowest x-value), select the next point on the 
x-axis and see if any points are left of that, when you draw a line between that point and the starting point. If there is a point to the left, we discard the
point and checks the next point on the x-axis. When a point does not have other points to the left, that point is appeended in the convex hull list, and is then
the new starting point, continuing the search for new points to add to the hull. This method however, breaks when we've reached the last point in the x-axis, i. e.
the point with the highest x-value and the search stops there. To close the polygon, we flip the list of points from lowest to highest x-values to continue the 
search towards the lowest x-value, thus closing the polygon. We implement the example convex hull polygon from the assignment to use for doctesting, and we have
implemented two assert tests to see if the points are written correctly as tuples and if there are any point duplicates.

'''

def random_points(n):                                                   # Random points function
    i = 0
    L = []
    while i < n:
        x,y = round(rd.random(),2), round(rd.random(),2)                # We dont want too many decimals, so im just giving them two. 
        point = (x,y)
        L.append(point)
        i = i + 1
    return L

def to_plot(L):                                                         # This is a help function so we can plot the x and y coordinates more easily
    x = []
    y = []
    for i in L:
        x.append(i[0])
        y.append(i[1])
    return x,y

def left_turn(p, q, r):                                                 # Left turn function to determine if a point is to the left of two other points
    return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]) > 0

def convex_hull(L):
    
    '''
    Examples:
    >>> convex_hull([(3,2), (1,1), (2,3), (2,2), (1.5, 2.25), (2.5, 2.25), (2, 1.25), (1, 1.5)])
    [(1, 1), (1, 1.5), (2, 3), (3, 2), (2, 1.25), (1, 1)]

    >>> convex_hull([(1,1)])
    [(1, 1)]
    '''

    assert all(type(x) == tuple for x in L), 'All points must be tuple' # Checking if all the points are written correctly
    assert len(L) == len(set(L)), 'Input has dublicates'                # Checking if two points have the exact same coordinates

    sorted_x = sorted(L, key=lambda L: L[0])                            # Here we sort the points with respect to the x-values (lowest first)
    Hull = [sorted_x[0]]

    Stand_point = sorted_x[0]                                           # This is the starting point for the convex hull
    while Stand_point != sorted_x[-1]:
        for i in np.arange(1, len(sorted_x[0:])):
            if len(sorted_x[i])== 1 or all(left_turn(Stand_point,x,sorted_x[i]) for x in sorted_x[i+1:]): # Here we sort out the points that goes in the convex hull
                Hull.append(sorted_x[i])
                Stand_point = sorted_x[i]
                break                                                   # Note that this while-loop above only applies for the y-coordinates going higher
    sorted_x = sorted_x[::-1]                                           # In order to catch the lower points, closing the polygon, we turn the method around by
    while Stand_point != sorted_x[-1]:                                  # flipping the order of sorted_x
        for i in np.arange(1,len(sorted_x[0:])):
            if len(sorted_x[i])== 1 or all(left_turn(Stand_point,x,sorted_x[i]) for x in sorted_x[i+1:]):
                Hull.append(sorted_x[i])
                Stand_point = sorted_x[i]
                break

    return Hull

def plot_hull(points, polygon):                                         # Plotting function, plotting all points and the polygon
    all_points = to_plot(points)
    convex_points = to_plot(polygon)

    plt.plot(all_points[0], all_points[1], 'ro')
    plt.plot(convex_points[0],convex_points[1], 'g.-')
    plt.show()

Points = random_points(10)
Hull = convex_hull(Points)
# print(Hull)
plot_hull(Points,Hull)

import doctest
doctest.testmod(verbose=True)

