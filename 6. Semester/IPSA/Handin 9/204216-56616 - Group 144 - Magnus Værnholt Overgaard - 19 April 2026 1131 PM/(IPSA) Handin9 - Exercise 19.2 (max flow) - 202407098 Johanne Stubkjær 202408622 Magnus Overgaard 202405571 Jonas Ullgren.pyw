"""
HANDIN 9 

This handin is done by:

202407098 Johanne Stubkjær
202408622 Magnus Overgaard
202405571 Jonas Ullgren

Reflection upon solution:

The biggest part was keeping track of shapes, axis, and what type of object we were working with. We had to make some design decisions regarding how we wanted to split the first part (a) of the code up into functions while at the same time keeping part (b) in mind (so we could reuse as much as posible). It took a really long time to figure out how we should include the x7+x8=flow constraint. Maybe some intuition and understanding of .linprog() could've helped us here. Oh well - We got the gist of it, kind of. 
"""


import numpy as np
from scipy.optimize import linprog


# Part a)

edges = [
    ('A', 'C', 4), #x0
    ('A', 'B', 3), #x1
    ('C', 'E', 1), #x2
    ('C', 'D', 1), #x3
    ('B', 'E', 3), #x4
    ('B', 'D', 1), #x5
    ('E', 'D', 3), #x6
    ('E', 'F', 1), #x7
    ('D', 'F', 5) #x8
]

source = 'A'
sink = 'F'

def handle_input(edges, source, sink):
    nodes = []

    capacity = []
    sinks = np.zeros(len(edges))

    for edge in range(len(edges)): # 0, 1, ... , 8
        capacity.append(edges[edge][2])

        if edges[edge][1] == sink:
            sinks[edge] = 1
        
        nodes.append(edges[edge][0])
        nodes.append(edges[edge][1])

    nodes = sorted(set(nodes))
    n_nodes = len(nodes)

    nodes.remove(sink)
    nodes.remove(source)  

    capacity = np.array(capacity)
    sinks = np.array(sinks)

    return nodes, capacity, sinks


def conservat(edges, nodes):

    conservation = np.zeros([len(nodes), len(edges)])

    row = 0
    for node in nodes: #B,C,D,E
        col = 0
        for list in edges: #
            if list[0] == node:
                conservation[row, col] = 1
            if list[1] == node:
                conservation[row, col] = -1
            col += 1
        row+=1

    return conservation

# print(capacity)
# print(sinks)
# print(conservation)

nodes, capacity, sinks = handle_input(edges, source, sink)
conservation = conservat(edges, nodes)

res = linprog(-sinks, 
              A_eq=conservation,
              b_eq=np.zeros(conservation.shape[0]),
              A_ub=np.eye(capacity.size),
              b_ub=capacity)

print(res.fun)



# Part b)
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

def capitalism(edges):
    costs = []

    for edge in edges: 
        costs.append(edge[3])

    return costs

nodes, capacity, sinks = handle_input(edges, source, sink)
costs = np.array(capitalism(edges))

conservation = conservat(edges, nodes)
conservation = np.append(conservation, [sinks], axis=0)


beq = np.zeros(conservation.shape[0])
beq[-1] = flow

res = linprog(costs, 
              A_eq=conservation,
              b_eq=beq,
              A_ub=np.eye(capacity.size),
              b_ub=capacity)

print(res.fun)