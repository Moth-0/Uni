'''
HANDIN 7 (convex hull)

This handin is done by (study ids and names of up to three students):

    202407458 Kenny Nguyen
    202408911 Safiya Chebil 
    202406237 Marie Schnoor - Madsen 

    
Reflection upon solution:

    Sværheden lå i spg c) hvor man skal forstå hvordan man opdater for løkken for hver iteration. at opstille methoden 
    korrekt og vurderer om for løkker var det mest optimal. 
'''

#a
import random as r
def random_points(n):
    list = []
    for i in range(n):
        x,y = r.random(),r.random()
        list.append((round(x,3),round(y,3)))
    return list
random_points(5)
    
#b
import matplotlib.pyplot as plt

def plot_hull(points, polygon):
    pol_x, pol_y = [(x,y)[0] for x,y in polygon], [(x,y)[1] for x,y in polygon]
    point_x, point_y = [(x,y)[0] for x,y in points], [(x,y)[1] for x,y in points]
    plt.plot(pol_x+[pol_x[0]], pol_y+[pol_y[0]], 'r-')
    plt.plot(point_x, point_y, 'go')
    plt.show()


# points = random_points(10)
# polygon = points

# plot_hull(points, polygon)

#c
def left_turn(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]) >= 0

def convex_hull(points):
    '''
    Tager en list af punkter i form af tuples med x og y koordinater.
    Skal indeholde mindst 3 punkter.
    Returner en list der skal bruges til at opbygge polygonet der omringer punkterne. 
    '''
    sort_points_x = sorted(points, key=lambda tup: (tup[0], tup[1]))
    start = sort_points_x[0]
    hull = [start]
    current = start 

    remaining = list(sort_points_x[1:]) + [start]
    while remaining: 
        next_point = remaining[0]
        for i in remaining[1:]: 
            if not left_turn(current, next_point, i): 
                next_point = i 
        hull.append(next_point)
        current = next_point 
        remaining.remove(next_point)
        if current == start:
            break

    return hull

# points = random_points(100)
# k = convex_hull(points)
# polygon = k
# plot_hull(points, k)

#d
def convex_hull(points):
    '''
    Tager en list af punkter i form af tuples med x og y koordinater.
    Skal indeholde mindst 3 punkter.
    Returner en list der skal bruges til at opbygge polygonet der omringer punkterne. 
    '''
    assert isinstance(points, list)
    assert all ([isinstance(i, tuple) for i in points])
    assert len(points) >= 3

    sort_points_x = sorted(points, key=lambda tup: (tup[0], tup[1]))
    start = sort_points_x[0]
    hull = [start]
    current = start 


    remaining = list(sort_points_x[1:]) + [start]
    while remaining: 
        next_point = remaining[0]
        for i in remaining[1:]: 
            if not left_turn(current, next_point, i): 
                next_point = i 
        hull.append(next_point)
        current = next_point 
        remaining.remove(next_point)
        if current == start:
            break

    return hull

assert convex_hull([(0,0.23),(1,0.3), (0.30, 1)]) == [(0, 0.23), (1, 0.3), (0.3, 1), (0, 0.23)]
points = [(0,0.23),(1,0.3), (0.30, 1)]
points = [(3,2), (1,1), (2,3), (2,2), (1.5, 2.25), (2.5, 2.25), (2, 1.25), (1, 1.5)]
h = convex_hull(points)
print(h)
plot_hull(points, h)