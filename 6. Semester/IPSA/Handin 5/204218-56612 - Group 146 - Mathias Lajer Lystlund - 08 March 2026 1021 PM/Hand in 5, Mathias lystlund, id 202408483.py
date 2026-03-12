'''
HANDIN 5 (Eight queens puzzle)

This handin is done by Mathias Lystlund, id: 202408483

Reflection upon solution:
My solution to the Eight-Queens puzzle uses recursion and backtracking to place queens
one row at a time. I store the column positions of queens in a list instead of 
representing the entire board. For each row, we test possible columns and check for 
conflicts with earlier queens. If a conflict occurs, the algorithm backtracks and tries 
another position. Some of the solution is inspired by the logic of the solution to the Maze.
'''

n = 8

def check(r1, c1, r2, c2 ):
    
    if r1 == r2 or c1 == c2:
        return False
    elif abs(r2-r1) == abs(c2 - c1):
        return False
    else:
        return True
    


print(check(r1=1, c1=2, r2=2, c2=2))

def print_solution(n, solution):
    
    for r in range(n):
        if r < len(solution):
            c = solution[r]
            print("." * c + "Q" + "." * (n - c - 1))
        else:
            print("." * n)




def solve(n, solution):
    if len(solution) == n:
        return True

    row = len(solution)

    for col in range(n):
        ok = True
        for r2, c2 in enumerate(solution):
            if not check(row, col, r2, c2):
                ok = False
                break

        if ok:
            solution.append(col)
            if solve(n, solution):
                return True
            solution.pop() 

    return False




solution = []
if solve(n, solution):
    print(True)
    print_solution(n, solution)
else:
    print(False)