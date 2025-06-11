'''
    INCREASING DEQUE

    Given a list of n distinct integers, you task is to find the maximum length
    of a subsequence of the integers (not necessarily consecutive) that can be
    processed from left-to-right, where each integer is either inserted into a 
    deque at the front or back, such that the deque is sorted in increasing order.

    Input:  A line with a sequence of n space separated distinct integers, 
            1 <= n <= 100.

    Output: The maximum length of a subsequence that can be inserted into a
            deque such that the deque always is sorted in increasing order, 
            when processing the integers from the subsequence left-to-right.

    Example:

      Input:  7 2 5 10 9 1 6

      Output: 4

      E.g., after the subsequence 2 5 9 1 (containing 4 integers) is inserted 
      into the deque, by first inserting 2, and pushing 5 and 9 on the back, 
      and 1 on the front, the deque contains in increasing order 1 2 5 9.
      Note that the subsequence obtaining a maximal length increasing deque 
      is not necessarily unique. Inserting the subsequence 7 5 9 1 would also
      result in an increasing deque 1 5 7 9 of length 4.
'''


# insert code
values = list(map(int, input().split()))
n = len(values)

lis = [1] * n  # lis[i] = longest increasing subsequence starting at i
lds = [1] * n  # lds[i] = longest decreasing subsequence starting at i
for i in reversed(range(n)):
    for j in range(i + 1, n):
        if values[i] < values[j]:
            lis[i] = max(lis[i], 1 + lis[j])
        elif values[i] > values[j]:
            lds[i] = max(lds[i], 1 + lds[j])

print(max([inc + dec - 1 for inc, dec in zip(lis, lds)], default=0))
