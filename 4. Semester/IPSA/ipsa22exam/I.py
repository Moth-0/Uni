'''
    RESTRICTED QUEENS

    The k-RESTRICTED QUEENS problem is a variant of the eight queens
    puzzle, where we are given an n x n chessboard, and want to place
    a maximum number of k-RESTRICTED QUEENS, so that no k-restricted
    queen can reach another k-restricted queen in one move.
    A k-restricted queen is a queen that in one move can go at most k
    cells horizontally, vertically or diagonally.

    Note that n=8 and k=7 is the classic 8-queens puzzle.

    Input:  A line with two space separated integers n and k, where
            n is the size of the board, and k how far a queen can move.
            It is guaranteed that 2 <= k <= n <= 7.

    Output: The maximum number of k-restricted queens possible to
            place on an n x n chessboard.

    Examples:

      Input:  6 4

      Output: 8

        E.g. obtained by the following queen positions:

        Q....Q
        ..Q...
        ....Q.
        .Q....
        ...Q..
        Q....Q

      Input:  5 2

      Output: 5

        E.g. obtained by the following queen positions:

        .Q..Q
        .....
        Q....
        ..Q..
        ....Q

    Note: The below code already handles reading the input.
'''

def queens(n, k): 
    def solve(i, j, partial):
        if i >= n:
            return partial
        if j >= n:
            return solve(i + 1, 0, partial)
        for d in range(1, k + 1):
            for r, c in [(i, j - d), (i - d, j - d), (i - d, j), (i - d, j + d)]:
                if 0 <= r < n and 0 <= c < n and (r, c) in partial:
                    return solve(i, j + 1, partial)
        return max(solve(i, j + 1, {*partial, (i, j)}), solve(i, j + 1, partial), key=len)

    return len(solve(0, 0, set()))


n, k = map(int, input().split())
print(queens(n, k))
