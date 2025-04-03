"""
HANDIN 9 - Maximum Flow

This handin is done by: 
    202307989 Mikkel Moth Billing 

Reflection upon solution: 
    I used most of the time to find out how to make the convert function, i think there is a better way, 
    but the if else statement works. I think my solution is good, but i'm not sure how to test for other 
    scenarios, since i don't know what the answer should be. 
"""

# Imports
import numpy as np 
from scipy.optimize import linprog

# a
a_edges = [
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

a_source = 'A'
a_sink = 'F'

def convert(edges, source, sink):
    # Make a list of the othe node names 
    nodes = list(set([node for edge in edges for node in edge[:2]]))
    nodes.remove(source)
    nodes.remove(sink)

    # Make the conservation array by checking if the edge goes from or to the source or sink, 
    # and if not find where it goes from and to. 
    conservation = []
    for edge in edges: 
        idx = np.zeros(len(nodes))
        
        if edge[0] == source: 
            idx[nodes.index(edge[1])] = -1
        
        elif edge[1] == sink: 
            idx[nodes.index(edge[0])] = 1
        
        else: 
            idx[nodes.index(edge[0])] = 1
            idx[nodes.index(edge[1])] = -1
        
        conservation.append(idx) # Append result of every edge

    conservation = np.array(conservation).T # Transpose

    # Make sink array
    sinks = np.array([1 if edge[1] == sink else 0 for edge in edges])

    # Extract capacity array
    capacity = np.array([x[2] for x in edges])

    return (conservation, sinks, capacity)

conservation, sinks, capacity = convert(a_edges, a_source, a_sink)

# Find maximum flow
res = linprog(-sinks, 
                A_eq=conservation,
                b_eq=np.zeros(conservation.shape[0]),
                A_ub=np.eye(capacity.size),
                b_ub=capacity)

print(f"a: \n flow: {res.x} \n")


# b
b_edges = [
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

b_source = 'A'
b_sink = 'F'
b_flow = 4

# Convert
conservation, sinks, capacity = convert(b_edges, b_source, b_sink)


# Make cost array and 
costs = np.array([x[3] for x in b_edges])

# Add a constraint that exit flow must be b_flow 
A_eq = np.vstack([conservation, sinks])
b_eq = np.append(np.zeros(conservation.shape[0]), [b_flow])

# Find minimum costs when flow is b_flow
res = linprog(costs, 
                A_eq=A_eq,
                b_eq=b_eq,
                A_ub=np.eye(capacity.size),
                b_ub=capacity)

print(f"b: \n flow: {res.x} \n cost: {np.sum(costs*res.x)}")