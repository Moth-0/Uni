"""
HANDIN 4 - Triplet distance part 2

This handin is done by: 
    202307989 Mikkel Moth Billing 

Reflection upon solution: 
    I had a hard time understanding recursion, so i had some help to get started and used python tutor,
    to understand what was actually going on. For excersise d i could rewrite the generate labels function, 
    so it just uses numbers instead so i could go higher, but the time taken seems to be linear, 
    so it could maybe go to 2_000_000. 
"""

# Functions from last time 
from random import randint

def generate_labels(n):
    return [chr(l) for l in range(65, 65+n)] # chr(n) gives the ASCII character of n A-Z is 65-90

def permute(L): 
    perm = []
    for i in range(len(L)): 
        n = randint(0, len(L)-1)    # Select random index of L
        perm.append(L[n])           # Add that element of L to perm
        L.remove(L[n])              # Remove that element from L so it is not picked again
    return perm

def pairs(L):
    return [(min(L[i], L[j]), max(L[i], L[j])) for i in range(len(L)) for j in range(i+1, len(L))]
    # For each element in L, for each element after i, add the tuple to the list
    # Done in one line instead of two for loops, and sorted for part 2 

def canonical_triplets(A, B): 
    B_pairs = pairs(B)                  # Get all pairs of B
    triplets = []
    for a in A:                         # For each element in A
        for b in B_pairs:               # For each pair in B
            triplets.append((a, b))     # Add the triplet to the list
    return triplets

def anchored_triplets(L, R): 
    L_triplets = canonical_triplets(L, R) # Get all triplets with L as the anchor
    R_triplets = canonical_triplets(R, L) # Get all triplets with R as the anchor
    return L_triplets + R_triplets        # Return the concatenation of the two lists

# Part 2 

# a
def generate_tree(labels): 
    # Base case to stop recursion if only one element in labels
    if len(labels) == 1:
        return labels[0]
    
    # Split tuple at random index
    split_int = randint(1, len(labels)-1)
    left = labels[:split_int]
    right = labels[split_int:]
    
    # Start recursion where both of the plit parts go through function
    return (generate_tree(left),generate_tree(right))

print("a: ", generate_tree(generate_labels(6)))

# b 
def generate_triplets(tree): 
    # To stop recursion and return the labels list
    if isinstance(tree, str):
        return [tree], []
    
    # Split tuple in left and right
    left, right = tree
    
    # Run recursion of every pair 
    left_label, left_triplet = generate_triplets(left)
    right_label, right_triplet = generate_triplets(right)

    # Make anchored canonical triplets, with function from part 1
    new_triplet = anchored_triplets(left_label, right_label)

    # Return the labels and the triplets 
    return left_label + right_label, left_triplet + right_triplet + new_triplet

trips = generate_triplets(((('A', 'F'), 'B'), ('D', ('C', 'E'))))
print("b: ", trips)
print(len(trips[1]))


# c
def triplet_distance(tree1, tree2): 
    # Generates triplet sets for both trees
    label1, triplets1 = generate_triplets(tree1)
    label2, triplets2 = generate_triplets(tree2)
    
    # Find common triplet sets with set operations 
    common_triplets = set(triplets1) & set(triplets2)

    # n is number of "leaves" therefore len of leaf-list, 
    # and we assume both trees have same set of labels
    n = len(label1)

    return ((n*(n-1)*(n-2)) / 6) - len(common_triplets)

print("c: ", triplet_distance(((('A', 'F'), 'B'), ('D', ('C', 'E'))), (((('D', 'A'), 'B'), 'F'), ('C', 'E'))))

# d 
import timeit
print("d: ")
# To make a tree i can go to 1 million before i hit the limit for ASCII characters, 
# and it takes 5 seconds
n = 1_000_000
start = timeit.default_timer()
generate_tree(generate_labels(n))
stop = timeit.default_timer()

print(f"Time to genereate tree, with {n} branches: {stop - start} s")  

# For finding the distance i get 9.5 seconds for n=300 and 38 seconds for 400 
n = 300
tree1 = generate_tree(generate_labels(n))
tree2 = generate_tree(generate_labels(n))

start = timeit.default_timer()
triplet_distance(tree1, tree2)
stop = timeit.default_timer()

print(f"Time to calculate distance, with {n} branches: {stop - start} s")  