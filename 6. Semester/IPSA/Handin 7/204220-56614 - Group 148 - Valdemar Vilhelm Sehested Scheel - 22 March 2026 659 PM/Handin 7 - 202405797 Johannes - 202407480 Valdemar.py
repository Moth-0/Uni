"""
HANDIN 7 (Convex Hull)

This handin is done by:
    202405797 Johannes Bøgh Fangel
    202407470 Valdemar Scheel

Reflection upon solution:
    Hard Parts: At first we had a little trouble how to implement the convex hull function. 
    Especially how we could iterate over it and remove a point and then still catch, if a
    point before that should now be removed. We solved this using a while-loop and some if
    statements controlling, what to do when we remove a point. The only other thing we
    found a little hard was coming up with usage examples for the docstring, so that we
    could test the function using doctest.
"""


# -------------------------------------------------------------------------------------------------------
import random
import matplotlib.pyplot as plt
import doctest


def random_points(n):
    return [(random.random(), random.random()) for i in range(n)]

def left_turn(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]) >= 0

def plot_hull(points, polygon):
    plt.plot([point[0] for point in polygon+[polygon[0]]], [point[1] for point in polygon+[polygon[0]]], 'r-')
    plt.plot([point[0] for point in points], [point[1] for point in points], 'go')
    plt.show()


def convex_hull(points):
    """ Finds the convex hull of a couple of points
    
    
    Usage examples:
        >>> convex_hull([(3,2), (1,1), (2,3), (2,2), (1.5, 2.25), (2.5, 2.25), (2, 1.25), (1, 1.5)])
        [(1, 1), (1, 1.5), (2, 3), (3, 2), (2, 1.25)]
        >>> convex_hull([(1,1), (2,2), (1.5, 2.25), (2, 1.25), (1, 1.5)])
        [(1, 1), (1, 1.5), (1.5, 2.25), (2, 2), (2, 1.25)]
        >>> convex_hull([(2, 3), (2, 2), (2, 1.25)])
        [(2, 1.25), (2, 3)]
    """
    upper_hull = sorted(sorted(points, key=lambda p: p[1]), key=lambda p: p[0])
    i = 1
    while i != len(upper_hull)-1:
        if len(upper_hull) <= 2:
            break
        
        
        elif left_turn(upper_hull[i - 1], upper_hull[i], upper_hull[i + 1]):
            upper_hull.remove(upper_hull[i])
            i -= 1
            continue

        else:
            i += 1

    lower_hull = sorted(sorted(points, key=lambda p: p[1], reverse=True), key=lambda p: p[0], reverse=True)
    while i != len(lower_hull)-1:
        if len(lower_hull) <= 2:
            break
        
        elif left_turn(lower_hull[i - 1], lower_hull[i], lower_hull[i + 1]):
            lower_hull.remove(lower_hull[i])
            i -= 1
            continue

        else:
            i += 1

    return upper_hull +  lower_hull[1:-1]

points = [(3,2), (1,1), (2,3), (2,2), (1.5, 2.25), (2.5, 2.25), (2, 1.25), (1, 1.5)]
polygon = convex_hull([(3,2), (1,1), (2,3), (2,2), (1.5, 2.25), (2.5, 2.25), (2, 1.25), (1, 1.5)])
print(polygon)

plot_hull(points, polygon)

# Test using doctest
if __name__ == '__main__':
    doctest.testmod(verbose=True)


# Tests using assert
test1 = convex_hull([(3,2), (1,1), (2,3), (2,2), (1.5, 2.25), (2.5, 2.25), (2, 1.25), (1, 1.5)])
test2 = convex_hull([(1,1), (2,2), (1.5, 2.25), (2, 1.25), (1, 1.5)])
test3 = convex_hull([(2, 3), (2, 2), (2, 1.25)])

assert test1 == [(1, 1), (1, 1.5), (2, 3), (3, 2), (2, 1.25)]
assert test2 == [(1, 1), (1, 1.5), (1.5, 2.25), (2, 2), (2, 1.25)]
assert test3 == [(2, 1.25), (2, 3)]

