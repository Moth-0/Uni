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

from random import randint

#a)
def generate_labels(n):
    return [chr(65 + i % 26) for i in range(n)]

#b)
def permute(L):
    L_copy = L[:]
    permutation = []

    while L_copy:
        num = randint(0, len(L_copy) - 1)
        permutation.append(L_copy[num])
        del L_copy[num]

    return permutation


#c)
def pairs(L):
    L_sorted = sorted(L)
    return [(L_sorted[i],L_sorted[j])
            for i in range(len(L))
            for j in range(i+1, len(L))]

print(pairs(['A', 'F', 'B']))

#d)

A = ['A', 'B']
B = ['C', 'D', 'E']

def canonical_triplets(A, B):
    B_pairs = pairs(B)
    triplets = [(i, j)
                for i in A 
                for j in B_pairs]
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
#%%

#Aflevering 4

''' Refleksioner
a) Havde mange problemer med type errors på grund af at returnere en liste eller string
, der så ikke kunne concatenates i funktionen... randint gav også problemer,
da den gik fra 0 og ikke 1 til længden af labels-1, da vi endte med tomme lister
og uendelig rekursion på dem for a). Ellers fulgte jeg hintet og slicede
et tilfældigt indeks frem og tilbage og fortsatte denne proces til der kun var 
et label tilbage. Herfra er det bare at sætte labels sammen i tuples.

b) Havde mange problemer og brugte sygt lang tid, indtil jeg ændrede base case til
at returnere "[tree], []". Funktionen opsamler egentlig bare labels ved at køre
funktionen rekursivt på left og right gren af træet. Ved hver node beregner
vi med funktionen anchored triplets og samler dem sammen for hvert funktionskald
også. Til sidst returnerer vi labels i rækkefølge og alle triplets ved hver node.
Blev nødt til at ændre på en del funktioner fra sidste aflevering undervejs, fordi
de ikke holdt. Særligt pairs og canonical_triplets og generate_labels.

c) Vi bruger generate_triplets til at give de gyldige triplets fra hvert træ.
Vi ved per antagelse at trææerne indeholder de samme labels, så n = len(labels1).
med mængdeoperationen '&' kan vi trække de triplets der går igen fra.


d) Efter antal labels i et træ overstiger 500, virker mine to funktioner ikke længere.
Jeg har ikke tid til at plotte det, og min computer er nok også for sløv.
Har bare brugt time() og kører det for værdierne i listen. Gætter på 
kombinationsmulighederne eksploderer for mulige triplets, når tallet nærmer sig
størrelsesorden 10^3. Det er triplet distance der er det svageste led i kæden -
det er nok tidskrævende at lede efter fælleselementer blandt triplets.
'''

#a) 
def generate_tree(labels):
    if len(labels) == 1:
        # print("leaf=", labels)
        return labels[0]
    
    num = randint(1, len(labels)-1) #sørger for vi aldrig splitter til tom liste
    # print("Split index=",num)
    # print(f"Current labels={labels}")

    right = generate_tree(labels[num:])
    left = generate_tree(labels[:num])

    return (left, right)

#b)
def generate_triplets(tree):
    if isinstance(tree, str):
        return [tree], []  # single leaf, no triplets

    # recursive case
    labels1, triplets1 = generate_triplets(tree[0])
    labels2, triplets2 = generate_triplets(tree[1])

    labels = labels1 + labels2
    anchored = anchored_triplets(labels1, labels2)
    triplets = triplets1 + triplets2 + anchored

    return labels, triplets
    

#c) compute triplet distance between two trees with the same labels
def triplet_distance(tree1, tree2):

    labels1, triplets1 = generate_triplets(tree1)
    labels2, triplets2 = generate_triplets(tree2)

    n = len(set(labels1))
    union_of_triplets = set(triplets1) & set(triplets2)
    n_common_triplets = len(union_of_triplets)

    d = (n*(n-1)*(n-2))/6-n_common_triplets

    return d

'''
#d)

import time

tree_sizes = [10, 50, 100, 500, 550]

for n in tree_sizes:
    labels = generate_labels(n)
    
    start = time.time()
    tree = generate_tree(labels)
    end = time.time()
    print(f"generate_tree funktionen for n={n}: {end-start:.5f} s")
    
    start = time.time()
    distance = triplet_distance(tree, tree)
    end = time.time()
    print(f"triplet_distance funktionen for n={n}: {end-start:.5f} s")
'''
# %%
