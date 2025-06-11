r'''
    INORDER MIRROR

    In this problem we consider the problem of mirroring a binary tree. 
    We assume that each node stores a value, and that the tree is represented 
    by a recursive tuple (left, value, right), where an empty tree is 
    represented by None. The mirror of a tree is obtained by recursively
    reversing the order of the children of each node.

    Example:

          3              3
         / \            / \
        1   4    ==>   4   1
         \     mirror     /
          2              2
               
      T = ((None, 1, (None, 2, None)), 3, (None, 4, None))
      mirror(T) = ((None, 4, None), 3, ((None, 2, None), 1, None))

    Input:  A recursive tuple representing a binary tree T where all values are 
            distinct integers. The tree has been 1 and 100 nodes.

    Output: A recursive tuple representing the mirror of the tree T.

    Example:

      Input:  ((None, 1, (None, 2, None)), 3, (None, 4, None))

      Output: ((None, 4, None), 3, ((None, 2, None), 1, None))

    Note: The below code already takes care of reading the tree and printing
          the result of calling mirror(tree). Your task is to implement
          the function mirror.
'''


def mirror(tree):
    # insert code
    if tree == None:
        return None
    right, value, left = tree
    return (mirror(left), value, mirror(right))
    


tree = eval(input())
print(mirror(tree))
