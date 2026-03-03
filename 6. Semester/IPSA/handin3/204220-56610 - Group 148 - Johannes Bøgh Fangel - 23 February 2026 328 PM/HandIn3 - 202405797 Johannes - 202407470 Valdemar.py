#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HANDIN 3 (triplet distance - part I)

This handin is done by:

    202405797 Johannes Bøgh Fangel
    202407470 Valdemar Scheel

Reflection upon solution:
    In the implementation of the generate labels function you could also do it using a dictionary of acceptable labels,
    and then loop through that dictionary to create the list of labels of a given length. Using the function chr() 
    you can do this in a quite simpler way as seen in our implementation.
    
    
    To implement the pairs function we used a list comprehension looping thorugh the list of labels creating tuples w
    ith the pairs. The if-statement makes sure that we don't create pairs where the two labels are the same, make pairs 
    that always have the alphabetically first come letter as the first letter of the tuple. At the same time this also 
    make sure that we don't make two pairs that are the same.
    
    In the implementation  of the cannonical triplets function we used the pairs list to create all the pairs of the
    list B and then a list comprehension to pair up all the pairs of B with a label from A in a tuple.
"""
from random import randint

# a
def generate_labels(n: int):
    return [chr(65 + i) for i in range(n)]

L = generate_labels(5.0)


# b
def permute(L: list):
    L_permutted = []
    L_copy = L[:]
    while len(L_permutted) < len(L):
        i = randint(0, len(L_copy)-1)
        L_permutted.append(L_copy[i])
        L_copy.remove(L_copy[i])
    return L_permutted

permute(['A', 'B', 'C'])

# c
def pairs(L: list):
    return [tuple([L[i], L[j]]) for i in range(len(L)) for j in range(len(L)) if L[i] < L[j]]

pairs(['A', 'F', 'B'])

# d
def canonical_triplets(A: list, B: list):
    B_pairs = pairs(B)
    return [tuple([a, B_pair]) for a in A for B_pair in B_pairs]
                  
canonical_triplets(['A', 'B'], ['C', 'D', 'E'])

# e
def anchored_triplets(L: list, R: list):
    return canonical_triplets(L, R) + canonical_triplets(R, L)

anchored_triplets(['A', 'F', 'B'], ['D', 'C', 'E'])




# Alternative Approach 

#a --------------------
def generate_labels(n):
    labels = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6}
    return [label for label, position in labels.items() if position <= n<= 6]
    #I could add an if and else to secure the values of n
L = generate_labels(5)

#b --------------------
from random import randint
def permute(L):
    remaining_elements_in_L = L.copy()
    permuted_L = []
    while len(remaining_elements_in_L) > 0:
        random_index_in_Rem_L = randint(0,len(remaining_elements_in_L)-1)
        element_taken_out_of_Rem_L = remaining_elements_in_L.pop(random_index_in_Rem_L)
        permuted_L.append(element_taken_out_of_Rem_L)
    return permuted_L
permute(L)

# c --------------------
n = 5
L = generate_labels(n)
L = permute(L)
print(L)
def pairs(L):
    pos_tracker = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6}
    raw_combinations = [(a,b) for _ in L 
                    for a in L 
                    for b in L 
                    if (pos_tracker[str(a)] < pos_tracker[str(b)])]
    filtered_combinations = list(set(raw_combinations))
    # This last step is a bit like going from combinatoric to permutation, in a way. But not really. 
    # Because of the way my two loops are set up. There will be duplicates like, ('A','C') and ('A','C')
    # set() collects the duplicates in one entry, and then we make that into the new list.
    return filtered_combinations

print(pairs(L))

#d --------------------
def canonical_triplets(A, B):
    return [(a,(B1,B2)) for a in A for B1 in B for B2 in B if B1 < B2]

canonical_triplets(['A', 'B'], ['C', 'D', 'E'])

#e --------------------
def anchored_triplets(L, R):
    return canonical_triplets(L, R) + canonical_triplets(R,L)

anchored_triplets(['A', 'B'], ['C', 'D', 'E'])