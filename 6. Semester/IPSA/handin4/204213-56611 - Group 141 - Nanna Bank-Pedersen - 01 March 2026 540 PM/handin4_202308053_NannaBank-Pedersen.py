'''
HANDIN 4 (triplet distance - part II)

This handin is done by:
    202308053 Nanna Bank-Pedersen

Reflection upon solution:
Det mest udfordrende var den rekursive struktur og at forstå 
hvordan triplets kunne laves fra både venstre og højre undertræer. 
Især var det lidt udfordrende at kombinere labels og triplets korrekt i 
generate_triplets, så ingen triplets blev glemt, og rækkefølgen af 
labels stadig var rigtig. Jeg antager stadig at input er en liste i formatet "L<tal>".
En anden udfordring var beregningen af triplet-afstanden mellem to træer. 
Det kræver, at man først genererer alle triplets, og derefter sammenligner 
dem som mængder. Dette kan blive langsomt for store træer, som man også 
kan se i koden for n > 400, hvor triplet_distance tager over 10 sekunder. 
En begrænsning er derfor, at algoritmen ikke skalerer effektivt til meget store træer.
Det nemmere ved opgaven var at bruge de tidligere funktioner som pairs og 
anchored_triplets fra sidste aflevering.
'''

'''
Foregående afleverings kode nedenfor
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
'''
Foregående afleverings kode ovenfor
Denne afleverings kode nedenfor
'''

# Recursive generate tree function
def generate_tree(labels):
    if len(labels) == 1:
        return labels[0]
    
    split = randint(1, len(labels) - 1)

    left_labels = labels[split:]
    right_labels = labels[:split]

    left_tree = generate_tree(left_labels)
    right_tree = generate_tree(right_labels)

    return (left_tree, right_tree)

            #labels = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6']
            #tree = generate_tree(labels)
            #print(tree)

# Recursive generate triplets tree functio
def generate_triplets(tree):
    if isinstance(tree, str):
        return([tree], [])
    
    left, right = tree
    
    left_labels, left_triplets = generate_triplets(left)
    right_labels, right_triplets = generate_triplets(right)

    anchored = anchored_triplets(left_labels, right_labels)
    labels = left_labels + right_labels
    triplets = left_triplets + right_triplets + anchored

    return (labels, triplets)

            #tree = ((('L1', 'L6'), 'L2'), ('L4', ('L3', 'L5')))
            #labels, triplets = generate_triplets(tree)
            #print(labels)
            #print(triplets)

# Triplet distance function
def triplet_distance(tree1, tree2):
    labels1, triplets1 = generate_triplets(tree1)
    labels2, triplets2 = generate_triplets(tree2)
    n = len(labels1)
    
    total_triplets = n * (n - 1) * (n - 2) // 6

    set1 = set(triplets1)
    set2 = set(triplets2)
    common = len(set1 & set2)

    return (total_triplets - common)

            #tree1 = ((('L1', 'L6'), 'L2'), ('L4', ('L3', 'L5')))
            #tree2 = (((('L4', 'L1'), 'L2'), 'L6'), ('L3', 'L5'))
            #print(triplet_distance(tree1, tree2))

'''
# Order of trees in reasonable time
import time

for n in [20, 50, 100, 200, 300, 400, 450]:
    labels = generate_labels(n)

    start = time.time()
    t1 = generate_tree(labels)
    t2 = generate_tree(labels)
    gen_time = time.time() - start

    start = time.time()
    d = triplet_distance(t1, t2)
    dist_time = time.time() - start

    print(f"n={n:4d}, generate_tree: {gen_time:.4f}s, triplet_distance: {dist_time:.4f}s")

# Output
#n=  20, generate_tree: 0.0001s, triplet_distance: 0.0016s
#n=  50, generate_tree: 0.0001s, triplet_distance: 0.0110s
#n= 100, generate_tree: 0.0002s, triplet_distance: 0.0873s
#n= 200, generate_tree: 0.0005s, triplet_distance: 0.8201s
#n= 300, generate_tree: 0.0007s, triplet_distance: 2.7109s
#n= 400, generate_tree: 0.0010s, triplet_distance: 7.6127s
#n= 450, generate_tree: 0.0012s, triplet_distance: 10.6653s
# ved n på 450 tager triplet_distance funktionen over 10 sekunder, muligvis vil et lavere n give en højere tid på en anden computer
# men jeg vil mene grænsen er ved et par hundrede.
'''
