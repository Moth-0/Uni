"""
HANDIN 5 

This handin is done by:

202407098 Johanne Stubkjær
202408622 Magnus Overgaard
202405571 Jonas Ullgren

Reflection upon solution:

This was really a tough one for us.. We thought the triplet handins were more approachable because all the steps were kinda 
given. here we really had to think of our own stretagy. We tried several different paths, including ignoring recursion and
focusing solely on working with lists. we wrote a lot of pseudo code and sketched ideas. in the end, it was surprising to
realize that the amount of lines of code, ended up being a lot less, than we initially thought. this problem was great at
showing how recursion really can shine an be extremely usefull. the runtime grow exponentially with n (as expected). and 
around n=12 it becomes a mouthfull for the computer.. 
"""


def valid(r1, c1, r2, c2):
    if (r1 != r2) and (c1 != c2) and (abs(r1-r2)!=abs(c1-c2)):
        return True
    else:
        return False
    

def check_queen(queen, queens):
    r1, c1 = queen[0], queen[1]
    valiiid = []
    if queens==[]:
        valid_q = True #hvis det er den første dronning må du jo stille din dronning hvor du vil
    else: 
        for q in queens: #tjekker om dronning er tilladt af samtlige tidligere dronninger
            r2, c2 = q[0], q[1] 
            valid_queen = valid(r1, c1, r2, c2) #returnerer True hvis tilladt
            valiiid.append(valid_queen)
        valid_q = all(valiiid) #returnerer True hvis alle elementer i valiiid er True

    return valid_q


def check_row(r, queens, n, sol):

    columns = range(n)

    for c in columns:
        valid_q = check_queen((r,c), queens)
        if valid_q == True:
            new_queens = queens[:] #kopi
            new_queens.append((r,c)) #tilføj den tilladte dronning til listen af tilladte dronninger.
            if r+1 == n:
                sol.append(new_queens)
                return sol
            else:   
                check_row(r+1, new_queens, n, sol)
            
    return sol  


def board(sol, n):
    print(f'There are {len(sol)} solutions to The {n} Queens Puzzle')
    print('One of the solutions look like this:')
    for i in range(n):
        idx = sol[0][i][1]
        row = idx * ' # ' + ' Q ' + (n-idx-1) * ' # '
        print(row)


def sols(n):
    sol = check_row(0, [], n, [])
    board(sol, n)

sols(8)