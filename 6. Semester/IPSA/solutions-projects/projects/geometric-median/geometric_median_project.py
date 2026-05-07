import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from scipy.optimize import minimize
from math import sqrt
from random import random
#import geocoder
import pyproj
import matplotlib.pyplot as plt
import time

# Question 1
def distance(p, q):
    ''' Compute distance between d-dimensional points 'p' and 'q' '''

    return sqrt(sum((a - b)**2 for a, b in zip(p, q)))

def distance_sum(points, q):
    ''' Compute sum of distances from 'q' to all points in 'points' '''
    return sum(distance(p, q) for p in points)

def geometric_median(points):
    ''' Compute the geometric median point for the points in 'points' '''

    return minimize(lambda q: distance_sum(points, q), [0, 0]).x

# Question 2
def plot_geometric_median(points):
    ''' Plot points in 'points' and their geometric median '''

    c = geometric_median(points)

    min_x, max_x, min_y, max_y = bounding_box(points)
    plt.xlim(min_x, max_x)
    plt.ylim(min_y, max_y)

    for p in points:
        plt.plot(*zip(*[p, c]), "y:")
    plt.plot(*c, "bo")
    plt.plot(*zip(*points), "r.")

# Question 3    
def bounding_box(points):
    ''' Compute bounding box for a set of points '''

    (min_x, max_x), (min_y, max_y) = [(min(vs), max(vs)) for vs in zip(*points)]

    d = max(max_x - min_x, max_y - min_y) / 10

    return min_x - d, max_x + d, min_y - d, max_y + d

def plot_contour(points):
    ''' Plot contour lines for the 'distance_sum' function within
        the bounding box of points
    '''

    min_x, max_x, min_y, max_y = bounding_box(points)
    
    plot_geometric_median(points)
    Z = [[distance_sum(points, (x, y)) 
          for x in linspace(min_x, max_x, 50)]
          for y in linspace(min_y, max_y, 30)]

    contour = plt.contour(Z, extent=(min_x, max_x, min_y, max_y))
    plt.clabel(contour, inline=1, inline_spacing=1, fontsize=8, fmt='%.1f')

# Question 4
def left_turn(p, q, r):
    ''' return if three points p, q, r constitute a left turn '''
    return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]) >= 0

def two_geometric_medians(points):
    if len(points) == 2:
        return points

    total, q1, q2 = None, None, None

    for p1 in points:
        for p2 in points:
            if p1 != p2:
                A = [p for p in points if left_turn(p1, p2, p)]
                B = [p for p in points if not left_turn(p1, p2, p)]

                a = geometric_median(A)
                b = geometric_median(B)
                total_ = distance_sum(A, a) + distance_sum(B, b)

                if total == None or total_ < total:
                    total, q1, q2 = total_, a, b
 
    return q1, q2

# Question 5
def plot_two_geometric_medians(points):
    q1, q2 = two_geometric_medians(points)

    (min_x, max_x, min_y, max_y) = bounding_box(points)

    a = np.array(q1)
    b = np.array(q2)
    m = (a + b) / 2
    d = a - b 
    d = np.array([-d[1], d[0]])

    if abs(d[1]) > abs(d[0]):
        m_top = m + d * (max_y - m[1]) / d[1]
        m_bottom = m + d * (min_y - m[1]) / d[1]
    else:
        m_top = m + d * (max_x - m[0]) / d[0]
        m_bottom = m + d * (min_x - m[0]) / d[0]

    plt.xlim(min_x, max_x)
    plt.ylim(min_y, max_y)
    for p in points:
        q = q1 if distance(p, q1) < distance(p, q2) else q2
        plt.plot(*zip(*[p, q]), "y:")
    plt.plot(*zip(*[q1, q2]), "b:o")
    plt.plot(*zip(*points), "r.")

    plt.plot(*m, "go")
    plt.plot(*zip(*[m_bottom, m_top]), "b-")

    total_distance = sum(min(distance(p, q) for q in (q1, q2)) for p in points)
    plt.title(f'Total distance {total_distance:.5f}')

# Question 6
def left_turn(p, q, r):
    '''Return if three points p, q, r constitute a left turn.'''
    
    det = (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1])
    if det != 0:
        return det >= 0

    # if p, q, r are on line, return if r is before or after p
    q2 = p[0] - (q[1] - p[1]), p[1] + (q[0] - p[0])
    return (q2[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q2[1] - p[1]) >= 0

# Question 7
netto_address = [ 
  "Korshøjen 1, 8240 Risskov",
  "Frijsenborgvej 5, 8240 Risskov",
  "Randersvej 116-118, 8200 Aarhus",
  "Finlandsgade 15, 8200 Aarhus",
  "Skovvejen 17, 8000 Aarhus",
  "Thorvaldsensgade 22-24, 8000 Aarhus",
  "Sankt Knuds Torv 2, 8000 Aarhus",
  "Silkeborgvej 246, 8230 Aarhus",
  "Silkeborgvej 650, 8220 Brabrand",
  "Finderupvej 1-3, 8000 Aarhus",
  "Jægergårdsgade 64-70, 8000 Aarhus"
  "Frederiks Allé 162, 8000 Aarhus",
  "Søren Frichs Vej 53m, 8230 Aarhus",
  "Viby Ringvej 20, 8260 Viby",
]

coordinates = [[56.20019929999999, 10.2235067],
               [56.189145, 10.214827],
               [56.1780266, 10.2013551],
               [56.17027299999999, 10.18925],
               [56.1644677, 10.2165978],
               [56.156526, 10.196554],
               [56.1513585, 10.2058708],
               [56.1555554, 10.1662598],
               [56.1543354, 10.0978546],
               [56.155654, 10.18228],
               [56.148483, 10.2057255],
               [56.1500915, 10.1682726],
               [56.1309422, 10.1593882]]

# coordinates = [] # force fetching coordinates from google

if coordinates == []:
    print("Fetching coordinates of addresses")
    for a in netto_address:
        print(a)
        ll = geocoder.google(a).latlng
        while ll == None:
            time.sleep(1)
            ll = geocoder.google(a).latlng
        print(ll)
        coordinates.append(ll)

p = pyproj.Proj(proj='utm', zone=32, ellps='WGS84')

netto = [p(c[1], c[0]) for c in coordinates if c is not None]

# end Question 7

point_sets = [
    [(20*random()**2 - 10, 10*(1-random()**3) - 10) for _ in range(10)],
    [(1,1), (2,1), (3,1), (4,1)],
    # The following point set gives a different solution if 2-means is used instead of 2-median
    [(0,0), (0,1), (1,0), (1,1), (25, 0), (25, 1), (26, 0), (26, 1), (0, 70)],
    # netto,
]

plt.suptitle('Geometric median')
for idx, points in enumerate(point_sets, start=1):

    ax = plt.subplot(3, len(point_sets), idx)
    ax.set_aspect('equal')
    plot_geometric_median(points)

    ax = plt.subplot(3, len(point_sets), idx + 1 * len(point_sets))
    ax.set_aspect('equal')
    plot_contour(points)
    
    ax = plt.subplot(3, len(point_sets), idx + 2 * len(point_sets))
    ax.set_aspect('equal')
    plot_two_geometric_medians(points)

plt.show()
