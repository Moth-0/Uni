'''
    ZEROSUM

    Given a list of integers, find three integers in the list that sum to zero.

    Input:  A single line with n distinct integers separated by spaces, where
            3 <= n <= 5000 and each integer is in the range -10**10 to 10**10.
            It is guaranteed that the input contains a unique solution, i.e., 
            three exist integers x < y < z in the list such that x + y + z = 0.

    Output: A single line with the three integers that sum to zero, 
            separated by spaces and in increasing order.

    Example:

      Input:  -67 3 -11 -93 -32 7 9 -36 53 -12

      Output: -12 3 9
'''


input_list = sorted(list(map(int, input().split())))
n = len(input_list)
for i in range(n):
    a = input_list[i]
    left = i + 1
    right = n - 1
    while left < right:
        b = input_list[left]
        c = input_list[right]
        total = a + b + c
        if total == 0:
            print(a, b, c)
            exit()
        elif total < 0:
            left += 1
        else:
            right -= 1
