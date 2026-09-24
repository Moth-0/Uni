'''
    EXPAND

    In this task you are given a list of words of capital letters, some possibly
    abbreviated to <prefix>*, where <prefix> is a sequence of capital letters. 
    Your task is to expand all abbreviated strings to the most recently output 
    string with a matching prefix.

    Input:  The first line contains an integer n, where 1 <= n <= 100.
            The next n lines each contain a word with 1 to 25 characters, 
            all upper case letters, except the last character that can be '*'.

    Output: n lines, where the i'th output line equals the i'th input string
            if this string only contains upper case letters. If the i'th input 
            string ends with '*', the i'th output line equals the most recent 
            output line before the i'th output line with a prefix matching the 
            characters before '*' (possibly the empty string, like in the second 
            last input line in the example below). It is guaranteed that such a 
            line exists.

    Example:

      Input:  7
              AARHUS
              DENMARK
              COPENHAGEN
              DEN*
              A*
              *
              C*

      Output: AARHUS
              DENMARK
              COPENHAGEN
              DENMARK
              AARHUS
              AARHUS
              COPENHAGEN
'''


# insert code
n = int(input())

text = [input() for _ in range(n)]

for i in range(len(text)): 
    j = i # Save index
    while text[i][-1] == "*": # if word has * 
        # check if word before starts with text[j][:-1]
        if text[j-1].startswith(text[i][:-1]): 
            text[i] = text[j-1] # If yes replace word j with word i
        else: 
            j -= 1 # else move to word above 

for t in text:
    print(t)