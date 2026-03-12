'''
HANDIN 5 (8 queen puzzle)

202307796 Oskar Juul Bjerre
202304778 Mathias Dahl Rahbek

Reflection upon solution:
We have used the hint in the assignment to solve the puzzle! In the valid
function we first check vertical and horizontal, then we check diagonal.
This is inspired by the rook and bishop of chess. To implement this we make
use of the fact that two points on the diagonal always have slope = 1.
We have also made the print function look like a chess board with number on the
rows and letters on the columns. We chose to have the solve function find all
possible solutions and print these. Also, we check how many solutions we find,
so that we can see that we find the expected number of solutions! We have also
implemented in the input, that if your input is invalid, meaning you set two
queens so that they can see each other, the program returns 'This solution is
invalid. Try again.'.
'''

n = int(input('Size of board: '))


def valid(r1, c1, r2, c2):

    if r1 == r2 or c1 == c2:    # Check row and column
        return False

    if abs(r1-r2) == abs(c1 - c2):  # Check diagonal
        return False

    return True


def print_solution(solution):
    grid = [[' . ' for _ in range(n)] for _ in range(n)]    # Make chess board
    for i, j in enumerate(solution):
        grid[i][j] = ' Q '  # Add queens
    for i, line in enumerate(grid):
        space = 1+len(str(n))-len(str(n-i))     # Ensure that the | align
        print(f'{n-i}'+' '*space+'|'+''.join(line))     # Print rows
    bottom_line = [chr(65 + i) for i in range(n)]
    print('   ' + '---'*len(bottom_line))   # Add bottom lines
    print('   '+' '*space + '  '.join(bottom_line))


def solve(solution, indent=0):
    global count    # Make sure 'count' can always be found
    if len(solution) == n:  # Basecase
        count += 1
        print(f'Solution nr. {count}:')
        print_solution(solution)
        return True

    for j in range(n):  # Try placing queen in every column
        i = len(solution)
        memory = 0
        for row, col in enumerate(solution):    # Check queen against all
            if valid(i, j, row, col):           # other queens
                memory += 1
        if memory == i:
            solution.append(j)  # Add queen
            solve(solution, indent=indent+1)    # Add next queen
            solution.pop()  # Remove queen so that the rest can be tried

    return


count = 0
nr_of_given_queens = int(input('Number of queens: '))   # Size of board input
solution = []
'''
for i in range(1, nr_of_given_queens+1):    # Add queens and check that they
    queen_column = int(input(f'Queen nr. {i} (column 1 - {n}): ')) - 1  # are
    for row, col in enumerate(solution):                                # valid
        if not valid(i-1, queen_column, row, col):
            print('Not a valid solution! Try again.')
            exit()
    solution.append(queen_column)
'''

print()
solve(solution)
if count == 0:
    print('There is no solution')
