from random import randint
'''
HANDIN 4 (triplet distance part II )

This handin is done by (study ids and names of up to three students):

    202407458 Kenny Nguyen
    202408911 Safiya Chebil 
    202406237 Marie Schnoor - Madsen 

    
Reflection upon solution:

    Sværheden lå i at visulisere functionerne, implemetere rekursion og opbygge basen for funktionen
    opgave d) var sværheden at arbejde med tuples, sammenligne dem og sortere dem. 
'''
#Importere kode fra tidligere handins
#a)
L = ['A','B','C','D','E','F']
def generate_labels(n):
    out = []
    k = 1 

    while len(out) < n:
        for ch in L:
            out.append(ch * k)
            if len(out) == n:
                return out
        k += 1

print(generate_labels(10))

#b)
def permute(L): 
    shuffled_L = []
    while len(L) != len(shuffled_L):
        x = randint(0,len(L)-1)
        if L[x] in shuffled_L:
            pass 
        else:
            shuffled_L.append(L[x])
    return shuffled_L 

permute(L)

#c)
def pairs(L): 
    out = []
    for i in range(0, len(L)-1): 
        for j in range(i+1, len(L)): 
            k = (L[i], L[j])
            out.append(k) 
    return out 
pairs(L) 
L2 = ['C','D','E']
pairs(L2)

#d)
L1 = ['A','B'] 
L2 = ['C','D','E']

def canconical_triplets(L1,L2): 
    L2 = pairs(L2) 
    out = []
    for i in range(0,len(L1)):
        for j in range(0, len(L2)): 
            k = (L1[i], L2[j]) 
            out.append(k) 
    return out 

canconical_triplets(L1,L2)

#e)
def anchored_triplets(L,R): 
    k = canconical_triplets(L,R)
    l = canconical_triplets(R,L)
    return k+l

L = ['A','B','P'] 
R = ['C','D','E']

anchored_triplets(L,R) 

#a) 
import time 
start = time.time() 
def generate_tree(labels): 
    if len(labels) == 1: 
        return labels[0]
    
    mid = randint(1,len(labels)-1)
    left = generate_tree(labels[:mid])
    right = generate_tree(labels[mid:])

    return (left, right)

labels = ['A','B','C','D','E','F']
generate_tree(labels) 
end = time.time() 
print(end - start)

#b) 
def generate_triplets(tree): 
    if isinstance(tree, str): 
        return [tree], []
    
    left, right = tree
    l_labels, l_triplets = generate_triplets(left)
    r_labels, r_triplets = generate_triplets(right)
    labels = l_labels + r_labels 
    k = canconical_triplets(l_labels,r_labels)
    l = canconical_triplets(r_labels,l_labels) 
    anchored_triplets = k + l
    return labels, l_triplets+r_triplets+anchored_triplets

generate_triplets(((('A', 'F'), 'B'), ('D', ('C', 'E'))))

def triplet_distance(tree1, tree2): 
    labels1, triplets1 = generate_triplets(tree1)
    labels2, triplets2 = generate_triplets(tree2)
    
    #triplets1 = [(triplets1[i][0],tuple(sorted(triplets1[i][1]))) for i in range(0, len(triplets1))]
    #triplets2 = [(triplets2[i][0],tuple(sorted(triplets2[i][1]))) for i in range(0, len(triplets2))]
    common_triplets = len(set(triplets1) & set(triplets2)) 
    if common_triplets < 3: 
        return [] 

    n = len(set(labels1) & set(labels2)) 
    distance = (n * (n-1)*(n-2)/6) - common_triplets 

    return distance

print(triplet_distance(((('A', 'F'), 'B'), ('D', ('C', 'E'))), (((('D', 'A'), 'B'), 'F'), ('C', 'E'))))


#d) på cirka 2e5 labels er vi op på 8.5 sekunders kørsel