import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

def points_on_circle(center, radius, n):
    x, y = center
    return [(x + radius * np.cos(angle), y + radius * np.sin(angle))
            for angle in np.linspace(0, 2 * np.pi * (n - 1) / n, n)]


def distance(p, q):  # distance between d-dimensional vectors
    return np.sqrt(sum((i - j)**2 for i, j in zip(p, q)))


def min_distance(p, centers):
    return min(distance(p, q) for q in centers)


def distance_sum(centers):
    return sum(min(distance(c, p) for c in centers) for p in points)


def plot_solution(centers, fixed_centers=None, trace=None, cost=''):
    if trace:  # show optimization trace
        coordinates = list(zip(*trace))
        for idx, (x, y) in enumerate(zip(coordinates[0::2], coordinates[1::2])):
            plt.plot(x, y, 'k-', alpha=0.25,
                label='minimize trace' if idx==0 else None)
        plt.plot(trace[0][0::2], trace[0][1::2], 'k.',
                 label='optimization seed')

    if fixed_centers != None:  # show contour map
        points_X, points_Y = zip(*points)
        x_min = min(points_X)
        x_max = max(points_X)
        y_min = min(points_Y)
        y_max = max(points_Y)
        padding = 0.1
        x_min -= (x_max - x_min) * padding
        x_max += (x_max - x_min) * padding
        y_min -= (y_max - y_min) * padding
        y_max += (y_max - y_min) * padding
        X, Y = np.meshgrid(np.linspace(x_min, x_max, 100),
                           np.linspace(y_min, y_max, 100))

        Z = np.zeros(X.shape)
        for p in points:
            px, py = p
            dist = np.sqrt((X - px)**2 + (Y - py)**2)
            if fixed_centers:
                dist = np.minimum(dist, min_distance(p, fixed_centers))
            Z += dist
        CS = plt.contour(X, Y, Z)
        plt.clabel(CS, inline=1, fontsize=10, fmt='%1.2f')

    if centers:
        for idx, p in enumerate(points):  # line from point to nearest center
            nearest = centers[np.argmin([distance(p, c) for c in centers])]
            plt.plot(*zip(p, nearest), 'y:', label='Nearest center' if idx == 0 else None)
    fixed = [c for c in centers if fixed_centers != None and c in fixed_centers]
    free = list(set(centers) - set(fixed))
    if fixed: plt.plot(*zip(*fixed_centers), 'ro', label='Fixed center')
    if free: plt.plot(*zip(*free), 'bo', label='Center')
    plt.plot(*zip(*points), 'g.', label='Input point')
    if cost: plt.legend(title='Cost = %.2f' % cost)


######################################################################
# Geometric Median example plot

def opt_function(coordinates):
    trace.append(coordinates)
    centers = list(zip(coordinates[0::2], coordinates[1::2]))
    return distance_sum(centers)

def opt_start(centers):  # init trace & flatten seed
    global trace
    trace = []
    return [v for c in centers for v in c]

points = points_on_circle((-2, 5), 1, 10)
points += points_on_circle((-3, -4), 2, 12)
points += points_on_circle((10, 1), 0.5, 4)

seeds = [
#         [(10, -4)],
         [(0, 0), (0, 1)],
         [(0, 0), (7, 0)],
#         [(0,0), (1,1), (1,-1)]
         ]

FIGS = sum(len(seed) for seed in seeds)
fig = 1
for seed in seeds:
    solution = minimize(opt_function, opt_start(seed))  #, method='nelder-mead')
    centers = list(zip(solution.x[0::2], solution.x[1::2]))
    for i in range(len(seed)):
        plt.subplot(1, FIGS, fig)
        plot_solution(centers, fixed_centers=centers[:i] + centers[i+1:], trace=trace, cost=solution.fun)
        fig += 1

plt.suptitle('Geometric Median (scipy.minimize)')
plt.show()
