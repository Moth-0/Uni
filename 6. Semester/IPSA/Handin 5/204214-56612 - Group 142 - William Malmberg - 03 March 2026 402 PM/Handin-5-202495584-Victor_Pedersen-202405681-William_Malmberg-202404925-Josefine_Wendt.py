'''
HANDIN 5 (eight queens puzzle)

This handin is done by (study ids and names of up to three students):

    202405584 Victor Kvist Loft Pedersen
    202405681 William Malmberg
    202404925 Josefine Ella Luci Sandy Dorothea Wendt

    Reflections upon solutions
    It was very hard for our mortal minds to have the base case being an expanded version of
    the input. At the same time we had some problems how to do the backtracking because when
    it had gone down a false road it was not capable to get out of it again giving wrong boards/
    solutions.
'''
n =int(input("How big should the board be?"))

def valid(r1, c1, r2, c2):
    if c1 == c2:
        return False
    if abs(r1 - r2) == abs(c1 - c2):
        return False
    return True

def print_solution(solution):
    for queen in solution:
        print('.'*(queen)+'Q'+'.'*(n-queen-1))

def solve(solution):
    # Base case / Final solution found
    if len(solution) == n:
        sol_found = True
        return solution
    
    # The queen to be placed
    row = len(solution) 

    # Placed queen in all coloumns
    for col in range(n): 
        # Checks if the queen is valid for all previously placed queens
        if all([valid(i, queen, row, col) for i, queen in enumerate(solution)]): 
            # Recursivly check next queen
            result = solve((*solution, col))
            # Result is none until solution is found
            if result:
                return result

for i in range(n): # Checks all starting positions
    if solve((i,)):
        print_solution(solve((i,)))
        print()