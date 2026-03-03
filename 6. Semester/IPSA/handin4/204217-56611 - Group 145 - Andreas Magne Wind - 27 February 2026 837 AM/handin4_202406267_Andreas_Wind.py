
'''
HANDIN 4 (triplet distance - part II)

This handin is done by (study ids and names of up to three students):

    202406267 Andreas Wind

Reflection upon solution:

    Til de første opgaver med rekursion lavede jeg et "udkast" og spurgte
    AI om den kunne give mig et hint til hvordan det blev rigtigt. Så
    opdagede jeg at mine udkast faktisk var meget tæt på at være rigtige
    og det kun var nogle logiske detaljer der manglede.
    I opgave c syntes jeg at det var sjovere at antage at de ikke havde
    samme antal labels, da jeg nemt kunne se mig ud af at lave en
    funktion til det.
    Triplets kunne regnes på under et sekund på til 1000 træer, men
    derefter tog det meget længere tid end 10 sekunder.
'''

import random
import timeit

def generate_labels(n):
    l = []
    for i in range(1,n+1):
        l.append("L" + str(i))
    return l
        
def permute(L):
    # laver list til resultatet
    permuted_list = []
    # laver en liste med værdier der ikke er blevet valgt endnu
    pool = L.copy()
    while pool: #mens der stadig er værdier tilbage i pool
        #til permuted_list bliver der lagt en af de tilfældige poppede fra pool
        permuted_list.append(pool.pop(random.randrange(len(pool))))
        
    return permuted_list

def pairs(L):
    # looper over hvert element
    # for hvert element laves der en tuple for hvert andet element
    # men jeg skal undgå dobbelt-tællinger
    # så hvert element skal kun lave liser med elementerne der ligger efter
    pairs_list = []
    for i, l  in enumerate(L): # looper over hvert element i listen
        for j in L[i+1:]: # looper over alle elementerne efter
            tup = tuple(sorted((l,j)))
            pairs_list.append(tup)
    return pairs_list

def canonical_triplets(A, B):
    tups = []
    for a in A: # looper over venstre subtree
        for p in pairs(B):
            tups.append((a,p))
    return tups

def anchored_triplets(L,R):
    triplets = []
    for l in L:
        for p in pairs(R):
            triplets.append((l,p))
    
    for r in R:
        for p in pairs(L):
            triplets.append((r,p))
    
    return triplets


# a)

def generate_tree(labels):
    result = []
    if len(labels) == 1:
        return labels[0]
    else:
        split_index = random.randint(1, len(labels)-1)
        left = labels[:split_index]
        right = labels[split_index:]
        return (generate_tree(left), generate_tree(right))

#print(generate_tree(['A', 'B', 'C', 'D', 'E', 'F']))

# b)
def generate_triplets(tree):
    if isinstance(tree,str):
        return [tree], []
    else:
        labels_left, triplets_left = generate_triplets(tree[0])
        labels_right, triplets_right = generate_triplets(tree[1])
        new_triplets = anchored_triplets(labels_left, labels_right)
        return (labels_left + labels_right, triplets_left + triplets_right + new_triplets)

#print(generate_triplets(generate_tree(['A', 'B', 'C', 'D', 'E', 'F'])))

# c)
def triplet_distance(tree1, tree2):
    
    # noget med at bruge generate_triplets første output labels til at
    # se alle labels i træet

    labels1, triplets1 = generate_triplets(tree1)
    labels2, triplets2 = generate_triplets(tree2)

    n =len(list(set(labels1) & set(labels2)))
    common_triplets = len(list(set(triplets1) & set(triplets2)))
    return (n*(n-1)*(n-2)//6) - common_triplets

#print(triplet_distance(((('A', 'F'), 'B'), ('D', ('C', 'E'))),
#                (((('D', 'A'), 'B'), 'F'), ('C', 'E'))))
'''
# d)
test_sizes = [10, 100, 1000]


for s in test_sizes:

    test_tree1 = generate_tree(generate_labels(s))
    test_tree2 = generate_tree(generate_labels(s))

    t_tree = timeit.timeit('generate_tree(generate_labels(s))', 
                    globals=globals(), 
                    number=1)
    print(f"Time to generate tree of {s} leaves: {t_tree}")

    t_distance = timeit.timeit('triplet_distance(test_tree1, test_tree2)', 
                    globals=globals(), 
                    number=1)
    print(f"Time to calculate triplet distance for {s} leaves: {t_distance} seconds")
'''