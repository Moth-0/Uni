"""
This is done by :
748507 Kristian Milla

Reflection upon solution:
Jeg havde generelt svært ved opgaven og fik hjælp af AI.
Den største udfordring var at automatisere opbygningen 
af A_eq-matricen, så loven om flow-bevarelse (flow ind = flow ud) overholdes for alle knuder 
undtagen kilde og dræn. Jeg valgte at bruge loops til at gennemløbe lister over kanter og knuder, 
hvilket gør koden fleksibel over for forskellige grafer. En begrænsning ved løsningen er, 
at den antager, at grafen er orienteret (directed). Ved at benytte 'bounds' til kanternes 
kapacitet i stedet for at tilføje dem som uligheder i A_ub, blev koden væsentligt mere 
overskuelig og lettere at implementere.
"""

import numpy as np
from scipy.optimize import linprog

# Datarepræsentation: (fra, til, kapacitet)
edges_a = [
    ('A', 'C', 4), ('A', 'B', 3), ('C', 'E', 1),
    ('C', 'D', 1), ('B', 'E', 3), ('B', 'D', 1),
    ('E', 'D', 3), ('E', 'F', 1), ('D', 'F', 5)
]
source_a = 'A'
sink_a = 'F'

# Find alle unikke knuder
nodes_a = sorted(list(set([e[0] for e in edges_a] + [e[1] for e in edges_a])))

# 1. c: Vi vil maksimere flow ud af source. 
# Da linprog minimerer, sætter vi -1 for alle kanter, der starter i 'source'
c_a = [(-1 if e[0] == source_a else 0) for e in edges_a]

# 2. A_eq og b_eq: Flow-bevarelse (flow ind = flow ud)
A_eq_a = []
b_eq_a = []

for node in nodes_a:
    if node == source_a or node == sink_a:
        continue
    row = []
    for u, v, cap in edges_a:
        if v == node:   # Flow ind i knuden
            row.append(1)
        elif u == node: # Flow ud af knuden
            row.append(-1)
        else:
            row.append(0)
    A_eq_a.append(row)
    b_eq_a.append(0)

# 3. Bounds: Flow på hver kant er begrænset af [0, kapacitet]
bounds_a = [(0, cap) for u, v, cap in edges_a]

# Løs programmet
res_a = linprog(c_a, A_eq=A_eq_a, b_eq=b_eq_a, bounds=bounds_a)

print(f"--- Opgave 19.2 (a) Maximum Flow ---")
print(f"Maksimalt flow fra {source_a} til {sink_a}: {-res_a.fun:.2f}\n")


#19.2b

# Datarepræsentation: (fra, til, kapacitet, omkostning)
edges_b = [
    ('A', 'C', 4, 1), ('A', 'B', 3, 1), ('C', 'E', 1, 1),
    ('C', 'D', 1, 1), ('B', 'E', 3, 1), ('B', 'D', 1, 1),
    ('E', 'D', 3, 0), ('E', 'F', 1, 1), ('D', 'F', 5, 2)
]
source_b = 'A'
sink_b = 'F'
target_flow = 4

nodes_b = sorted(list(set([e[0] for e in edges_b] + [e[1] for e in edges_b])))

# 1. c: Minimér samlede omkostninger (flow * omkostning per enhed)
c_b = [e[3] for e in edges_b]

A_eq_b = []
b_eq_b = []

# 2. Flow-bevarelse for alle knuder undtagen source og sink
for node in nodes_b:
    if node == source_b or node == sink_b:
        continue
    row = []
    for u, v, cap, cost in edges_b:
        if v == node: row.append(1)    # Ind
        elif u == node: row.append(-1) # Ud
        else: row.append(0)
    A_eq_b.append(row)
    b_eq_b.append(0)

# 3. Constraint: Det samlede flow ud af source SKAL være lig med target_flow (4)
source_flow_row = []
for u, v, cap, cost in edges_b:
    if u == source_b:
        source_flow_row.append(1)
    else:
        source_flow_row.append(0)
A_eq_b.append(source_flow_row)
b_eq_b.append(target_flow)

# 4. Bounds: Flow på hver kant mellem 0 og kapacitet
bounds_b = [(0, e[2]) for e in edges_b]

# Løs programmet
res_b = linprog(c_b, A_eq=A_eq_b, b_eq=b_eq_b, bounds=bounds_b)

print(f"--- Opgave 19.2 (b) Minimum Cost Flow ---")
if res_b.success:
    print(f"Minimum omkostning for flow på {target_flow}: {res_b.fun:.2f}")
    # Vis hvilke stier der bruges
    for i, edge in enumerate(edges_b):
        if res_b.x[i] > 0:
            print(f"  Kant {edge[0]}->{edge[1]}: Sender {res_b.x[i]:.1f} enheder")