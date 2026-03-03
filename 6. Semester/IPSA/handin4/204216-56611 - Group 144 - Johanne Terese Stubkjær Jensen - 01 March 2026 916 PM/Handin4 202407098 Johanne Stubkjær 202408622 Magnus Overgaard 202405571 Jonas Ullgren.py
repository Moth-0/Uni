"""
HANDIN 4 (triplet distance - part 2)

This handin is done by:

202407098 Johanne Stubkjær
202408622 Magnus Overgaard
202405571 Jonas Ullgren

Reflection upon solution:

We struggled a bit with the generate_triplet function and had to use pythontutor.com several times to viasualize what really
happend. But it made us understand recursion more in depth. Actually generate_tree was also surprisingly hard and we initially
tried a lot of lenghtier, more complicated paths, which turned out to be not necessary at all. Also nice and useful to be 
reminded how the time() function works. to reflect on the time results in d): as expected generate_triplets takes a lot longer
time than generate tree. obvs. Also the time for generate_triplets seems to grows exponentially - which is bad.
"""

def generate_labels(n, start=0):
    if start !=0:
        return [chr(start+63+i) for i in range(1, n+1)]
    else:
        return [chr(64+i) for i in range(1, n+1)]
    
generate_labels(6)

n=3
L = generate_labels(n)

from random import randint
def permute(L):
    for i in range(len(L*5)):
        a, b = L.index(L[randint(0, len(L)-1)]), L.index(L[randint(0,n-1)])
        L[a], L[b] = L[b], L[a]
    return L

permute(L)

n=3
L = generate_labels(n)

def pairs(L):
    pairss = []
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            pairss.append(tuple(sorted((L[i], L[j]))))
    return (pairss)

pairs(L)

A = generate_labels(6)
B = generate_labels(6)

#print(f'A = {A}, B = {B}')

def canonical_triplets(A,B):
    B_par = pairs(B)
    par = []
    for i in range(len(B_par)):
        for j in range(len(A)):
            par.append((A[j],B_par[i]))
    return par

canonical_triplets(A,B)

def anchored_triplets(L,R):
    return canonical_triplets(L,R) + canonical_triplets(R,L)

L = generate_labels(3)
R = generate_labels(3, start=4)   

anchored_triplets(L,R)

# a)
def generate_tree(labels):
    if len(labels) <= 1:
        return labels[0]
    elif len(labels) == 2:
        return tuple(labels)
        
    split = randint(1, len(labels) - 1)
    
    left, right  = labels[:split], labels[split:]

    left_tree = generate_tree(left)
    right_tree = generate_tree(right)

    return (left_tree, right_tree)

labels = generate_labels(6)
generate_tree(labels)

# b)
labels = generate_labels(6)
tree = generate_tree(labels)

tree1 = (((('D', 'A'), 'B'), 'F'), ('C', 'E'))

def generate_triplets(tree, leaves=None, triplets=None):

    if leaves is None:
        leaves = []
    if triplets is None:
        triplets = []

    if isinstance(tree, str): #leaves
        leaves.append(tree[0])
        return (leaves, triplets)

    left, right  = tree[0], tree[1]

    leaves_left=[]
    leaves_right=[]

    generate_triplets(left, leaves_left, triplets)
    generate_triplets(right, leaves_right, triplets)

    trip = anchored_triplets(leaves_left, leaves_right)
    triplets.extend(trip)
    leaves.extend(leaves_left)
    leaves.extend(leaves_right)
    
    return (leaves, triplets)

print(generate_triplets(tree1))

# c)
def triplet_distance(tree1, tree2):
    labels1, triplets1 = generate_triplets(tree1)
    labels2, triplets2 = generate_triplets(tree2)
    
    n = len(labels1)
    
    set1 = set(triplets1)
    set2 = set(triplets2)
    
    common_triplets = len(set1.intersection(set2))
    total_possible = (n * (n - 1) * (n - 2)) // 6
    
    distance = total_possible - common_triplets
    return distance

tree1 = generate_tree(generate_labels(6))
tree2 = generate_tree(generate_labels(6))

# tree1 = ((('A', 'F'), 'B'), ('D', ('C', 'E')))
# tree2 = (((('D', 'A'), 'B'), 'F'), ('C', 'E'))

triplet_distance(tree1, tree2)

# d)
import time

def run_scaling_test():
    n_values = [10, 20, 50, 100, 200, 300, 400, 800]
    
    print(f"{'Leaves (n)':<10} | {'Time (gen) (seconds)':<20} | {'Time (trip) (seconds)':<20}")
    print("-" * 60)
    
    for n in n_values:

        labels_1 = generate_labels(n)
        labels_2 = generate_labels(n)

        start_time_gen = time.time()
        
        tree_1 = generate_tree(labels_1)
        tree_2 = generate_tree(labels_2)

        end_time_gen = time.time()
        time_gen = end_time_gen - start_time_gen

        start_time_trip = time.time()

        triplet_distance(tree_1, tree_2)
        
        end_time_trip = time.time()
        time_trip = end_time_trip - start_time_trip
        
        print(f"{n:<10} | {time_gen:<20.4f} | {time_trip:<20.4f}")

        if time_gen > 10:
            print(f"\nResult: n={n} is the limit for generate_tree. n={n} exceeded 10s.")
            break

        if time_trip > 10:
            print(f"\nResult: n={n} is the limit for generate_triplets. n={n} exceeded 10s.")
            break

