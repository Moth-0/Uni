'''
HANDIN 7 (convex hull)

This handin is done by (study ids and names of up to three students):

    202405584 Victor Kvist Loft Pedersen
    202405681 William Malmberg
    202404925 Josefine Ella Luci Sandy Dorothea Wendt

    Reflections upon solutions
    During this handin threre were some time spent on figuring out how to build up the code with the three functions.
    Then it was easier to see what every function had to do with the final product. Then the random function came to us fast.
    After that the plot_hull function was written, where we had some issues with how to get the x and y coordinates 
    from the polygon using the zip-function. Thereafter the plotting, for people skilled in matplolib, was easy.
    Then the convex_hull function gave a bit more trouble since it was harder to split up in the lower and upper part.
    But after reading some pseudo code we got the hang of it and had a working code.
    There were a little bit of discussion aboout if assert is a good way to check variables, which it of coruse it is!
    Then we had to change the code to being clockwise which then made sure it could pass the doctest.

    Best regards group
    William, Josefine ELla Luci Sandy Dorothea Wendt and Victor Kvist Loft Pedersen
'''

from random import random
import matplotlib.pyplot as plt
import doctest

def random_points(n: int) -> list[tuple]:
    '''Return list of n random (x, y) pairs representing points'''

    assert 1 <= n <= 100, "number not between 1 and 100"
    assert isinstance(n, int), "Input is not an integer"

    points = [(random(), random()) for _ in range(n)]
    assert len(points) == n
    return points

def plot_hull(points: list[tuple], polygon: list[tuple]) -> None:
    '''Plot all points and the polygon'''
    assert isinstance(points, list)
    assert isinstance(polygon, list), f"polygon is {polygon}"

    for x, y in points:
        plt.scatter(x, y, c="green")

    x, y = zip(*polygon, polygon[0])

    plt.plot(x, y)

def convex_hull(p: list) -> list:
    '''Compute the convex hull of a set of 2D points
    
    Input: A list of (x, y) pairs representing points
    Output: A list of vertices in the convex clockwise order 
        starting from the vertex with the lexicographically lowest coordinate

    Examples:
    >>> convex_hull([(0, 0), (0,4), (4,0), (4,4), (2,2), (3,3), (2,1), (3,1)])
    [(0, 0), (0, 4), (4, 4), (4, 0)]
    >>> convex_hull([(3,2), (1,1), (2,3), (2,2), (1.5, 2.25), (2.5, 2.25), (2, 1.25), (1, 1.5)])
    [(1, 1), (1, 1.5), (2, 3), (3, 2), (2, 1.25)]
    '''
    assert isinstance(p, list), "p must be a list"
    assert len(p) >= 3, "There must be atleast three points"

    def left_turn(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]) >= 0
    
    p.sort()
    u = []
    l = []
    n = len(p)

    for i in range(n):
        while len(l) >= 2 and left_turn(l[-2], l[-1], p[i]):
            del l[-1]
        l.append(p[i])
    
    for i in range(n-1, -1, -1):
        while len(u) >= 2 and left_turn(u[-2], u[-1], p[i]):
            del u[-1]
        u.append(p[i])

    del u[-1]
    del l[-1]

    CH = l+u

    assert min(CH) == CH[0], "First coordinate is not the lexicographically lowest"
    assert isinstance(CH, list), "CH is not list"

    return CH

doctest.testmod(verbose=True)