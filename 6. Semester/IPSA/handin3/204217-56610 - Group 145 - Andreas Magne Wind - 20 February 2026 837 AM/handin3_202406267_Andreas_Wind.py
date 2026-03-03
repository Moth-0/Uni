
'''
HANDIN 3 (triplet distance - part I)

This handin is done by (study ids and names of up to three students):

    202406267 Andreas Wind

Reflection upon solution:

    Først syntes jeg at det var ret uoverskueligt med al den information
    fra opgaven, men så gik det op for mig at det bare var en masse
    funktioner man skulle lave.
    Jeg brugte ret lang tid på at gennemskue opgave d, indtil det gik op
    for mig at jeg bare skulle bruge pairs() funktionen som jeg lavede i
    opgave c.
'''


import random


# a)

def generate_labels(n):
    l = []
    for i in range(1,n+1):
        l.append("L" + str(i))
    return l
        
generate_labels(5)

# b)

def permute(L):
    # laver list til resultatet
    permuted_list = []
    # laver en liste med værdier der ikke er blevet valgt endnu
    pool = L.copy()
    while pool: #mens der stadig er værdier tilbage i pool
        #til permuted_list bliver der lagt en af de tilfældige poppede fra pool
        permuted_list.append(pool.pop(random.randrange(len(pool))))
        
    return permuted_list

# c)

def pairs(L):
    # looper over hvert element
    # for hvert element laves der en tuple for hvert andet element
    # men jeg skal undgå dobbelt-tællinger
    # så hvert element skal kun lave liser med elementerne der ligger efter
    pairs_list = []
    for i, l  in enumerate(L): # looper over hvert element i listen
        for j in L[i+1:]: # looper over alle elementerne efter
            tup = sorted((l,j))
            pairs_list.append(tup)
    return pairs_list
            
pairs(['A', 'F', 'B'])

# d)

def canonical_triplets(A, B):
    tups = []
    for a in A: # looper over venstre subtree
        for p in pairs(B):
            tups.append((a,p))
    return tups


dlist1 = ['A', 'B']
dlist2 = ['C', 'D', 'E']

canonical_triplets(dlist1, dlist2)

# e)

def anchored_triplets(L,R):
    triplets = []
    for l in L:
        for p in pairs(R):
            triplets.append((l,p))
    
    for r in R:
        for p in pairs(L):
            triplets.append((r,p))
    
    return triplets

elista, elistb = ['A', 'F', 'B'], ['D', 'C', 'E']

print(anchored_triplets(elista, elistb))



