'''
    RESTRICTED LABELS

    Create a generator labels(chars, n, k) that generates a sequence of
    all labels (strings) of length n and with at most k distinct characters
    (the same character is allowed multiple times), where all characters
    come from chars.  The labels should be generated in lexicographic order.

    Input:  A single line with a Python expression using the generator labels.
            It is guaranteeed that chars is a string of distinct lower case
            letters between 'a' and 'z' appearing in alphabetic order,
            and 0 <= n <= 10 and 0 <= k <= 10.

    Output: The result of evaluation the input expression.

    Example:

      Input:  list(labels('abc', 3, 2))

      Output: ['aaa', 'aab', 'aac', 'aba', 'abb', 'aca', 'acc',
               'baa', 'bab', 'bba', 'bbb', 'bbc', 'bcb', 'bcc',
               'caa', 'cac', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']

    Note: The below code already handles reading and evaluating the input.
'''


def labels(chars, n, k):
    # insert code
    if n == 0:
        yield ''
    else:
        for label in labels(chars, n - 1, k):
            for char in chars:
                new_label = label + char
                if len(set(new_label)) <= k:
                    yield new_label


expression = input()
print(eval(expression))
