import numpy as np
from scipy.optimize import linprog

'''
HANDIN 9 (maximum flow)

This handin is done by (study ids and names of up to three students):

    202407458 Kenny Nguyen
    202408911 Safiya Chebil 
    202406237 Marie Schnoor - Madsen 

    
Reflection upon solution:

    Det store problem var at forstå matematikken bag det, og selve opgave formuleringen. F.eks hintet i b) havde vi svært ved at forstå. 
'''

#a) 
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

capacity = []
sinks = []
for i in range(len(edges)): 
    capacity.append(edges[i][2])
    if edges[i][1] == 'F': 
        sinks.append(1)
    else: 
        sinks.append(0)
sinks = np.array(sinks)
capacity = np.array(capacity)

all_nodes = []
for e in edges: 
    if e[0] not in all_nodes: 
        all_nodes.append(e[0])
    if e[1] not in all_nodes: 
        all_nodes.append(e[1])  
internal = [n for n in all_nodes if n != source and n != sink]

conservation = np.zeros((len(internal), len(edges)))

for row, node in enumerate(internal): 
    for col, (fr,to, cap) in enumerate(edges): 
        if node == fr: 
            conservation[row, col] = 1 
        if node == to: 
            conservation[row, col] = -1 
conservation = np.array(conservation)


res = linprog(-sinks, A_eq=conservation, b_eq=np.zeros(conservation.shape[0]), A_ub=np.eye(capacity.size), b_ub=capacity)
print(res.fun)
print(conservation)

#a) 
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

capacity = []
sinks = []
for i in range(len(edges)): 
    capacity.append(edges[i][2])
    if edges[i][1] == 'F': 
        sinks.append(1)
    else: 
        sinks.append(0)
sinks = np.array(sinks)
capacity = np.array(capacity)

all_nodes = []
for e in edges: 
    if e[0] not in all_nodes: 
        all_nodes.append(e[0])
    if e[1] not in all_nodes: 
        all_nodes.append(e[1])  
internal = [n for n in all_nodes if n != source and n != sink]

cost_vec = [edges[n][3] for n in range(len(edges))]

conservation = np.zeros((len(internal), len(edges)))
for row, node in enumerate(internal): 
    for col, (fr,to, cap, cost) in enumerate(edges): 
        if node == fr: 
            conservation[row, col] = 1 
        if node == to: 
            conservation[row, col] = -1 
conservation = np.array(conservation)


res = linprog(cost_vec, A_eq=np.vstack([conservation, sinks]), b_eq=np.append(np.zeros(conservation.shape[0]), flow), A_ub=np.eye(capacity.size), b_ub=capacity)
print(res.fun)