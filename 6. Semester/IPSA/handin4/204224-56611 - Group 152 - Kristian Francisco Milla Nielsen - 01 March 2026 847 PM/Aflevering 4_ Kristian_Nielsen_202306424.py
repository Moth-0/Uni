'''''
This is done by :
748507 Kristian Milla

Reflection upon solution:
Jeg har fået mange hints af AI til at komme i mål med denne aflevering.

b: Jeg skulle lige vride mit hoved omkring, at funktionen skulle returnere to ting 
(både labels og triplets) for at holde styr på informationen hele vejen op gennem træet. 
Når først man forstår, at man bygger løsningen nedefra (bottom-up), så giver det pludselig 
mening, hvorfor man skal have begge dele med.

c: Sæt-operationer er virkelig en livredder her. Uden set.intersection ville sammenligningen 
af træer være alt for tung og langsom. Det er en 
hård lektie at lære, at $O(n^3)$ kompleksitet vokser hurtigere, end man lige regner med, 
når man tester med bare lidt for mange blade!
'''
#old code from last assignment
#a
def generate_labels(n):
    return [f'L{i}' for i in range(n)]

generate_labels(5)

#b
from random import randint
def permute(L):
    copy_L = list(L)
    result = []
    while len(copy_L) > 0:
        random_index = randint(0, len(copy_L) - 1)
        chosen_element = copy_L[random_index]
        result.append(chosen_element)
        copy_L = copy_L[:random_index]+copy_L[random_index+1:]
    return result

print(permute(['A', 'B', 'C', 'D']))

#c
def pairs(L):
    resultat = []
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i]<L[j]:
                resultat.append((L[i], L[j]))
            else:
                resultat.append((L[j], L[i]))
    #ligesom palindromer!
    return resultat

pairs(['A', 'F', 'B'])

#d
def canonical_triplets(A, B):
    return [(a, p) for a in A for p in pairs(B)]

canonical_triplets(['A', 'B'], ['C', 'D', 'E'])

#e
def anchored_triplets (L, R):
    return canonical_triplets(L, R) + canonical_triplets(R, L)

anchored_triplets(['A', 'F', 'B'], ['D', 'C', 'E'])


#8.8, part two

#a
import random

def generate_tree(labels):
    if len(labels) == 1:
        return labels[0]
    split = random.randint(1, len(labels) - 1)
    return (generate_tree(labels[:split]), generate_tree(labels[split:]))

generate_tree(['A', 'B', 'C', 'D', 'E', 'F'])

#b
def generate_triplets(tree):
    if isinstance(tree, str):
        return ([tree], [])

    left_labels, left_triplets = generate_triplets(tree[0])
    right_labels, right_triplets = generate_triplets(tree[1])
    
    all_labels = left_labels + right_labels
    
    new_triplets = anchored_triplets(left_labels, right_labels)
    
    total_triplets = left_triplets + right_triplets + new_triplets
    
    return (all_labels, total_triplets)

generate_triplets(((('A', 'F'), 'B'), ('D', ('C', 'E'))))

#c
def triplet_distance(tree1, tree2):
    _, triplets1 = generate_triplets(tree1)
    _, triplets2 = generate_triplets(tree2)

    set1 = set(triplets1)
    set2 = set(triplets2)

    labels1, _ = generate_triplets(tree1)
    n = len(labels1)
    
    total_triplets = n * (n - 1) * (n - 2) // 6

    common_triplets = len(set1.intersection(set2))
    
    return total_triplets - common_triplets

triplet_distance(((('A', 'F'), 'B'), ('D', ('C', 'E'))),
                 (((('D', 'A'), 'B'), 'F'), ('C', 'E')))

#d
import time

def benchmark_trees(sizes):
    print(f"{'Blade (n)':<12} | {'Generer (s)':<12} | {'Distance (s)':<12}")
    print("-" * 40)
    
    for n in sizes:
        labels = [f'L{i}' for i in range(n)]
        
        # Mål generate_tree
        start = time.time()
        t1 = generate_tree(labels)
        t2 = generate_tree(labels)
        gen_time = time.time() - start
        
        # Mål triplet_distance
        start = time.time()
        dist = triplet_distance(t1, t2)
        dist_time = time.time() - start
        
        print(f"{n:<12} | {gen_time:<12.4f} | {dist_time:<12.4f}")

# Prøv med forskellige størrelser
#benchmark_trees([10, 50, 100, 250, 500, 1000])

'''
Baseret på målingerne kan koden håndtere træer med op til ca. 250-300 blade inden for 10 sekunder. 
Vi befinder os altså solidt i kategorien "hundredvis" af blade, da beregningstiden for triplet_distance 
eksploderer derefter pga. dens $O(n^3)$ kompleksitet. Tusinder eller millioner af blade er desværre 
uden for rækkevidde med denne tilgang, da computeren løber tør for tid (og hukommelse) længe før.
'''