"""
HANDIN 7 - Exercise 14.2 (convex hull)

This handin is done by:

202407098 Johanne Stubkjær
202408622 Magnus Overgaard
202405571 Jonas Ullgren

Reflection upon solution:

We found how to solve part (a) pretty quickly, and the same for part (b) when we realized that hx and hy weren't to be used until 
the functon in part (c) was actually called. We also spent some time trying to understand the left_turn function, and eventually
found how to implement it in part (c), which was the most difficult part of this handin.
For part (d) we tried to write some assert-tests. When we run the the code itself, it seems like it works fine in iterms of giving
us the correct polygon / convex hull, however according to the first and last assert test there are some problems. We are not 
entirely sure if the problem is with the assert-tests (that we maybe misunderstand) or the code though.....
"""


import random
import matplotlib.pyplot as plt


# Part (a)
def random_points(n):
    points = []
    
    if not 1 <= n <= 100:
        raise ValueError('n must be an integer in the range [1,100]')

    else:
        for k in range(n):
            x, y = round(random.random(), 5) , round(random.random(), 5)
            points.append((x,y))

    return points

punkter = random_points(13)


# Part (b)
def plot_hull(points, polygon): # It needed an argument called "polygon", which is defined in another function as "poly".
    fig, ax = plt.subplots()
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    hx = [p[0] for p in polygon] + [polygon[0][0]]  # Makes sure to close the loop.
    hy = [p[1] for p in polygon] + [polygon[0][1]]
    
    ax.scatter(xs, ys)
    ax.plot(hx, hy)
    plt.show()


# Part (c)
def left_turn(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]) >= 0
    

def convex_hull(points):
    """
    >>> convex_hull([(0,0),(1,0),(0,1)])
    [(0,0),(1,0),(0,1)]
    """
    
    lex = sorted(set(points))
    
    if len(lex) < 3:
        raise ValueError("More than two distinct points, thank you!")
        
    upper = list.copy(lex) # Finds the upper part
    i = 0
    while i < len(upper)-2:
        if left_turn(upper[i],upper[i+1],upper[i+2]):
            upper.pop(i+1)
            if i > 0:
                i -= 1
        else:
            i += 1

    lower = [] # Finds the lower part
    for p in lex:
        while len(lower) >= 2 and not left_turn(lower[-2], lower[-1], p):
            lower.pop()
        lower.append(p)
        
    CH = lower[::-1] + upper[1:]
    return CH

poly = convex_hull(punkter) 
#plot_hull(punkter, poly)
print()


# Part (d)
test =     [(3,2), (1,1), (2,3), (2,2), (1.5, 2.25), (2.5, 2.25), (2, 1.25), (1, 1.5)]
expected = [(1, 1), (1, 1.5), (2, 3), (3, 2), (2, 1.25)]
result = convex_hull(test)
print(result)

assert convex_hull(test)==expected, f'Expected {expected}, but got {result} for input {test}'
assert set(result).issubset(set(test)), f'There is a problem!....  {set(result) = } is not a subset of {set(test) = }'
assert (0.5,0.6) not in result, f'Interior point (0.5,0.6) incorrectly included in hull {result}, which it should not be!'
assert result[0] == min(result), f'First point {result[0] = } is not the lexicographically smallest {min(result) = }'