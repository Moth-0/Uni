r'''
    CENTER
    
    Assume we are given a binary tree, where each node is labeled with a
    unique label A-Z, and each node has a left and right child (which can 
    be None). We call a node a center of the tree if the removal of the node
    and its adjacent edges leaves the resulting (at most three) subtrees being
    of size at most half of the original tree. We assume a tree is represented
    by a recursive tuple (label, left subtree, right subtree).
    
    For example, in the below tree the node B is the unique center. 
    The original tree has size 6, and the three resulting subtrees by 
    removing B have sizes 2, 2, and 1.

            A
           / \
          B   F          A            C
         / \       ->     \      +     \     +    E
        C   E              F            D
         \
          D
          
        ('A',('B',('C',None,('D',None,None)),('E',None,None)),('F',None,None)) 

    Note that the center is not necessarily unique as both B and C are centers
    in the below example.

              A 
             /      
            B
           / 
          C
         /
        D

        ('A', ('B', ('C', ('D', None, None), None), None), None)

    Your task is to write a function centers(tree) that takes a tree and
    returns a sorted list of the labels of all possible centers of the tree.

    Input:  A single line containing a Python expression representing a tree.

    Output: A sorted list with all centers of the tree.

    Example:

      Input:  ('A', ('B', ('C', ('D', None, None), None), None), None)

      Ouput: ['B', 'C']

    Note: The below code already reads the input, calls the centers function,
          and prints the returned result.
'''


def centers(tree):
    
    #> find labels
    labels = set()
    
    def validate(tree):
        if tree == None:
            return
        assert isinstance(tree, tuple)
        label, left, right = tree
        assert isinstance(label, str)
        assert label not in labels
        assert len(label) == 1 and 'A' <= label <= 'Z'
        labels.add(label)
        validate(left)
        validate(right)

    validate(tree)

    #> solution
    def solve(tree):  # returns size of tree
        if tree == None:
            return 0
        label, left, right = tree
        left_size = solve(left)
        right_size = solve(right)
        candidates.append((label, left_size, right_size))
        return 1 + left_size + right_size
    
    candidates = []
    size = solve(tree)
    center_nodes = [label for label, left_size, right_size in candidates
                    if size - left_size - right_size - 1 <= size / 2 
                    and left_size <= size / 2 
                    and right_size <= size / 2]

    return sorted(center_nodes)


print(centers(eval(input())))
