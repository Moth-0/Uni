'''
    COVERAGE

    Given a set of n points and m circles, determine how many points are 
    contained in at least one circle. We say a point is contained in a circle 
    if it inside or on the boundary of the circle.

    E.g., if we have four points (0, 0), (0, 10), (10, 0), and (10, 10),
    and two circles with centers (1, 1) and (5, 12) and radii 5 and 6,
    respectively, then the first point is contained in the first circle,
    and the second and fourth points are contained in the second circle. 
    The third point is not contained in either circle. Thus, the answer is 3.

    Input:  The first line contains two integers n and m, separated by space,
            where 1 <= n <= 100 and 1 <= m <= 100. The next n lines contain 
            two integers x and y each, separated by space, representing the
            coordinates of a point. The next m lines contain three integers 
            cx, cy, and r each, separated by spaces, where (cx, cy) is the
            center of a circle with radius r.

    Output: An integer, the number of points contained in at least one circle.

    Example:

      Input:  4 2
              0 0
              0 10
              10 0
              10 10
              1 1 5
              5 12 6

      Output: 3
'''


# insert code
points, circles = map(int, input().split())

p_list = []
c_list = []

count = 0

for _ in range(points): 
    x, y = map(int, input().split())
    p_list.append((x, y))
for _ in range(circles):
    x, y, r = map(int, input().split())
    c_list.append((x, y, r))

for p in p_list: 
    x, y = p
    for c in c_list: 
        c1, c2, r = c
        if (x-c1)**2+(y-c2)**2 <= r**2: 
            count += 1
            break

print(count)