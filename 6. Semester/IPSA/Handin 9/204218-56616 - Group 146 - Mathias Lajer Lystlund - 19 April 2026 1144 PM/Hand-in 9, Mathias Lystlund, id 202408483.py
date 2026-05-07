'''
HANDIN 9 (Maximum flow)

This handin is done by Mathias Lystlund, id: 202408483:


Reflection upon solution:
In this solution, I formulated the network flow problem as a linear program by assigning one variable to each 
edge and encoding flow conservation through a matrix representation. I initially approached it as a maximum flow 
problem, but then adapted it to a minimum-cost flow by introducing costs and fixing the total flow from the source. 
A key realization was that the total flow constraint must be enforced explicitly, rather than through sink-related coefficients.
'''

import numpy as np
from scipy.optimize import linprog
edges = [
    ('A', 'C', 4),
    ('A', 'B', 3),
    ('C', 'E', 1),
    ('C', 'D', 1),
    ('B', 'E', 3),
    ('B', 'D', 1),
    ('E', 'D', 3),
    ('E', 'F', 1),
    ('D', 'F', 5)
]

source = 'A'
sink = 'F'

def Maximum_flow(edges, source, sink, flow=None):
    rows = []
    for i, n in enumerate(edges):
        if n[1] != source and n[1] != sink and n[1] not in rows:
            rows.append(n[1])
        if n[0] != source and n[0] != sink and n[0] not in rows:
            rows.append(n[0])

    matrix = [[0 for _ in range(len(rows))] for _ in range(len(edges))]
    sinks = [0 for _ in range(len(edges))]
    capacity = []
    cost = []

    for i, n in enumerate(edges):
        if flow is not None:
            cost.append(n[3])

        capacity.append(n[2])

        if n[0] != source and n[1] != sink:
            k = rows.index(n[1])
            matrix[i][k] = -1
            g = rows.index(n[0])
            matrix[i][g] = 1

        if n[0] == source:
            k = rows.index(n[1])
            matrix[i][k] = -1

        if n[1] == sink:
            k = rows.index(n[0])
            matrix[i][k] = 1
            if flow is None:
                sinks[i] = 1

    matrix_T = list(map(list, zip(*matrix)))

    if flow is not None:
        source_row = [1 if n[0] == source else 0 for n in edges]
        matrix_T.append(source_row)

    return matrix_T, sinks, capacity, cost

find = Maximum_flow(edges, source, sink)
conservation = np.array(find[0])
sinks = np.array(find[1])
capacity = np.array(find[2])

res = linprog(-sinks, A_eq=conservation,
               b_eq=np.zeros(conservation.shape[0]),
                A_ub=np.eye(capacity.size),
                b_ub=capacity)

edges1 = [
    ('A', 'C', 4, 1),
    ('A', 'B', 3, 1),
    ('C', 'E', 1, 1),
    ('C', 'D', 1, 1),
    ('B', 'E', 3, 1),
    ('B', 'D', 1, 1),
    ('E', 'D', 3, 0),
    ('E', 'F', 1, 1),
    ('D', 'F', 5, 2)
]

source1 = 'A'
sink1 = 'F'
flow1 = 4

mat = Maximum_flow(edges1, source1, sink1, flow1)
conservation1 = np.array(mat[0])
sinks1 = np.array(mat[1])
capacity1 = np.array(mat[2])
cost = np.array(mat[3])

b_eq = np.array([0]*(conservation1.shape[0]-1) + [flow1])
bounds = [(0, cap) for cap in capacity1]

res1 = linprog(cost,
               A_eq=conservation1,
               b_eq=b_eq,
               bounds=bounds,
               method="highs")

print(res.fun)
print(res1.x)
print(res1.fun)