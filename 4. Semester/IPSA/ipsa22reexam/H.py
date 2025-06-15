r'''
    NO UNARY

    Consider trees represented by recursive tuples, where all leaves
    are strings and internal nodes are tuples.  Below are two examples
    of such trees, where * denotes a tuple.  Your task is to implement
    a function remove_unary(tree) that removes all unary internal
    nodes from a tree by replacing a node with a single child by the
    single child.

     ((('A', 'B'),), 'C', ('D',))   (('A', 'B'), 'C', 'D')

                *                             *
               /|\                           /|\ 
              / | \                         / | \
             /  |  \     remove_unary      /  |  \
            *  'C'  *      ------->       *  'C' 'D'
            |       |                    / \
            *      'D'                 'A' 'B'
           / \
         'A' 'B'

    Input:  A Python expression using the function remove_unary.
            It is guaranteed that all tuples in the representation
            of a tree contain at least one element.

    Output: The result of evaluating the input expression.

    Example:

      Input:  remove_unary(((('A', 'B'),), 'C', ('D',)))

      Output: (('A', 'B'), 'C', 'D')

    Note: The below code already handles reading the input and
          printing the output of evaluating the expression.
'''


def remove_unary(tree):
    # insert code
    pass


print(eval(input()))
