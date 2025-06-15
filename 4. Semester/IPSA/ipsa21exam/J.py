'''
    LABELS

    Your task is to create a generator function
    labels(symbols, length), that can generate all labels
    with exactly length characters and all characters
    come from symbols. The labels should be generated in
    alphabetical/lexicographical order.

    An example usage could be:

        > g = labels('abc', 4)
        > next(g)
        'aaaa'
        > next(g)
        'aaab'
        > next(g)
        'aaac'
        > next(g)
        'aaba'
        > next(g)
        'aabb'

    Input:  A Python expression using the labels generator, where
            1 <= len(symbols) <= 25 and 1 <= length <= 25.
            The letters in symbols appear alphabetically sorted.

    Output: The evaluation of the input expression returns
            an iterable object. Print all elements of the
            iterable on a single line separated by spaces.

    Example:

      Input:  list(labels('xy', 3))

      Output: xxx xxy xyx xyy yxx yxy yyx yyy

    Note:

      The below code already takes care of handling input and output. 
'''


def labels(symbols, length):
    # insert code

    pass
    

print(*eval(input()))
