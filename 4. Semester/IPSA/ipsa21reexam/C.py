'''
    SUM AND BLANKS

    Print the number of input lines containing an integer and their sum.

    Input:  The first line contains an integer n, 1 <= n <= 100.
            The following n lines each contain a positive integer value or '-'.

    Output: A single line with two integers separated by a space.
            The first integer is the number of lines not containing '-',
            and the second integer is the sum of all lines not containing '-'.

    Example:

        Input:   3
                 2
                 -
                 5

        Output:  2 7
'''


# insert code

n = int(input())
sum = 0 
ints = 0

for _ in range(n): 
    i = input()
    if i != '-': 
        sum += int(i)
        ints += 1

print(f"{ints} {sum}")


