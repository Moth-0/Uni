'''
    COMMON

    You are given a list of n names, and for each name a list of preferences (an
    unordered list of distinct values). The goal is to find the largest k such
    that at least two names have k preferences in common. Your task is to find k
    and list all such subsets of k preferences shared by at least two names, and
    list the names who share these preferences.

    Input:  The first line is an integer n, where 2 <= n <= 100. The following
            n lines each contain a name followed by a list of one or more
            preferences, all separated by spaces. The names and preferences
            consist only of lower and upper case letters. The names are unique.
            Each name has between 1 and 100 distinct preferences.

    Output: The first line contains two space separated integers k and s, where 
            k is the size of the largest subset of preferences shared by at
            least two names, and s is the number of such distinct subsets of
            size k. The following 2 * s lines contain for each of these s
            subsets of preferences in lexicographical order two lines (the sets
            are ordered as if a set was a sorted list of preferences): The first
            line the preferences in alphabetical order, separated by spaces, and
            the second line all names sharing these preferences, in alphabetical
            order and separated by spaces. It is guaranteed that k >= 1.

    Example:

      Input:  5
              Brittany Pineberry Mohsina MonsteraDeliciosa
              Liam Guava Loganberry Melon StarApple Pineberry
              Adam Cherimoya Pineberry Lychee Melon Plum Guava
              Joshua MonsteraDeliciosa Plum
              Arthur Thimbleberry Damson Orange Date Tangerine

      Output: 3 1
              Guava Melon Pineberry 
              Adam Liam
'''


# insert code
n = int(input())

dic = {}
subset = {}

for _ in range(n): 
    i = input().split()
    dic[i[0]] = set(i[1:])
    
for n1 in dic:
    for n2 in dic:
        if n1 != n2: 
            subset[" ".join(sorted([n1, n2]))] = dic[n1] & dic[n2]

subset = {i: sorted(j) for i, j in subset.items()}

k = max([len(x) for x in subset.values()])
pref = {y:x for y,x in sorted(zip(subset.keys(), subset.values()), 
                              key=lambda x: (x[1], x[0])) # Sorting a dict was with help from 
                              if len(x)==k}               # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value 
n = len(pref)
print(f"{k} {n}")

for p in pref: 
    print(" ".join(subset[p]))
    print(p)

    