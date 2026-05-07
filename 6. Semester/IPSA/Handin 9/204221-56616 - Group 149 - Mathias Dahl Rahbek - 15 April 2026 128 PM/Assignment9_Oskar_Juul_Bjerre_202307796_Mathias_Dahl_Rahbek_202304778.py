'''
HANDIN 9 (maximal flow)

202307796 Oskar Juul Bjerre
202304778 Mathias Dahl Rahbek

Reflection upon solution:
We spent a long time finding all the internal nodes generally. We know a better
solution exists, but we decided not to spend more time finding it, since our
solution already works. Numpy could have been used more and would maybe also
provide a better solution to finding the internal nodes. We used np.unstack to
unpack each column in the edges list, concerting it to an np.array.
'''
import numpy as np
from scipy.optimize import linprog
# a)

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

conservation = []

nodes = []
for x, y, _ in edges:
    if x not in set(nodes):
        nodes.append(x)

    if y not in set(nodes):
        nodes.append(y)

nodes.remove(source)
nodes.remove(sink)

for node in nodes:
    row = [0] * len(edges)
    for i, quartet in enumerate(edges):
        if node == quartet[0]:
            row[i] = 1
        elif node == quartet[1]:
            row[i] = -1
    conservation.append(row)

conservation = np.array(conservation)

sinks = np.zeros(len(edges))
for i, quartet in enumerate(edges):
    if quartet[1] == sink:
        sinks[i] = 1

capacity = np.array([triplet[-1] for triplet in edges])

res = linprog(-sinks,
              A_eq=conservation,
              b_eq=np.zeros(conservation.shape[0]),
              A_ub=np.eye(capacity.size),
              b_ub=capacity)
print(res)
print('Maximal flow =', -res.fun)
print('Maximal solution =', res.x)

# b)
edges = [
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

source = 'A'
sink = 'F'
flow = 4

conservation = []

nodes = []
for x, y, _, _ in edges:
    if x not in set(nodes):
        nodes.append(x)

    if y not in set(nodes):
        nodes.append(y)

nodes.remove(source)
nodes.remove(sink)

for node in nodes:
    row = [0] * len(edges)
    for i, quartet in enumerate(edges):
        if node == quartet[0]:
            row[i] = 1
        elif node == quartet[1]:
            row[i] = -1
    conservation.append(row)

edges = np.array(edges)
edges_unpacked = np.unstack(edges, axis = 1)

cost = edges_unpacked[-1]

row = [0]*len(edges)
for i, node in enumerate(edges_unpacked[1]):
    if node == sink:
        row[i] = 1
conservation.append(row)

conservation = np.array(conservation)

b_eq = np.zeros(conservation.shape[0])
b_eq[-1] = flow

capacity = edges_unpacked[-2]

res = linprog(cost,
              A_eq=conservation,
              b_eq=b_eq,
              A_ub=np.eye(capacity.size),
              b_ub=capacity)
print(res)
print('Minimal cost =', res.fun)
print('Solution =', res.x)