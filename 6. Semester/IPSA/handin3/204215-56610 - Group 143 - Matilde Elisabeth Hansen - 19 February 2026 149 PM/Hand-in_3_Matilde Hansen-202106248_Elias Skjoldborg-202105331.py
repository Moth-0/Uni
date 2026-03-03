'''
HANDIN 3 (triplet distance - part I)

This handin is done by:

    202106248 Matilde E. Hansen
    202105331 Elias R. Skjoldborg

Reflection upon solution:

We chose to treat the labels as numbers in base 26, where we use capital letters as the digets of the numbers. 
Therefore we needed a help function to convert back to regular base 10 numbers, such that we could compare their size (relevant for the pairs problem), using the build-in python operations. 
This is because these operations would not work as we wanted them to, since our labels are still strings. 
We do this because we want our labels to be strings of capital letters instead of strings containing numbers.

'''
import random as rd
from itertools import combinations

def generate_labels(n):
    String = []

    for k in range(1, n + 1):
        s = ""
        while k > 0:
            k -= 1                      # shift to start val
            k, r = divmod(k, 26)        # remainder is diget of a number in base 26
            s = chr(ord('A') + r) + s   # convert remainder to character and add to existing string
        String.append(s)
    # print(String)
    return String

def permute(List):                          # Fisher–Yates shuffle Algorithm
    n = len(List)
    for i in range(n-1,0,-1):               # We run over the elements from behind and swap one by one. 
                                            # We don't need to do this for the first element
        j = rd.randint(0,i+1)
        List[i],List[j] = List[j],List[i]
    return(List)

# Help function for the next task (pairs)
def label_to_int(label):
    n = 0
    for ch in label:
        n = n * 26 + (ord(ch) - ord('A') + 1)   # changes labels to integers
    return n

def pairs(List):
    Pairs = []
    n = len(List)
    for i in range(0,n):
        # print(List[i])
        for j in range(i+1,n):              # running from i+1 to n ensures we only consider every combination once
            x = label_to_int(List[i])
            y = label_to_int(List[j])
            if x < y:
                Pairs.append((List[i],List[j]))
            elif x > y:
                Pairs.append((List[j],List[i]))
    #print(Pairs)
    return Pairs
        
def canonical_triplets(A, B):
    x = [(a, pair) for a in A for pair in combinations(B, 2)] # Combinations looks at the B list, and returns all the possible combinations of two elements of the list
    #print(x)
    return x

def anchored_triplets(L, R):
    All_of_it = canonical_triplets(L,R)
    All_of_it += canonical_triplets(R,L)
    #print(All_of_it)
    return All_of_it


L = generate_labels(28)
LP = permute(L)
print(L)                                                    # Task a
print(LP)                                                   # Task b
print(pairs(['Z','A', 'F', 'B']))                           # Task c
print(canonical_triplets(['A', 'B'], ['C', 'D', 'E']))      # Task d
print(anchored_triplets(['A', 'F', 'B'], ['D', 'C', 'E']))  # Task e