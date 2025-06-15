'''
    FRESH

    Your task is to create a generator function fresh(sequence),
    that takes an iterable sequence (finite or infinite), and generates
    the same sequence of values, but only yielding the first
    occurence of a value.

    An example usage could be:

        > g = fresh([1, 2, 1, 4, 2, 3, 1])
        > next(g)
        1
        > next(g)
        2
        > next(g)
        4
        > next(g)
        3
        > next(g)
        StopIteration

    Input:  A Python expression using the fresh generator.

    Output: The evaluation of the input expression returns an iterable
            object. Print all elements of the iterable on a single
            line separated by spaces.

    Example:

      Input:  fresh([1, 2, 1, 4, 2, 3, 1])

      Output: 1 2 4 3

    Note:

      The below code already takes care of handling input and output. 
'''


def fresh(sequence):
    # insert code
    used = set()
    for s in sequence: 
        if s not in used: 
            used.add(s)
            yield s
    

print(*eval(input()))
