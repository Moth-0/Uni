'''
HANDIN 7 (convex hull)

This handin is done by Mathias Lystlund, id: 202408483:

Reflection upon solution:
I approached the convex hull problem by simulating a rotating reference line,
which felt intuitive geometrically. However I realize that my implementation relies
heavily on approximations, especially through discretizing angles and using floating-point
comparisons. This makes the method sensitive to resolution and numerical tolerance,
so it may miss the correct extreme points or pick suboptimal ones. Additionally, selecting
the first valid point rather than the most extreme candidate introduces inaccuracies
in the hull construction. My solution should capture the idea, but lacks robustness
and precision compared to more exact geometric algorithms.
'''

import numpy as np
import random as ran
import matplotlib.pyplot as plt
def random_points(n):
    points = []
    for i in range(n):
        points.append((round(ran.random(), 2), round(ran.random(), 2)))
    return points

po = random_points(6)
print(po)


def left_turn(p, q, r):
    val = (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1])
    return abs(val) < 1e-4

fig, ax = plt.subplots()
def plot_hull(points, polygon):
    point = [list(x) for x in points]
    
    for i in point:
        plt.scatter(i[0], i[1])
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i+1) % len(polygon)]

        plt.plot([p1[0], p2[0]], [p1[1], p2[1]])

k = plot_hull(po, [po[0], po[1], po[2]])
plt.grid('on')


def Convex_hull(points):
    start = min(points)
    first = start
    ref = [first[0], -4]
    læn = np.sqrt((ref[0] - first[0])**2 + (ref[1] - first[1])**2)
    
    
    #læn = np.sqrt((abs(ref[0]) - abs(first[0])**2) + (abs(ref[1]) - abs(first[1]))**2)
    convex_points = [start]
    while True:
        print(læn)
        ang = np.arctan2(ref[1]-first[1], ref[0]-first[0])
        #ang_y = np.arcsin(np.radians(ref[1]/læn))
        rest = [p for p in points if p != first]
        x = np.linspace(0, 2*np.pi, 36000)
        px = læn*np.cos(ang-x) + first[0]
        py = læn*np.sin(ang-x) + first[1]
        q = list(zip(px, py))
        bre = False
        for i in q:
            for n in rest:
                if on_segment(first, i, n) == True and n not in convex_points:
                    if len(convex_points) == 6:
                        return convex_points
                    A = np.array(first)
                    
                    B = np.array(n)
                    #v = i + (B - A)
                    P = 2*B - A
                    #v_hat = v / np.linalg.norm(v)
                    #P = A + 20 * v_hat
                    print(i)
                    print(P)
                    
                    first = tuple(B)
                    ref = tuple(P)
                    convex_points.append(n)
                    bre = True
                    break
            if bre:
                break
                    
        if not bre:
            break
h = Convex_hull(po)
print(h)