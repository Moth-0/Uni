#%%

'''
a) Første funktion er meget simpel. Den henter hele alfabetet som upper case bogstaver og gemmer de
n første med en list comprehension, hvorefter den returnerer dem i en liste af strings.
, hvor n er en fri parameter.

b) Vi laver en ny liste med længden af den gamle og appender et tilfældigt element fra den gamle liste, indtil
denne er udtømt. Vi returnerer den shufflede liste.

c) Vi laver en list comprehension med 2 for-loops så vi kan få alle kombinationer af par, hvor a<b, dvs.
det første element er mindre end det næste.

d) Med en list comprehension henter vi for hvert element i listen A også et muligt par fra B og returnerer en
liste af alle kombinationerne på formen ('A', ('B', 'C')).

e) Vi kører den gamle funktion canonical_triplets() for at få alle gyldige triplets fra ret anchor point v.
Den køres både forfra og bagfra (ved at bytte om på rækkefølge af inputs) for at få alle muligheder med og
returnerer dem i en liste af nested tuples som den skal.

'''
import string
from random import randint

#a)
def generate_labels(n):
    letters = list(string.ascii_uppercase)
    labels = [letters[_] for _ in range(n)]
    return labels

#b)
def permute(L):
    permutation = []
    for _ in range(len(L)):
        num = randint(0, len(L)-1)
        permutation.append(L[num])
        del L[num]
    return permutation

#c)
def pairs(L):
    L_paired = [(a, b) for a in L for b in L if
                a < b]
    return L_paired

#d)

# A = ['A', 'B']
# B = ['C', 'D', 'E']

def canonical_triplets(A, B):
    triplets = [(i, j) for i in A for j in pairs(B)]
    return triplets

#e)

# L = ['A', 'F', 'B']
# R = ["D", "C", "E"]

def anchored_triplets(L, R):
    triplets1 = canonical_triplets(L, R)
    triplets2 = canonical_triplets(R, L)
    all_triplets = triplets1 + triplets2
    return all_triplets

#print(anchored_triplets(L, R))
# %%
