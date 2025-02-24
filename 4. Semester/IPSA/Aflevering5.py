"""
HANDIN 5 - eight queens puzzle

This handin is done by: 
    202307989 Mikkel Moth Billing 

Reflection upon solution: 

"""

def valid(r1, c1, r2, c2):                          # Checks rows, coloumns and diagonals
    if r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
        return False
    else: 
        return True
    
def print_solution(solution):                       # For printing the board 
    rows = len(solution)
    print(rows * " - ")
    for i in range(rows): 
        print(solution[i] * " . " + " Q "+ (rows - solution[i]-1) * " . ")
    print(rows * " - " + "\n")

def solve(solution): 
    global n, found_solution
    if len(solution) == n:                          # If we have a full solution
        print_solution(solution)                    # Print the solution
        found_solution = True                       # We found a solution
    
    
    row = len(solution)                             # Current row we want to place queen
    for c in range(n):                              # For every coloumn
        safe = True                                 # Assume the location is safe 
        for r in range(row):                        # Check with every row
            if not valid(r, solution[r], row, c):   # Check if queen can't be placed at location
                safe = False                        # If it cant location is not safe 
                break                               # If we found a row where there is attacking queen,
                                                    # we don't need to check the remaning rows
                
        if safe == True:                            # When we have checked all the rows, 
            solve(solution + [c])                   # and none are unsafe, run recursion with the added queen
            

n = input("n: ")                                    # n input
found_solution = False

solve([])

if not found_solution:                              # If we didn't find solution
    print("No solution")