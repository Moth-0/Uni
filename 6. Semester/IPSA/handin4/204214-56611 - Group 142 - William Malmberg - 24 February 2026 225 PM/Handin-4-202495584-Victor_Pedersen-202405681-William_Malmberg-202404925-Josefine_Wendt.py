'''
HANDIN 4 (Triplet Distance part II)

This handin is done by (study ids and names of up to three students):

    202405584 Victor Kvist Loft Pedersen
    202405681 William Malmberg
    202404925 Josefine Ella Luci Sandy Dorothea Wendt

    Reflections upon solutions
    When making the recursive functions we always started with finding the basecase and then expanding
    from the bottom and up. The generate_triplets function was especially tricky, and it took us a while
    to realize that you have to unpack and repack the tuples in every recursion level.
    For the triplet distance we quickly realized how to compare two trees by using the set type.
    Everything else came to us in dreams.
'''
from random import randint

def generate_tree(label):
    if len(label) < 2:
        return label[0]
    pivot = randint(1, len(label)-1)
    return (generate_tree(label[:pivot]), generate_tree(label[pivot:]))

def canonical_triplets(A, B): 
    def pairs(L):
        _L = sorted(L)
        pair_list = [(_L[i], _L[j]) for i in range(len(_L)-1) for j in range(i+1, len(_L)) if i != j]
        return pair_list
    B_pairs = pairs(B)
    return [(A[i], B_pairs[j]) for i in range(len(A)) for j in range(len(B_pairs))]

def anchored_triplets(L, R):
    triplets = canonical_triplets(L, R) + canonical_triplets(R,L)
    return triplets

def generate_triplets(tree):
    if isinstance(tree, str):
        return ([tree], [])
    L, R = tree
    labels_L, triplets_L = generate_triplets(L)
    labels_R, triplets_R = generate_triplets(R)
    triplets = anchored_triplets(labels_L, labels_R)
    return (labels_L+labels_R, triplets_L+triplets_R+triplets)

def triplet_distance(tree1, tree2):
    labels1, triplets1 = generate_triplets(tree1)
    labels2, triplets2 = generate_triplets(tree2)
    n = len(labels1)
    overlap = set(triplets1) & set(triplets2)
    dist = n*(n-1)*(n-2)//6 - len(overlap)
    return dist

'''d) Our generate_tree can generate trees with 500,000 elements within 13 seconds.
Our triplet_distance can only calculate the distance for trees of size 400 within 13 seconds'''