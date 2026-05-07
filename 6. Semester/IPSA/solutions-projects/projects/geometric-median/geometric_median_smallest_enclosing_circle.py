"""This program visualizes the problem of minimizing the sum of
distances to a set of points.  The point with minimum sum of distances
to all points is known as the Geometric median
(https://en.wikipedia.org/wiki/Geometric_median)

A recent algorithmic paper on the problem:
"Geometric Median in Nearly Linear Time",
Cohen, Lee, Miller, Pachocki, Sidford
https://arxiv.org/abs/1606.05225

Also visualizes finding the minimum enclosing circle problem
"""

from math import sqrt
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

opt_algorithm = 'nelder-mead' # Default is BFGS (fails)

######################################################################

points_X = [1.0, 3.0, 2.5, 4.0, 5.0, 6.0, 5.0]
points_Y = [3.0, 1.0, 3.0, 6.0, 7.0, 7.0, 2.0]

points = list(zip(points_X, points_Y))

######################################################################
#  Geometric Median solver

print("GEOMETRIC MEDIAN")


def distance(p, q):
    """ compute distance between d-dimensional points p and q """
    return sqrt(sum([(i-j)**2 for i, j in zip(p, q)]))


def distance_sum(p):
    """ compute sum of distances from p to all points in global points """
    return sum([distance(p, q) for q in points])


solution = minimize(distance_sum, [0.0, 0.0], method=opt_algorithm)

cx, cy = list(solution.x)

print(solution)

######################################################################
# 2D plot of points and Geometric Median (center)

plt.subplot(2, 3, 1)
plt.title("Geometric Median")
plt.xlabel("x")
plt.ylabel("y", rotation="horizontal")
plt.tight_layout()

for x, y in points:  # line from center to each point
    plt.plot([cx, x], [cy, y], "y:")  # (yellow dotted)

plt.plot([cx], [cy], "ro")            # center point (red circle)
plt.plot(points_X, points_Y, "g.")    # data points (green dots)

######################################################################
#  Plot 3D plot around minimum

x_min = min(points_X)
x_max = max(points_X)
y_min = min(points_Y)
y_max = max(points_Y)
z_min = distance_sum((cx, cy))
z_max = max([distance_sum(p) for p in points])

grid_x_values = np.arange(x_min, x_max, (x_max-x_min)/100.0)
grid_y_values = np.arange(y_min, y_max, (y_max-y_min)/100.0)

X, Y = np.meshgrid(grid_x_values, grid_y_values)

Z = np.zeros(X.shape)

for px, py in points:
    Z += np.sqrt((X-px)**2 + (Y-py)**2)

plt.subplot(2, 3, 2, projection='3d')
plt.title("Sum point distances")

ax = plt.gca()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("sum of distances")
ax.set_zlim(z_min, z_max)
plt.tight_layout()

surf = ax.plot_surface(X, Y, Z)
ax.scatter([cx], [cy], [z_min], c="red")

######################################################################
# Geometric Median - contour plot

plt.subplot(2, 3, 3)
plt.title("Sum point distance")
CS = plt.contour(X, Y, Z)
plt.clabel(CS, inline=1, fontsize=10, fmt="%1.2f")

######################################################################
# Minimum enclosing circle solver

print("MINIMUM ENCLOSING CIRCLE")
      

def distance_max(c):
    """computes the distance to the point furthest away from c"""
    return max([distance(p, c) for p in points])


solution = minimize(distance_max, [0.0, 0.0], method=opt_algorithm)

cx, cy = solution.x
c = (cx, cy)
r = distance_max(c)

print(solution)

######################################################################
# 2D plot of points and minimum enclosing circle

plt.subplot(2, 3, 4)
plt.title("Minimum enclosing circle")
plt.xlabel("x")
plt.ylabel("y", rotation="horizontal")
plt.tight_layout()

plt.plot([cx], [cy], "ro")           # center point (red circle)
plt.plot(points_X, points_Y, "g.")   # data points (green dots)

circle = plt.Circle((cx, cy), r, color='r', fill=False)
ax = plt.gca()
ax.add_artist(circle)
R = r * 1.1
ax.set_xlim((cx-R, cx+R))
ax.set_ylim((cy-R, cy+R))
ax.set_aspect("equal")

######################################################################
#  3D plot for minimum enclosing circle

x_min = min(points_X)
x_max = max(points_X)
y_min = min(points_Y)
y_max = max(points_Y)
z_min = distance_max((cx, cy))
z_max = max([distance_max(p) for p in points])

grid_x_values = np.arange(x_min, x_max, (x_max-x_min)/100.0)
grid_y_values = np.arange(y_min, y_max, (y_max-y_min)/100.0)

X, Y = np.meshgrid(grid_x_values, grid_y_values)

Z = np.zeros(X.shape)

for px, py in points:
    Z = np.maximum(Z, np.sqrt((X-px)**2 + (Y-py)**2))

plt.subplot(2, 3, 5, projection='3d')
plt.title("Maximum point distance")

ax = plt.gca()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("max distance")
ax.set_zlim(z_min, z_max)
plt.tight_layout()

surf = ax.plot_surface(X, Y, Z)
ax.scatter([cx], [cy], [z_min], c="red")

######################################################################
# Minimum enclosing circle - contour plot

plt.subplot(2, 3, 6)
plt.title("Maximum point distance")
CS = plt.contour(X, Y, Z)
plt.clabel(CS, inline=1, fontsize=10, fmt="%1.2f")

######################################################################

plt.show()
