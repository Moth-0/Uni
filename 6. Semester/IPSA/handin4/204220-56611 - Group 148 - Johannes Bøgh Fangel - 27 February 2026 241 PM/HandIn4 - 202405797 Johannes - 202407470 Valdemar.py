#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# a
"""
HANDIN 4 (triplet distance - part II)

This handin is done by:
    202405797 Johannes Bøgh Fangel
    202407470 Valdemar Scheel

Reflection upon solution:
    Implementaton: We used randomint to randomly split a list of labels into a left and right side of a tree. 
Then using recursion we could split a list of labels into a tree. To implement the recursion we sat up a base, 
so the recursion would break when a given tuple of labels were of length 1 or 2. For length 1 it would just 
return the label, and for length 2 it would return the tuple with the two labels. Else it should split the 
labels into left and right and return a tuple with the function used on left and right.

Now in the implementation of generate_triplets, we had a hard time figuring out how to make it a recursive 
function. We set the base of the function to as when the tree is a string, which would mean that it has reached
a leaf. It should then return a list with the leaf and an empty list, as a leaf has no canonical triplets. 
Otherwise it should split the tree up in a left and a right, and then use the function recursively to find the 
labels and triplets of left and right. It can then find the total labels and triplets of the tree using the 
canonical triplets function from Hand-in 3.

In the implementation of the triplet_distance function. We just used the generate_triplets function to find the
labels and triplets of the two trees. We then used set to find the common labels and triplets and the calculated
the distance using the formula.

From our timings from d) we can see that our generate triplets function is very fast. It generates trees for a
millon labels in under 10 seconds. On the other hand triplet_distance can only handle a couple of hundred labels
in under 10 seconds. This makes sense, as generate_tree calls itself one time when running. triplet_distance on 
other hand calls the generate_triplets function twice, which is also a recursive function. It therefore makes
sense that generate_tree is faster than triplet_distance. Why it is that much faster is more complex.

"""

from random import randint

# From Handin 3 
def pairs(L: list):
    return [tuple([L[i], L[j]]) for i in range(len(L)) for j in range(len(L)) if L[i] < L[j]]

def canonical_triplets(A: list, B: list):
    B_pairs = pairs(B)
    return [tuple([a, B_pair]) for a in A for B_pair in B_pairs]

def anchored_triplets(L: list, R: list):
    return canonical_triplets(L, R) + canonical_triplets(R, L)

# a
def generate_tree(labels):
    if len(labels) < 3:
        if len(labels) == 1:
            return labels[0]
        else:
            return tuple(labels)
    
    else:
        split_index = randint(1, len(labels)-1)
        left = labels[:split_index]
        right = labels[split_index:]
        return tuple([generate_tree(left), generate_tree(right)])

generate_tree(['A', 'B', 'C', 'D', 'E', 'F'])
generate_tree(['A'])
    
# b
def generate_triplets(tree):
    if isinstance(tree, str):
        return [tree], []
    
    else:
        left, right = tree
        left_labels, left_triplets = generate_triplets(left)
        right_labels, right_triplets = generate_triplets(right)
        
        labels = left_labels + right_labels
        triplets = left_triplets + right_triplets + anchored_triplets(left_labels,
            right_labels)
        return (labels, triplets)

generate_triplets(((('A', 'F'), 'B'), ('D', ('C', 'E'))))

# c
def triplet_distance(tree1, tree2):
    labels1, triplets1 = generate_triplets(tree1)
    labels2, triplets2 = generate_triplets(tree2)
    
    common_labels = set(labels1) & set(labels2)
    common_triplets = set(triplets1) & set(triplets2)
    n = len(common_labels)
    return n * (n-1) * (n-2) // 6 - len(common_triplets)

triplet_distance(((('A', 'F'), 'B'), ('D', ('C', 'E'))),
                 (((('D', 'A'), 'B'), 'F'), ('C', 'E')))

'''
# d
import time

data = []

n = 1100000
labels = [chr(i) for i in range(n)]
start = time.time()
generate_tree(labels)
end = time.time()
    
time_to_generate = end - start
print(f'Time to generate tree of {n} labels: {time_to_generate: 0.2f} s')

n = 350
labels = [chr(i) for i in range(n)]   
tree1 = generate_tree(labels)
tree2 = generate_tree(labels)
    
start = time.time()
triplet_distance(tree1, tree2)
end = time.time()
    
time_to_find_distance = end - start
print(f'Time to find triplet distance for trees of {n} labels: {time_to_find_distance: 0.2f} s')  
    
'''



