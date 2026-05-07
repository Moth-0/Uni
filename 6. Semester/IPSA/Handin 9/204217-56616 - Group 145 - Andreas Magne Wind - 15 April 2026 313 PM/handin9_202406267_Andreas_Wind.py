'''
HANDIN 9 (maximum flow)

This handin is done by (study ids and names of up to three students):

    202406267 Andreas Wind

Reflection upon solution:

    Det er helt klart ikke den mest optimale måde jeg har løst opgaven
    på, men den er da løst.
    Jeg har nok for mange loops, men det var fordi jeg syntes at det var
    en svær opgave, så jeg delte den op i flere mindre opgaver.
    I del b) af opgaven kopierede jeg en del kode fra del a), men måske 
    kunne man have gjort det på en mere clean måde ved at bygge det op 
    fra bunden igen.
    

'''

import numpy as np
from scipy.optimize import linprog


def find_maximum_flow(edges, source, sink):

    # konverter

    length = len(edges)
    

    # laver capacity-vektoren med 0'er. Tallene kommer ind senere.

    capacity = np.zeros(length)
    

    # udtrækker array af nodes fra edges

    nodes = np.array([])
    for edge in edges:
        
        if edge[0] not in nodes:
            nodes = np.append(nodes, edge[0])

        if edge[1] not in nodes:
            nodes = np.append(nodes, edge[1])

    nodes = np.sort(nodes)
    

    # finder hvilke nodes der ikke er source eller sink
    intern_nodes = np.array([])
    for node in nodes:
        if node != sink and node != source:
            intern_nodes = np.append(intern_nodes, node)
    
    intern_nodes = np.sort(intern_nodes)

    # laver conservation array

    conservation = np.zeros((len(intern_nodes), length))

    sinks = np.zeros(length)

    for i, edge in enumerate(edges):
        f, t, cap = edge

        if f in intern_nodes:
            loc = np.where(intern_nodes == f)
            conservation[loc[0][0], i] = 1
        
        if t in intern_nodes:
            loc = np.where(intern_nodes == t)
            conservation[loc[0][0], i] = -1

        # laver sinks
        if t == sink:
            sinks[i] = 1
        
        capacity[i] = cap

    # hvis man vil tjekke arrays:

    #print(conservation)
    #print(sinks)
    #print(capacity)

    res = linprog(-sinks,
                  A_eq = conservation,
                  b_eq = np.zeros(conservation.shape[0]),
                  A_ub = np.eye(capacity.size),
                  b_ub = capacity)
    
    return res.x



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

result = find_maximum_flow(edges, source, sink)

print(result)


# b

def find_flow(edges, source, sink, flow):

    # konverter

    length = len(edges)
    

    # laver capacity-vektoren med 0'er. Tallene kommer ind senere.

    capacity = np.zeros(length)

    costs = np.zeros(length)
    

    # udtrækker array af nodes fra edges

    nodes = np.array([])
    for edge in edges:
        
        if edge[0] not in nodes:
            nodes = np.append(nodes, edge[0])

        if edge[1] not in nodes:
            nodes = np.append(nodes, edge[1])

    nodes = np.sort(nodes)
    

    # finder hvilke nodes der ikke er source eller sink
    intern_nodes = np.array([])
    for node in nodes:
        if node != sink and node != source:
            intern_nodes = np.append(intern_nodes, node)
    
    intern_nodes = np.sort(intern_nodes)

    # laver conservation array

    conservation = np.zeros((len(intern_nodes), length))

    sinks = np.zeros(length)
    sources = np.zeros(length)

    for i, edge in enumerate(edges):
        f, t, cap, cost = edge

        if f in intern_nodes:
            loc = np.where(intern_nodes == f)
            conservation[loc[0][0], i] = 1
        
        if t in intern_nodes:
            loc = np.where(intern_nodes == t)
            conservation[loc[0][0], i] = -1

        # laver sinks
        if t == sink:
            sinks[i] = 1
        
        # laver capacity
        capacity[i] = cap

        # sources
        if f == source:
            sources[i] = 1

        costs[i] = cost


    conservation = np.vstack([conservation, sources])

    # hvis man vil tjekke arrays:

    #print(conservation)
    #print(sinks)
    #print(capacity)

    res = linprog(costs,
                  A_eq = conservation,
                  b_eq = np.append(np.zeros(len(intern_nodes)), flow),
                  A_ub = np.eye(capacity.size),
                  b_ub = capacity)
    
    return res.fun


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

result_b = find_flow(edges, source, sink, flow)

print(result_b)