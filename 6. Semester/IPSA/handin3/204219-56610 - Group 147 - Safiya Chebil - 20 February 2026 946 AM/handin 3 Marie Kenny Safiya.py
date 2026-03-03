'''
202408911 Safiya Chebil
202406237 Marie Schnoor-Madsen
202407458 Kenny Nguyen

#for spg a) var udfordringen at generer en liste der tager højde for n'er der 
#er større end længden af listen og generer nye strings til den, istedet for slicing.
#for d) var udfordringen at sikre sig at den ikke gentager den samme string, det gøre vi med en if betingelse med pass
#for c) var der store overvejlser til hvordan man vil opstille den og vi endte med at have
#en for loop der tæller index. 
#resten kan vi nemt genbruge funktioner fra tidliger som forkorter koden
'''

from random import randint

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
