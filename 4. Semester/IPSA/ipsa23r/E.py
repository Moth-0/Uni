'''
    MISSING

    You are given two lists of names. The second list contains a subset of the
    names in the first list. Your task is to print the missing names from the
    first list in sorted order.

    Input:  The first line contains a positive integer n, the number of names 
            in the first list. Then follows n lines, each containing a name.
            Then follows a positive integer m, the number of names in the
            second list, followed by m lines, each containing a name.
            All names in each of the lists are distinct, and all names only
            contain letters. The second list is a subset of the first list.
            1 <= m <= n <= 100.

    Output: Sorted list of the names only in the first list, one name per line.

    Example:

      Input:  5
              Goofy
              Micky
              Scrooge
              Donald
              Daisy
              3
              Micky
              Daisy
              Goofy

      Output: Donald
              Scrooge
'''


# insert code
n = int(input())
names = [input() for _ in range(n)]

m = int(input())
sub_names = [input() for _ in range(m)]

missing = [x for x in names if x not in sub_names]

for p in sorted(missing):
    print(p)
