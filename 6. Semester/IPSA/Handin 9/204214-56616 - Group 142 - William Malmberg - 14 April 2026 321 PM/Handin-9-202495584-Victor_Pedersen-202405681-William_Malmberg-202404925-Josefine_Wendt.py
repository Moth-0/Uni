'''
HANDIN 9 (maximum flow)

This handin is done by (study ids and names of up to three students):

    202405584 Victor Kvist Loft Pedersen
    202405681 William Malmberg
    202404925 Josefine Ella Luci Sandy Dorothea Wendt

    Reflections upon solutions
    The most difficult part of the handin was figure out how to fill the conservation table. 
    We found a solution where we used the set class to find all pipes that was not sink nor source.
    From there we had to realize that if the nod was in the first index of the edge tuple then we should put a +1 in the 
    table and if it was in the second index it sould be a -1.

    To solve the second part of the exercise we had to figure out how to add the new condition to the ones from before.
    Also what function should be minimized.
'''

import numpy as np
from scipy.optimize import linprog

def max_flow(edges: list, source: str, sink: str):
    capacity = np.array([cap for _, _, cap in edges])
    sinks = np.where(np.array(edges).T[1] == sink, 1, 0)

    letters = {letter for letter, _, _ in edges}
    letters = letters & {letter for _, letter, _ in edges}
    letters = sorted(letters)

    # Fill conservation table
    conservation = np.zeros((len(letters), len(edges)))
    for i, letter in enumerate(letters):
        for j, edge in enumerate(edges):
            if edge[0] == letter:
                conservation[i][j] = 1
            elif edge[1] == letter:
                conservation[i][j] = -1

    sol = linprog(-sinks,
                  A_eq=conservation,
                  b_eq=np.zeros(conservation.shape[0]),
                  A_ub=np.eye(capacity.size),
                  b_ub=capacity
    )
    assert sol.success, "Could not solve"
    return -sol.fun

def min_cost(edges: list, source: str, sink: str, flow:int):
    capacity = np.array([cap for _, _, cap, _ in edges])
    sinks = np.where(np.array(edges).T[1] == sink, 1, 0)

    letters = {letter for letter, _, _, _ in edges}
    letters = letters & {letter for _, letter, _, _ in edges}
    letters = sorted(letters)

    # Fill conservation table
    conservation = np.zeros((len(letters), len(edges)))
    for i, letter in enumerate(letters):
        for j, edge in enumerate(edges):
            if edge[0] == letter:
                conservation[i][j] = 1
            elif edge[1] == letter:
                conservation[i][j] = -1
            else:
                conservation[i][j] = 0

    sol = linprog(np.array(edges).T[3],
                  A_eq=np.append(conservation, [sinks],axis=0),
                  b_eq=np.append(np.zeros(conservation.shape[0]), flow),
                  A_ub=np.eye(capacity.size),
                  b_ub=capacity
    )
    assert sol.success, "Could not solve"
    return sol.fun

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

print(max_flow(edges, source, sink))

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

print(min_cost(edges, source, sink, flow))