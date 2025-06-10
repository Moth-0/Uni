r'''
    LOWER BOUND

    Assume we have a tree where each node stores an integer value, and can
    have an arbitrary number of children.  Given a value minimum, we want to
    write a function lower_bound(tree, minimum) that returns the same tree,
    except that all values less than minimum are replaced by minimum. E.g.,
    
            7      minimum = 6     7
          / | \                  / | \
         /  |  \                /  |  \
        2   9   13     --->    6   9   13
        |       |              |       |
       -3       8              6       8
               / \                    / \
             12   1                 12   6

    Input:  The first line is a recursive Python tree structure, 
            where each node is a tuple (value, list of children).
            The second line is an integer minimum.

    Output: The same tree where values are increased to at least minimum.

    Example: 

      Input:  (7, [(2, [(-3, [])]), (9, []), (13, [(8, [(12, []), (1, [])])])])
              6

      Output: (7, [(6, [(6, [])]), (9, []), (13, [(8, [(12, []), (6, [])])])])

      This example is the same as the trees above.

    Note: The below code already reads the input and calls lower_bound.
'''


def lower_bound(tree, minimum):
    # insert code
    if isinstance(tree, int):
        return max(tree, minimum)
    else: 
        value, children = tree
        new_value = max(value, minimum)
        new_children = [lower_bound(child, minimum) for child in children]
        return (new_value, new_children)




tree = eval(input())
minimum = int(input())
print(lower_bound(tree, minimum))