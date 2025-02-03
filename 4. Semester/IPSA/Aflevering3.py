"""
HANDIN 2 (palindrome)

This handin is done by: 
    202307989 Mikkel Moth Billing 

Reflection upon solution: 
    I'm not sure about the effeciency of my pairs function. Maybe there is  a way without using to for loops, 
    but im not sure. In e, I'm not sure if I understood the question right, but i got 18 elements, like specified
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
    pair = []
    for i in range(len(L)):             # For each element in L
        for j in range(i+1, len(L)):    # For each element after i
            pair.append((L[i], L[j]))   # Add the tuple to the list
    return pair

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