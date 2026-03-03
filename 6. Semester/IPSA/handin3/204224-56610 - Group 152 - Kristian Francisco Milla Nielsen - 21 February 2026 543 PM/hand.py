'''''
This is done by :
748507 Kristian Milla

Reflection upon solution:
a: Lettest at bare sætte et stigende tal på L fremfor A,B,C,D... (ved ik lige hvordan jeg får den til at printe 
de n første tal i alfabetet)
b: Jeg startede med at tage et tilfældigt tal fra min(L) til max(L) og kun bruge det hvis det var et element i L. 
Men det er smartere at tage et tilfældigt indeks. 
c: Minder meget om palindromer - en forløkke i en forløkke. Ikke problematisk
d: Jeg skulle lige vride mit hoved omkring at for a in A for p in B - faktisk også er en forløkke i en forløkke!
e: Simpelt når det lige går op for en at alle tripletter der har en given knude som deres "mødepunkt" enten har 
1 element i venstre og 2 elementer i højre 
- eller omvendt. Så er det bare at bruge funktionen fra før og addere de to resultater
'''''

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

        