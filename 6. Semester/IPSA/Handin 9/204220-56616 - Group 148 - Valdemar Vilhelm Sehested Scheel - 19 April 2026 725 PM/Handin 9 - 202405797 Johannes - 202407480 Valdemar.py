"""
Handin 9 (maximum flow)

Hards parts:
    We found it a bit hard at first to find out the best implementation of the 
    algorithm changing the edges layout of the problem into the one we can use
    for the linprog-function. When the implementation choices were taken, it
    was quite straightforward. The next hard part was wrapping our heads around
    how the flow constraint in b) should be implemented, but when we understood
    that, it was quite straightforward to find the minimal cost using the code
    from a).
"""
import numpy as np
from scipy.optimize import linprog


def edges_to_setup(edges, source, sink):
    number_of_unknowns = len(edges)
    
    capacity = np.zeros(number_of_unknowns)
    sinks = np.zeros(number_of_unknowns)
    conservation = []
    non_sink_or_source_nodes = dict()
    
    for index, edge in enumerate(edges):
        capacity[index] = edge[2]
        
        
       # Adds non-source and non-sink node to the conservation array
        if edge[1] != sink and edge[1] not in non_sink_or_source_nodes.keys():
            non_sink_or_source_nodes[edge[1]] = len(conservation)
            conservation.append([0 for i in range(number_of_unknowns)])
            
        if edge[0] != source and edge[0] not in non_sink_or_source_nodes.keys():
            non_sink_or_source_nodes[edge[0]] = len(conservation)
            conservation.append([0 for i in range(number_of_unknowns)])
            
        
        # Puts in the constrains in the conservation array
        if edge[0] != source:
           conservation_index = non_sink_or_source_nodes[edge[0]]
           conservation[conservation_index][index] = 1
        
        if edge[1] == sink:
            sinks[index] = 1 
        
        else:
            conservation_index = non_sink_or_source_nodes[edge[1]]
            conservation[conservation_index][index] = -1
    
    conservation = np.array(conservation)    
    print(conservation)
    res = linprog(-sinks, 
                  A_eq=np.array(conservation), 
                  b_eq=np.zeros(conservation.shape[0]), 
                  A_ub=np.eye(capacity.size), 
                  b_ub=capacity)
    
    return res

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

sol = edges_to_setup(edges, source, sink)

print(sol.fun)

# b)
def minimal_flow_cost(edges, source, sink, flow):
    number_of_unknowns = len(edges)
         
    cost = []
    capacities = []
    sinks = [0 for i in range(number_of_unknowns)]
    conservation = []
    non_sink_or_source_nodes = dict()
         
         
    for index, edge in enumerate(edges):
        capacities.append(edge[2])
        cost.append(edge[3])
             
             
        # Adds non-source and non-sink node to the conservation array
        if edge[1] != sink and edge[1] not in non_sink_or_source_nodes.keys():
            non_sink_or_source_nodes[edge[1]] = len(conservation)
            conservation.append([0 for i in range(number_of_unknowns)])
                 
        if edge[0] != source and edge[0] not in non_sink_or_source_nodes.keys():
            non_sink_or_source_nodes[edge[0]] = len(conservation)
            conservation.append([0 for i in range(number_of_unknowns)])
                 
             
        # Puts in the constrains in the conservation array
        if edge[0] != source:
            conservation_index = non_sink_or_source_nodes[edge[0]]
            conservation[conservation_index][index] = 1
             
        if edge[1] == sink:
            sinks[index] = 1 
             
        else:
            conservation_index = non_sink_or_source_nodes[edge[1]]
            conservation[conservation_index][index] = -1
         
    b = [0 for i in range(len(conservation))] + [flow]
    A = conservation.copy()
    A.append(sinks)
    res = linprog(cost, 
                  A_eq=np.array(A), 
                  b_eq=np.array(b), 
                  A_ub=np.eye(len(capacities)), 
                  b_ub=capacities)
                     
    return res.fun, res.x
    
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

min_cost, cost_eff_flow  = minimal_flow_cost(edges, source, sink, flow)

print(f'The minimum cost of a flow of {flow} is {min_cost:0.0f}')
       
            























