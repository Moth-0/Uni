'''
HANDIN 4 (Triplet distance - part II)

This handin is done by Mathias Lystlund, id: 202408483

Reflection upon solution:

I implemented recursive algorithms to construct random binary trees, generate canonical triplets,
and compute triplet distance. A key implementation decision was to clearly separate the base case (leaf nodes) 
from the recursive case, which made the structure of the solution more transparent. The most challenging part 
was understanding how triplets are anchored at each internal node and ensuring they were represented 
canonically for correct comparison. The order of tree sizes that can be handled in a reasonable time with
my code is in the hundred, more specifically 300-400 and then the time increases with n^3.
'''

## Task A
import random

L = ['A', 'B', 'C', 'D', 'E', 'F']

def generate_tree(labels):
    if len(labels) == 1:
        return labels[0]
    k = random.randint(1, len(labels)-1)
    left = labels[:k]
    right = labels[k:]
    
    tree = (generate_tree(left), generate_tree(right))
    

    return tree

tree = generate_tree(L)
print(tree)

## Task B
def generate_triplets(tree):
    if isinstance(tree, str):
        return [tree], []
    left, right = tree
    left_labels, left_triplets = generate_triplets(left)
    right_labels, right_triplets = generate_triplets(right)

    labels = left_labels + right_labels
    triplets = left_triplets + right_triplets

    
    for x in left_labels:
        for i in range(len(right_labels)):
            for j in range(i + 1, len(right_labels)):
                y, z = right_labels[i], right_labels[j]
                
                pair = (y, z) if y <= z else (z, y)
                triplets.append((x, pair))

    
    for x in right_labels:
        for i in range(len(left_labels)):
            for j in range(i + 1, len(left_labels)):
                y, z = left_labels[i], left_labels[j]
                pair = (y, z) if y <= z else (z, y)
                triplets.append((x, pair))

    return labels, triplets

print(generate_triplets(tree))

## Task C
tree1 = ((('A', 'F'), 'B'), ('D', ('C', 'E')))
tree2 = (((('D', 'A'), 'B'), 'F'), ('C', 'E'))

def triplet_distance(tree1, tree2):
    labels1, triplets1 = generate_triplets(tree1)
    labels2, triplets2 = generate_triplets(tree2)

    T1 = set(triplets1)
    T2 = set(triplets2)
    L1 = set(labels1)
    L2 = set(labels2)

    common = len(T1 & T2)
    n = len(L1 & L2)

    dis = (n*(n-1)*(n-2))/6
    return dis - common

print(triplet_distance(tree1, tree2))

'''
## Task D
def make_labels(n):
    return [f"L{i}" for i in range(n)]

H = make_labels(350)
Tree = generate_tree(H)
triplets = generate_triplets(Tree)
#print(triplets)
'''