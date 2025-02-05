"""
HANDIN 3 - Triplet distance part 1

This handin is done by: 
    202307989 Mikkel Moth Billing 

Reflection upon solution: 
    At first i made the pair function with two for nested for loops, but i rewrote it to be in one line, 
    i dont know what is faster, but it looks nicer this way. 
    In e, I'm not sure if I understood the question right, but i got 18 elements, like specified
    in the description. Otherwise i think my solution is correct and well explained. 
"""

# a
def generate_labels(n):
    return [chr(l) for l in range(65, 65+n)] # chr(n) gives the ASCII character of n A-Z is 65-90

print("a: ", generate_labels(5))

# b
from random import randint

def permute(L): 
    perm = []
    for i in range(len(L)): 
        n = randint(0, len(L)-1)    # Select random index of L
        perm.append(L[n])           # Add that element of L to perm
        L.remove(L[n])              # Remove that element from L so it is not picked again
    return perm

print("b: ", permute(generate_labels(5)))

# c 
def pairs(L):
    return [(L[i], L[j]) for i in range(len(L)) for j in range(i+1, len(L))]
    # For each element in L, for each element after i, add the tuple to the list
    # Done in one line instead of two for loops

print("c: ", pairs(generate_labels(3)))

# d 
def canonical_triplets(A, B): 
    B_pairs = pairs(B)                  # Get all pairs of B
    triplets = []
    for a in A:                         # For each element in A
        for b in B_pairs:               # For each pair in B
            triplets.append((a, b))     # Add the triplet to the list
    return triplets

print("d: ", canonical_triplets(generate_labels(2), generate_labels(3)))

# e 
def anchored_triplets(L, R): 
    L_triplets = canonical_triplets(L, R) # Get all triplets with L as the anchor
    R_triplets = canonical_triplets(R, L) # Get all triplets with R as the anchor
    return L_triplets + R_triplets        # Return the concatenation of the two lists

print("e: ", anchored_triplets(generate_labels(3), ["D", "E", "F"]))