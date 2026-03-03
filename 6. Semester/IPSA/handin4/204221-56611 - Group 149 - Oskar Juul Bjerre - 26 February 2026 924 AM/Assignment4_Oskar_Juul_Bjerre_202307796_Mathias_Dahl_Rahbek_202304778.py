'''
HANDIN 4 (triplet distance - part 2)

202307796 Oskar Juul Bjerre
202304778 Mathias Dahl Rahbek 

Reflection upon solution: 
We found this assignment very difficult. We don't really understand recursion,
when to use it nor how to use it. The most difficult part for us was part b). 
We spend at lot of time using list comprehension before finding out it was not
necesarry. We had trouble keeping tracks of the different types, e.g comparing
tuples to lists or strings, meaning our code wouldn't work. 
Furthermore, we found task d) unnecessary. What was the point of this? 
Lastly, we probably spend close to 14 hours doing this assignment and the 
exercsises accosiated with recursion, so exercises 8.
On e) we spent alot of time trying to print in the draw function, but once we
had the idea to generate the string first and then print last, it went much 
easier.
'''

# PREVIOUS ASSIGNMENT
import random
#a) 
def generate_label(n): 
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

# CURRENT ASSIGNMENT

#a)
def generate_tree(label): 
    # Create base-case
    if len(label) == 1:
        return label[0]
    
    # Create random slice of list
    slice = random.randint(1,len(label)-1) 
    left = tuple((label[:slice]))
    right = tuple((label[slice:]))

    return generate_tree(left),generate_tree(right)

#b)
def generate_triplets(tree):
    #Base-case
    if isinstance(tree,str):
        return [tree], []
    #Extract leaves and triplets from left and right side
    left_leaves, left_triplets = generate_triplets(tree[0])
    right_leaves, right_triplets = generate_triplets(tree[1])
    #Combine leaves
    all_leaves = left_leaves + right_leaves

    #Find anchored triplets between all nodes
    triplets = anchored_triplets(left_leaves,right_leaves)
    #Combine to all triplets
    all_triplets = left_triplets+right_triplets + triplets

    return all_leaves, all_triplets

#c) 
def triplet_distance(tree1, tree2): 
    #Get all triplets from both trees
    n1,triplets_1 = generate_triplets(tree1)
    n2,triplets_2 = generate_triplets(tree2)
    #Find set of common triplets
    common_triplets = set(triplets_1).intersection(set(triplets_2))
    #Number of labels in trees
    n = len(n1) 
    if set(n1) != set(n2): #This acounts for the case where the two trees have
                            #different number of labels
        n = len(set(n1).intersection(set(n2)))

    #Calculate triplet distance
    distance = n*(n-1)*(n-2)/6 - len(common_triplets)

    return distance 

#d)
'''
The function, generate_trees, can generate a tree with over 1e6 labels
in less than 2 seconds. Meaning the function is quite fast. 
The function, triplet_distance can calculate the distance between
the trees with 180 labels in about 11 seconds. Meaning it is much slower.
'''

#e) 
def valid_binary_tree(tree, indent = 0):
    if isinstance(tree, str):
        is_valid = len(tree) > 0
        return is_valid, [tree]
    if len(tree) != 2:
        return False, []
    left, right = tree

    ok_l, labels_l = valid_binary_tree(left, indent + 1)
    ok_r, labels_r = valid_binary_tree(right, indent + 1)
   
    # Combine results
    all_labels = labels_l + labels_r
    structurally_valid = ok_l and ok_r
   
    return structurally_valid, all_labels

def get_height(tree):
    if isinstance(tree, str): return 1
    labels = valid_binary_tree(tree)[1]
    return len(labels) + max(get_height(tree[0]),
                             get_height(tree[1]))

def print_ascii_tree(tree, depth = 0):
    heigth = get_height(tree)
    width = heigth*2 
    grid = [[' ' for _ in range(width)] for _ in range(heigth)]
    def draw(tree, indent = width // 2-1, depth = depth,
             is_right = False):
        if isinstance(tree, str):
                offset = 1 if is_right else 0
                grid[depth][indent + offset] = tree
                return []
        left, right = tree

        leg_length = len(valid_binary_tree(tree)[1])
        for i in range(leg_length):
            grid[depth + i][indent - i] = '/'
            grid[depth + i][indent + 1 + i] = '\\'

        draw(left, indent=indent-leg_length,
             depth=depth+leg_length)
        draw(right, indent=indent+leg_length,
            depth=depth+leg_length, is_right=True)
    draw(tree, depth=depth)
    print_grid = ''
    for line in grid:
        for x in line:
            print_grid += x
        print_grid += '\n'
    print(print_grid)

print_ascii_tree(((('A', 'F'), 'B'), ('D', ('C', 'E'))))