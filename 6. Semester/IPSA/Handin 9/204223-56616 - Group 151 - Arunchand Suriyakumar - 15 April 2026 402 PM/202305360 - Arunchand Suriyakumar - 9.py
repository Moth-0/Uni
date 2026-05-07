#%%
#Exercise 19.2 - handin 9 (maximum flow)


'''
HANDIN 9 (Handin 9 - maximum flow)

This handin is done by 
    202305360: Arunchand Suriyakumar

Reflection upon solution:
    Part A: The idea is to find the distinct letters from the output, execpt 
    sink and source, to create a list of letters between source and sink.
    Then for each letter, we check its position in each tuple in "edges". Depending
    on its postion, we know wheter its a flow in (-1) or flow out (+1). This is done
    to create the conservation matrix. The sinks-list checks how many arrows points
    to the sink. Finally, the capacity hold the information of the maximum flow capacity
    along each direction

    Part B: Similar code to A. But now we minimize the cost instead. And we add another
    constraint to the conservation such that we end with a value "flow" at the sink. 
    This then also means, that b_eq changes from being the null-vector.

'''

#%%
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


def maximum_flow(edges, source, sink):
    letters = sorted(set(x for edge in edges for x in edge[:-1] if x != source and x != sink))


    conservation = []
    capacity = []

    for letter in letters:
        row = []
        for edge in edges:
            if letter == edge[0]:
                row.append(1)
            elif letter == edge[1]:
                row.append(-1)
            else:
                row.append(0)
        conservation.append(row)

    conservation = np.array(conservation)


    sinks = np.array([1 if sink in edge else 0 for edge in edges])

    capacity = np.array([edge[-1] for edge in edges])


    res = linprog(-sinks,
        A_eq=conservation,
        b_eq=np.zeros(conservation.shape[0]),
        A_ub=np.eye(capacity.size),
        b_ub=capacity)

    return res

maximum_flow(edges, 'A', 'F')
#%%
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
def minimal_costs(edges, source, sink, flow):

    letters = sorted(set(x for edge in edges for x in edge[:-2] if x != source and x != sink))


    conservation = []
    capacity = []

    for letter in letters:
        row = []
        for edge in edges:
            if letter == edge[0]:
                row.append(1)
            elif letter == edge[1]:
                row.append(-1)
            else:
                row.append(0)
        conservation.append(row)

    extra_constraint = [1 if sink in edge else 0 for edge in edges]

    conservation.append(extra_constraint)
    b_eq = np.zeros(len(conservation))
    b_eq[-1] = flow



    costs = np.array([edge[-1] for edge in edges])

    capacity = np.array([edge[-2] for edge in edges])


    res = linprog(costs,
        A_eq=conservation,
        b_eq=b_eq,
        A_ub=np.eye(capacity.size),
        b_ub=capacity)

    return res

minimal_costs(edges, 'A', 'F', 4)
