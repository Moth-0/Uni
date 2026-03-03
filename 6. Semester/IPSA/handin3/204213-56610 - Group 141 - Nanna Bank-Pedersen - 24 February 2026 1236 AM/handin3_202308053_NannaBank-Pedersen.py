'''
HANDIN 3 (triplet distance - part I)

This handin is done by:
    202308053 Nanna Bank-Pedersen

Reflection upon solution:
The hardest part was understanding how to generate all canonical triplets correctly, and how to use
list comprehensions for combining elements, also string slicing and comparisons. I assumed that 
labels are in "L<number>" format. The code may be slow for very large lists. I also found the permute
task a bit difficult to solve in the beginning.
'''
from random import randint

# Generate labels function
def generate_labels(n):
    return [f"L{i+1}" for i in range(n)]

# Permute function
def permute(L):
    remaining = L[:]
    result = []

    while remaining:
        i = randint(0, len(remaining) - 1)
        result.append(remaining[i])
        remaining.pop(i)
    
    return result

            #n = randint(2, 8)
            #L = generate_labels(n)

            #print(L)
            #print(permute(L))

# Pairs function
def pairs(L):
    def label_number(x):
        return int(x[1:])
    
    result = []
    for a in L:
        for b in L:
            if a < b:
                result.append((a,b))
    return result

            #print(pairs(L))

# Canonical triplets function
def canonical_triplets(A, B):
    B_pairs = pairs(B)
    triplets = []
    for a in A:
        for pair in B_pairs:
            triplets.append((a, pair))
    return triplets

            #A = ['L1', 'L2']
            #B = ['L3', 'L4', 'L5']

            #triplets = canonical_triplets(A, B)
            #print(triplets)

# Anchored triplets function
def anchored_triplets(L, R):
    triplets = []
    R_pairs = pairs(R)
    for leaf in L:
        for pair in R_pairs:
            triplets.append((leaf, pair))
    
    L_pairs = pairs(L)
    for leaf in R:
        for pair in L_pairs:
            triplets.append((leaf, pair))

    return triplets

            #L = ['L1', 'L6', 'L2']
            #R = ['L4', 'L3', 'L5']

            #result = anchored_triplets(L, R)
            #print(result)

