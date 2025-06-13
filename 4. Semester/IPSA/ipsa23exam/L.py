'''
    STONE THROWING

    Assume we have n points in the plane we can be in, and we start in an 
    arbitrary one of these points. In order to move from one point to another 
    point, we must throw a stone from the point we are in to the point we want
    to move to.  Unfortunately, throwing takes energy, so the next throw will 
    always be strictly shorter than the previous throw. I.e., moving from one 
    point p to another point q causes the next move to be strictly shorter than 
    the distance from p to q, and in particular we cannot move directly back 
    from q to p in the next move. The first throw can be of arbitrary length.

    As an example consider the following nine grid points below. 

        (3, 1) (3, 2) (3, 3)
        (2, 1) (2, 2) (2, 3)
        (1, 1) (1, 2) (1, 3)

    A possible longest valid point sequence is the following six points:

        (1, 1), (3, 3), (1, 2), (3, 2), (2, 1), (1, 1)

    The first move is from (1, 1) to (3, 3) with square distance 
    (3 - 1) ** 2 + (3 - 1) ** 2 = 8, and the next move is from (3, 3) to
    (1, 2) with square distance (1 - 3) ** 2 + (2 - 3) ** 2 = 5, and so on.
    Note that the point (1, 1) appears twice in the sequence.

    Input:  The first line contains an integer n, the number of points,
            where 1 <= n <= 100. The next n lines each contain two integers
            x and y, separated by a space, with the coordinates of the points. 
            It is guaranteed that all points are distinct.

    Output: The maximum number of points in a valid point sequence.

    Example:

      Input:  9
              1 1
              1 2
              1 3
              2 1
              2 2
              2 3
              3 1
              3 2
              3 3

      Output: 6
'''


# insert code
import functools
n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

def dist(i, j):
    px, py = points[i]
    qx, qy = points[j]
    return (px - qx) ** 2 + (py - qy) ** 2

@functools.cache
def solve(i, limit):
    answer = 1
    for j in range(n):
        if i != j and dist(i, j) < limit:
            answer = max(answer, 1 + solve(j, dist(i, j)))
    return answer

answer = max(solve(i, float('inf')) for i in range(n))
print(answer)