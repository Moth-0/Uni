r'''
    EXPLODE

    Given a tree represented by a recursive tuple, with single letters
    as leaves, create a function explode(tree) that recursively doubles
    all non-leaf nodes of the tree.

    A node with k children gets 2 * k children, where the recursive
    explosion of the i'th child becomes the 2 * i - 1 and 2 * i'th children
    of the resulting node.

    Example:
                                       o
                                      /||\
                                     / || \
                                    /  | \ \  
             o                     /   |  | \
            / \                   /    |  |  \
           /   C   explode       /     |  C   C
          o       --------->    /      |
         / \                   o       o
        A   B                 /|\     /|\
                             // \\   // \\
                            A A B B A A B B
                             
    Input:

       A recursive tuple representing a tree, where leaves are single
       capital letters.

    Output:

       A single line with the recursive tuple representing the exploded tree.

    Example:

       Input:  (('A', 'B'), 'C')

       Output: (('A', 'A', 'B', 'B'), ('A', 'A', 'B', 'B'), 'C', 'C')

    Note: The below code already takes care of handling the input and output.
'''


def explode(tree):
   # insert code
   if isinstance(tree, str): 
      return tree
   
   return tuple(explode(child) for child in tree for _ in range(2))
      


print(explode(eval(input())))
