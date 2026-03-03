'''
HANDIN 3 (Triplet distance, part 1)

This handin is done by Mathias Lystlund, id: 202408483

Reflection upon solution:
I found it much easier to label them with L and some incresing numbers. 
My solution depend mostly on for-loops, it might not be the fastest or the most simple
code but it works.

Other than that, i dont have much to say.


'''

## Task a
import random


def generate_labels(n1, n0=0):
    L = []
    for i in range(n0, n1):
        L.append('L'+str(i))
    return L

L = generate_labels(0, 4)
print(L)

## Task b
def permute(L):
    ny = []
    ran = []
    while len(ran) != len(L):
        k = random.randint(0, len(L)-1)
        if k not in ran:
            ran.append(k)
    
    for i in ran:
        ny.append(L[i])

    return ny

print(permute(L))

## Task c
def pairs(L):
    par = []
    for i in range(len(L)):
        for n in range(len(L)):
            if L[i] != L[n]:
                hold = (L[i], L[n])
                if hold and hold[::-1] not in par:
                    par.append(hold)

            
    return par
    
p = pairs(L)
print(p)

## Task d
a = generate_labels(0, 2)

b = generate_labels(2, 5)

def canonical_triplets(a, b):
    can = []
    par = pairs(b)

    for i in a:
        for n in range(len(par)):
            can.append((i, par[n]))
    return can

Can = canonical_triplets(a, b)

print(Can)

## Task e
A = generate_labels(0, 3)
B = generate_labels(3, 6)
def anchored_triplets(a, b):
    return canonical_triplets(a, b) + canonical_triplets(b, a)

anc = anchored_triplets(A, B)
print(anc)
