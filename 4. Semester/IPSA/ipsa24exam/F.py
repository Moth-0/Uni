'''
    ISOLATED

    Given a set of n points and a distance d, report the number of isolated 
    points, i.e., the number of points where all other points have Euclidean
    distance at least d to the point.

    Input:  The first line contains an integer n, 0 <= n <= 100,
            the number of points.
            The second line contains an integer d, 1 <= d <= 10_000,
            the distance.
            The next n lines each contains a point consisting of two space
            separated integers x and y, -1000 <= x <= 1000 and
            -1000 <= y <= 1000. Points are not necessarily distinct.

    Output: A single integer, the number of points where all other points have
            Euclidean distance at least d to the point.

    Example: 

      Input:  4
              4
              -3 0
              0 0
              3 3
              3 -3

      Output: 2

      The only isolated points are (3, 3) and (3, -3). They both have (0, 0)
      as the nearest point, with distance sqrt(18) > d = 4.
'''

# insert code
n = int(input())
d = int(input())

count = 0

points = [tuple(map(int, input().split())) for _ in range(n)]

for i, (xi, yi) in enumerate(points):
    if all((xi - xj)**2 + (yi - yj)**2 >= d**2 for j, (xj, yj) in enumerate(points) if j != i):
        count += 1

print(count)