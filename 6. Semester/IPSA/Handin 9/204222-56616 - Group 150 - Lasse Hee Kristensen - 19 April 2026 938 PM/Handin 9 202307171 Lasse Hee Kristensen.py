#%%
'''
I den første opgave kigger vi kun på nodes mellem source og sink, dvs.
[B, C, D, E], og vi har en 4x9 matrix, der sørger for flow bevares igennem hver node.
Conservation matricen bygges ved at tjekke hver node for dens in og outflow og
tildele 1 for hvert outlfow og -1 for hvert inflow.

Vi bygger på samme måde b_upperbound ved at tjekke capacities for hver edge,
og b_eq ved at indsætte 0'er svarenede højresiden af hver række i conservation matricen.
Sinks finder de flows, x_i, x_j, der går i sink og sætter dem til 1, og resten til 0.
Alting passes til linprog() og vi får et flow på 5 som det maksimale.

Anden opgave følger samme form, men kræver nu et bestemt flow ind og ud af soruce og sink.
Dvs. to rækker tilføjes til conservation matricen og derudover hentes cost per flow
fra hver edge og vi minimerer nu i linprog() costs @ x, som er summen for et givet flow.
b_eq tilføjes 4 og -4 som svarer til ønsket flow fra source -> sink.

'''

#a)
import numpy as np
from scipy.optimize import linprog

#(from, to, capacity)
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

def maxium_flow(source, sink, edges):
    nodes_num = np.abs(ord(source)-ord(sink))
    letters = [chr(ord(source)+i) for i in range(1, nodes_num)]

    conservation = []
    for letter in letters:
        row = []
        for tuple in edges:
            if letter == tuple[0]:
                row.append(1)
            elif letter == tuple[1]:
                row.append(-1)
            else:
                row.append(0)
        conservation.append(row)

    capacity = [edge[-1] for edge in edges]
    sinks = [1 if sink in tuple else 0 for tuple in edges]
    conservation = np.array(conservation)

    sinks = np.array(sinks)
    capacity=np.array(capacity)

    res = linprog(-sinks,
            A_eq=conservation,
            b_eq=np.zeros(conservation.shape[0]),
            A_ub=np.eye(capacity.size),
            b_ub=capacity)
    
    return res

maxium_flow(source, sink, edges)


# %% #b)

#fjerde kolonne repræsenterer nu prisen per flowenhed gennem hver edge
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

def minimal_cost(source, sink, edges, desired_flow):
    nodes_num = np.abs(ord(source)-ord(sink))
    #inkluder source og sink rækkerne i coservation matricen
    letters = [chr(ord(source)+i) for i in range(0, nodes_num+1)]
    #letters = [A, B, C, D, E, F]
    conservation = []
    
    #conservation conservation
    for letter in letters:
        row = []
        for tuple in edges:
            if letter == tuple[0]:
                row.append(1)
            elif letter == tuple[1]:
                row.append(-1)
            else:
                row.append(0)
        conservation.append(row)

    capacity = [edge[2] for edge in edges]
    costs = [edge[3] for edge in edges]

    conservation = np.array(conservation)
    capacity = np.array(capacity)

    b_eq = np.zeros(conservation.shape[0])
    b_eq[-1] = -desired_flow #outflow fra sink
    b_eq[0] = desired_flow #inflow til source

    #find vektoren x der minimerer c*x = [c1, c2, ..., cn]*[flow1, flow2, ..., flown]
    res = linprog(costs,
            A_eq=conservation,
            b_eq=b_eq,
            A_ub=np.eye(capacity.size),
            b_ub=capacity)
    
    return res

minimal_cost(source, sink, edges, flow)

# %%
