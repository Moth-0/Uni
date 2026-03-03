
"""
HANDIN 3 (triplet distance - part 1)

This handin is done by:

202407098 Johanne Stubkjær
202408622 Magnus Overgaard
202405571 Jonas Ullgren

Reflection upon solution:

We made sure that our generate function could generate lists based on a start value to be able to create non-identical lists. 
Furthermore we tried several different approaches to the permute function, which was the task we struggled most with. 
First we tried using randint to make shuffled indexes to zip with the list elements, but that failed and we ultimately ended
up just using a more 'brute-force'-method and essentially just swapping two elements one by one. for the pairs() function, we 
really struggled with getting a good idea, and before we used the hack of letting j go from i+1, there were a lot more code.
"""


#a)
def generate_labels(n, start=0):
    if start !=0:
        return ['L'+str(i+start-1) for i in range(1, n+1)]
    else:
        return ['L'+str(i+start) for i in range(1, n+1)]
    
generate_labels(6)



#b)
n=3
L = generate_labels(n)

from random import randint
def permute(L):
    for i in range(len(L*5)):
        a, b = L.index(L[randint(0, len(L)-1)]), L.index(L[randint(0,n-1)])
        L[a], L[b] = L[b], L[a]
    return L

permute(L)



#c)
n=3
L = generate_labels(n)

def pairs(L):
    pairss = []
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            pairss.append(tuple(sorted((L[i], L[j]))))
    return (pairss)

pairs(L)



#d)
A = generate_labels(3)
B = generate_labels(3, start=4)

print(f'A = {A}, B = {B}')

def canonical_triplets(A,B):
    B_par = pairs(B)
    par = []
    for i in range(len(B_par)):
        for j in range(len(A)):
            par.append((A[j],B_par[i]))
    return par

canonical_triplets(A,B)



#e)
def anchored_triplets(L,R):
    return canonical_triplets(L,R) + canonical_triplets(R,L)

L = generate_labels(3)
R = generate_labels(3, start=4)   

anchored_triplets(L,R)