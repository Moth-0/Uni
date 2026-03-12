#%%
#Exercise 9.5 - handin 5 (eight queens puzzle)

'''
HANDIN 5 (Handin 5 - Eight queens puzzle)

This handin is done by 
    202305360: Arunchand Suriyakumar

Reflection upon solution:
    The first part was to find a function that checked whether queens were in 
    danger to each other. This was done with use of vector and absoulute values

    Next the solve function is a recursive function where solution is empty at first.
    Recursively, the queens are placed such that they are not dangering already placed
    queens. This is checked using the valid function from part 1. Notice, this code
    only finds one of the solutions (if existing)

    Finally, a print function is made that prints the solution. Here, we made approtiate
    use of strings and function on strings as well. 

'''
#%%

n = int(input('Size of board: '))

def valid(r1, c1, r2, c2):
    v = [r2-r1, c2-c1]

    v_sq = (r2-r1)**2 + (c2-c1)**2

    if v_sq == abs(c2-c1)**2 or v_sq == abs(r2-r1)**2: #Checking same row and same colomm
        return False
    if abs(r2-r1) == abs(c2-c1): #Checking diagonal
        return False
    else:
        return True

def solve(solution):
    r = len(solution)

    #base case
    if r == n: #Working recursively upwards until we hit r = n (placed n queens)
        return solution

    for c in range(n): #For the given row, we take a look at each columm
            l = [valid(r, c, *position) for position in solution] #Now given a row and columm, we check with previous queens
            if all(l) == True: 
                solution_new = solution + [(r, c)]
                result = solve(solution_new)
                if result != 'No solutions':
                    return result #If there is a solution, this is returned
                
            
    
    return 'No solutions' #If there is no solutions, this is returned


def print_solution(solution):
    if solution == 'No solutions':
        return solution
    column = "".join(f'{col:<3}' for col in range(n)) #First part
    print(f'{"Column":<8}:  ' + f'{column}') 
    for pos in solution:
        i, col = pos
        row = []
        for x in range(n): #Placing a queen if the x matches the solution otherwise a dot is placed
            if x == col:
                row.append(f'{"Q":<3}')
            else: 
                row.append(f'{".":<3}')
        row = "".join(row)
        print(f'row {i:<4}:  {row}')

print_solution(solve([]))

# %%

# %%
