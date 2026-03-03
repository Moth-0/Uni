#%%
#Exercise 8.8 - handin 4 (triplet distance - part II)
'''
HANDIN 4 (Triplet distance - part 2)

This handin is done by 
    202305360: Arunchand Suriyakumar

Reflection upon solution:
    In part A: We make the recursive function by following steps: Basecase, reduction, leap, combine. 
    This means that we define the simples case of the function (basecase). Then we reduce the problem
    by splitting the input list. The recursively use the function on the two new lists. And finally, we
    combine. 

    In part B: At the same time, we go through every path in the tree and collect the leafes and use the
    anchored-triplet function to generate the triplets at each node. 

    In part C: We directly use the formula for triplet distance. We find n as the number of leafes, which
    can be found using the function from part B. By using "set" on the anchored-triplets for each tree
    and looking at the overlap, we then find the number "i" that we subtract to find triplet distance. 

    In part D: We run through a list of possible number of labels n. We generate a list with n labels. 
    Then use the function to generate a random binary tree and finally the triplet distance. 
    We used the "time" function to find running time. At n = 400, we get a running time of 12 s. 
'''
############################
#From previous task:
from random import randint
from time import time


#a
def generate_label(n):
    list = [chr(65+x) for x in range(n)]
    return list


#b
def permute(L):
    permuted_list = [L.pop( randint(0, len(L)-1) ) for _ in range(len(L))]
    return permuted_list
    

#c
def pairs(L):
    pairs = [(x,y) for x in L for y in L if x<y]
    return pairs


#d
def canonical_triplets(L1, L2): 
    result = [(x, y) for x in L1 for y in pairs(L2)]
    return result

#e
def anchored_triplets(L, R): 
    result1 = canonical_triplets(L,R)
    result2 = canonical_triplets(R,L)
    result = result1 + result2
    return result

############################

#%%
#A
def generate_tree(labels):
    #Basecase
    if len(labels) == 2:
        return tuple(labels)
    if len(labels) == 1:
        return labels[0]
    
    #Reduction
    r = randint(1, len(labels)-1) #Such that we cannot get empty lists
    left, right = labels[:r], labels[r:]

    #Leap
    left_tree = generate_tree(left)
    right_tree = generate_tree(right)

    #Combine
    result = (left_tree, right_tree)

    return result
# %%
#B
def generate_triplets(tree):
    if isinstance(tree, str):
        return [tree], []

    
    left, right = tree[0], tree[1]


    labels_left, triplets_left = generate_triplets(left)
    labels_right, triplets_right = generate_triplets(right)


    triplets = triplets_right + triplets_left + anchored_triplets(labels_left, labels_right)
    labels = labels_left + labels_right

    return (labels, triplets)


#%%
#C
def triplet_distance(tree1, tree2):
    n = len(generate_triplets(tree1)[0])

    set1 = set(generate_triplets(tree1)[1])
    set2 = set(generate_triplets(tree2)[1])

    overlap = set1 & set2 #Overlap
    i = len(overlap)

    distance = n*(n-1)*(n-2)/6 - i    
    
    return distance


#%%
#D
'''
ns = [10, 100, 400] #leafes

for n in ns:
    labels = generate_label(n)
    start = time()
    tree1 = generate_tree(labels)
    end = time()
    time_tree1 = end-start

    tree2 = generate_tree(labels)

    start = time()
    d = triplet_distance(tree1, tree2)
    end = time()
    time_triplet = end - start

    print(f'{n} leafes: Time to generate tree: {time_tree1:.3} s, Time to calculate triplet distance: {time_triplet:.3} s')

'''

