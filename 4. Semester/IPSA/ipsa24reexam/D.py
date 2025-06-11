'''
    DOUBLE WORDS

    Given a string find all words that appear twice in a row in the string.

    E.g., in the below string the words 'TREES' and 'BIRDS' appear twice in a row.

      THE FOREST CONTAINS TREES TREES TREES AND MORE TREES AND BIRDS BIRDS AND BIRDS

    Input:  A singe line containing a string of words separated by spaces. 
            Each word contains uppercase letters only.

    Output: A single line with the words that appear twice in a row in the 
            string, with no word repeated in the output, and the words appearing
            sorted in alphabetical order. If no word appears twice in a row,
            output '-'.

    Example:

      Input:  THE FOREST CONTAINS TREES TREES TREES AND MORE TREES AND BIRDS BIRDS AND BIRDS

      Output: BIRDS TREE
'''


# insert code
line = input().split()
out = []
for i in range(len(line)-1):
    if line[i] == line[i+1] and line[i] not in out:
        out.append(line[i])
if out == []:
    out = '-'
else: 
    out = " ".join(sorted(out)) # Denne linje er fra https://stackoverflow.com/questions/12309976/how-do-i-convert-a-list-into-a-string-with-spaces-in-python

print(out)