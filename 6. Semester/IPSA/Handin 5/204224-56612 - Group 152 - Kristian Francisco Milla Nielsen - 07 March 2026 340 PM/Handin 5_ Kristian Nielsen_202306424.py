'''''
This is done by :
748507 Kristian Milla

Reflection upon solution:
"Min største indsigt var at se return result som en stafet, 
der sender den gyldige løsning hele vejen tilbage gennem kæden, 
indtil den når main()."
"Jeg lærte, at backtracking ikke kræver, at man sletter i listen, 
men blot ignorerer de grene, der fører til None, hvilket gør algoritmen 
utrolig elegant."
'''

def valid(r1, c1, r2, c2):
    return c1 != c2 and abs(r1 - r2) != abs(c1 - c2)

def print_solution(n, solution):
    for row, col in enumerate(solution):
        print('.' * col + 'Q' + '.' * (n - col - 1))
    for _ in range(n - len(solution)):
        print('.' * n)


def solve(n, solution):
    row = len(solution)
    #da første ingang i solution har row=0, har den sidste ingang len-1.
    #derfor er indgang "len" den næste row/ny dronning
    if row == n:
        return solution

    for col in range(n):
        if all(valid(row, col, r, solution[r]) for r in range(row)):
            #tjekker om den nye dronning er valid indtil den rammer en valid kolonne
            result = solve(n, solution + [col]) #så laver den en kopi of løsningen med ny dronning
            #og sender den videre til solve for at bygge på
            if result is not None: 
                return result 

    return None 

def main():
    n = int(input("Size of board: "))
    solution = solve(n, []) #sender en tom liste uden dronninger
    if solution:
        print_solution(n, solution)
    else:
        print(f"No solution exists for a {n}x{n} board.")

if __name__ == "__main__":
    main()