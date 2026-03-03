'''
HANDIN 3 (triplet distance - part I)

202307796 Oskar Juul Bjerre
202304778 Mathias Dahl Rahbek 

Reflection upon solution: 
Throughout this Hand-in, we attempted to make list comprehension for all the 
functions. This proved to be quite the challenge for task b). We eventually
managed to do it by using the same logic as we did in task e). Task a), b) and
c) was quite straightforward to write as list comprehensions. In task e), we
struggled abit to unpack the elements from canonical_triplets, but when it 
eventually worked, we could use it for task b) as mentioned. 
Hopefully we have created our functions in such a way that they will be easy
to use in the next Hand-in. Lastly, we considered there might be a better way
to make it run through [L,R] and [R,L] in task e), but we could not find it.
'''
import random
#a) 
def generate_labels(n): 
    L=[chr(65+i) for i in range(n)] # Choosing chr(65) to get the alphabet
    return L

#b)
def permute(L):
    L_permuted= [L.pop(idx)
                 for _ in range(len(L)) 
                 for idx in [random.randint(0,len(L)-1)]]
    return L_permuted

#c)
def pairs(L): 
    L_pairs = [(e1,e2) for e1 in L for e2 in L if e1 < e2]
    return L_pairs

#d)
def canonical_triplets(A,B):
    L_triplet = [(e,(e1,e2)) for e in A for e1 in B for e2 in B if e1 < e2]
    return L_triplet

#e) 
def anchored_triplets(L, R):
    L_anchor = [triplet
                for L1 in [L,R] 
                for L2 in [L,R] if L1!=L2 
                # We changed (L,R) to (L1,L2), this fixes it
                for triplet in canonical_triplets(L1,L2)] 
    return L_anchor