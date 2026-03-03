'''
HANDIN 4 (triplet distance - part II)

This handin is done by:

    202106248 Matilde E. Hansen
    202105331 Elias R. Skjoldborg

'''
import random as rd
from itertools import combinations
import time

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
    new_list = List[:]                         # To avoid changing the original list, we need to make a copy, so that gets changed instead
    n = len(new_list)
    for i in range(n-1,0,-1):               # We run over the elements from behind and swap one by one. 
                                            # We don't need to do this for the first element
        j = rd.randint(0,i+1)
        new_list[i],new_list[j] = new_list[j],new_list[i]
    return(new_list)

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
    return tuple(Pairs)
        
def canonical_triplets(A, B):
    x = [(a, pairs(pair)) for a in A for pair in combinations(B, 2)] # Combinations looks at the B list, and returns all the possible combinations of two elements of the list
    #print(x)
    return x

def anchored_triplets(L, R):
    All_of_it = canonical_triplets(L,R)
    All_of_it += canonical_triplets(R,L)
    #print(All_of_it)
    return All_of_it

'''
Reflection upon solution (part II):
For the first task, we followed the hint of splitting up the tree in two halves, returning an element or a tuple, depending on how many elements were in the list,
on the left or right side. For the second task we used the same method of splitting into left and right. For the third task we created a set of the triplets,
such that we could convert it into a length integer n, such that we could use the formula for the triplet distance. We made sure to subtract the number of 
common triplets, again by dreating sets and finding the common elements of those sets. For the last task, concerning timing of the code, we used the command
time.time() and used a brute force method to find the approximate amount of labels generating trees in about 10 seconds. 

'''

#### New functions start below

def help_funk(side):        # We use a help function, since we want to do the same thing twice
    if len(side) == 1:
        return side[0]
    elif len(side) == 2:
        return tuple(side)
    else:
        return (generate_tree(side))    # This is the recursive step

def generate_tree(labels):
    j = rd.randint(1,len(labels)-1) # we shrink the range by one to insure no empty lists
    left = labels[:j]
    right = labels[j:]

    left = help_funk(left)      # We use the help function, instead of writing the same code twice for left and right
    right = help_funk(right)

    out = (left,right)
    return out


def generate_triplets(tree):
    if isinstance(tree, str):             # leaf
        return [tree], []                 # a leaf is nothing but a label and no triplets
    else:                                 # internal node
        left, right = tree                # we use that a binary tree always has two items at the root (left and right option)
        labels_L, trips_L = generate_triplets(left)     # we find all the labels and triplets from one side of the tree
        labels_R, trips_R = generate_triplets(right)    # and here the same for the other side

        labels = labels_L + labels_R    # we combine all the found labels
        trips  = trips_L + trips_R + anchored_triplets(labels_L, labels_R)  
                                    # anchored_triplets finds all the triplets that were previously split in left and right
        return labels, trips


def triplet_distance(tree1, tree2):
    Trip1 = generate_triplets(tree1)
    Trip2 = generate_triplets(tree2)
    
    Set1 = {val for val in Trip1[0]}
    Set2 = {val for val in Trip2[0]}
    n = len(Set1 & Set2)                # we convert the list of labels to sets and find the intersection

    triplet_distance = n * (n - 1) * (n - 2) / 6

    tripper1 = {val for val in Trip1[1]}
    tripper2 = {val for val in Trip2[1]}

    triplet_distance -= len(tripper1 & tripper2)
    return triplet_distance


# my_randome_tree = generate_tree(generate_labels(10))
# print(my_randome_tree)

# my_wack_tree = generate_triplets(((('A', 'F'), 'B'), ('D', ('C', 'E'))))
# print(len(my_wack_tree[1]))

# dis = triplet_distance(((('A', 'F'), 'B'), ('D', ('C', 'E'))),
#                         (((('D', 'A'), 'B'), 'F'), ('C', 'E')))
# print(dis)
'''
start_time = time.time()
generate_tree(generate_labels(4_400_000))
print("--- %s seconds ---" % (time.time() - start_time))

tree = generate_tree(generate_labels(275))
start_time = time.time()
generate_triplets(tree)
print("--- %s seconds ---" % (time.time() - start_time))
'''
