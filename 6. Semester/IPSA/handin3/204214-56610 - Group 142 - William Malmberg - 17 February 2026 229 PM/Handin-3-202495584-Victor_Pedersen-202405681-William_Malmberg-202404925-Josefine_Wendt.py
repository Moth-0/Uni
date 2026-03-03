'''
HANDIN 3 (Triplet Distance part I)

This handin is done by (study ids and names of up to three students):

    202405584 Victor Kvist Loft Pedersen
    202405681 William Malmberg
    202404925 Josefine Ella Luci Sandy Dorothea Wendt

Reflection upon solution:
 When writing the more complicated functions we always kept in mind if we could use previous functions
 to make our lives easier.
 We also discussed if we should just permute the list being inputted into the function, but we chose not to 
 to prevent unintended sideeffects on the user side, or in one word "encapsulation".

 We have also unlocked true compact ecstasy by using list comprehensions instead of for loops..
'''
from random import randint

def generate_labels(n):
    return list(map(chr, range(65, 65+n)))

def permute(L):
    _L = L[:] # This step prevents permuting the original list
    perm = [] # Placeholder list for the permutation
    while _L != []: # While list not empty
        idx = randint(0, len(_L)-1) # Choose random idx
        perm.append(_L.pop(idx)) # Extract random entry and add to perm
    return perm

def pairs(L):
    _L = sorted(L)
    pair_list = [(_L[i], _L[j]) for i in range(len(_L)-1) for j in range(i+1, len(_L)) if i != j]
    return pair_list

def canonical_triplets(A, B):
    B_pairs = pairs(B)
    return [(A[i], B_pairs[j]) for i in range(len(A)) for j in range(len(B_pairs))]

def anchored_triplets(L, R):
    triplets = canonical_triplets(L, R) + canonical_triplets(R, L)
    return triplets