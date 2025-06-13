'''
    TYPO

    Note: This problem builds upon problem G (KEYBOARD).

    Assume a text is typed on a keyboard with a specific layout, e.g.

        Q..W..E..R..T..Y..U..I..O..P
        ............................
        .A..S..D..F..G..H..J..K..L..
        ............................
        ..Z..X..C..V..B..N..M.......

    where '.' indicates spaces between keys.  The text only consists of
    a single word, but unfortunately some typos have been introduced.
    Your task is to find the "closest" word in a dictionary to the typed text.

    We define the "distance" between two keys to be the number of columns
    plus rows to be moved from getting from one key to the other, e.g.
    from 'S' to 'C' one has to move 4 columns to the right and 2 rows down,
    i.e. the distance is 4 + 2 = 6.

    The "keyboard distance" between two words word1 and word2 is the total cost
    of a sequence of edits to come from word1 to word2, where an arbitrary
    character can be deleted or inserted with a cost of 5, or a character
    can be changed to another character with cost equal to the distance
    between the two characters on the keyboard.

    Input:  The first line contains the typed text.  The text has length
            between 1 and 20, and all characters are capital letters.
            The second line contains an integer n, the number of rows in
            the keyboard layout, where 1 <= n <= 10.  Then follows n lines
            describing the layout of the keyboard.  All n lines have equal
            length and contain only '.' and 'A' to 'Z'.
            Each letter occurs exactly once.
            Then follows a line with an integer w, the number of words in
            the dictionary, followed by w lines containing the words in the
            dictionary in alphabetic order. It is guaranteed that
            1 <= w <= 1000 and each has length <= 20.

    Output: The first line contains a single integer, the minimum keyboard
            distance between the typed text and a word in the dictionary.
            The following lines should contain all words in the dictionary
            (in alphabetic order) with this keyboard distance to the typed
            text.

    Example:

      Input:  PYYNM
              5
              Q..W..E..R..T..Y..U..I..O..P
              ............................
              .A..S..D..F..G..H..J..K..L..
              ............................
              ..Z..X..C..V..B..N..M.......
              6
              JAVA
              MODULA
              OCAMEL
              PASCAL
              PYTHON
              SIMULA

      Output: 14
              PYTHON

      Note:   That PYYNM and PYTHON have keyboard distance 14 follows from:

                PYYNM  ->  replace Y by T, cost 3  ->
                PYTNM  ->  replace N by H, cost 1 + 2  ->
                PYTHM  ->  insert O, cost 5  ->
                PYTHOM ->  replace M by N, cost 3  ->
                PYTHON

              The keyboard distance of PYYNM to the other words in the dictionary:
              JAVA (37), MODULA (38), OCAMEL (37), PASCAL (41), and SIMULA (40).
'''


# insert code
pass
