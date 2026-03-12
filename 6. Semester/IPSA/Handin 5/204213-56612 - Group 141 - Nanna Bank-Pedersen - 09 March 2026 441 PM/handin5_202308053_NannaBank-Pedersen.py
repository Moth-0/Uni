'''
HANDIN 5 (eight queens puzzle)

This handin is done by:
    202308053 Nanna Bank-Pedersen

Reflection upon solution:
Det mest udfordrende ved opgaven var at lave solve funktionen rekursivt, og at forstå hvordan
man kunne bygge løsningen ved at tilføje en kolonne for hver række. Det krævede også at man
skulle tjekke om en placering var tilladt ved at sammenligne med allerede placerede dronninger.
Løsningen gemmes som en liste med index som række og værdi som kolonne, hvilket jeg synes er meget praktisk.
Print funktionen var også lidt tricky, da jeg lige skulle tænke over hvordan jeg kunne hente informationen 
fra løsningen for at printe. 
Det nemmere ved opgaven var valid funktionen, som bare tjekker om der er to på samme række eller diagonal.
Jeg antager at inputtet n er et positivt heltal, men har ikke lavet nogen 
begrænsninger på det i koden.
'''
def valid(r1, c1, r2, c2):
    #række
    if c1 == c2:  
        return False
    #diagonal 
    if abs(c1 - c2) == abs(r1 - r2):  
        return False
    return True


def print_solution(solution, n):
    for r in range(n):
        row = ""
        for c in range(n):
            row += "Q" if solution[r] == c else "."
        print(row)


def solve(solution, n):
    row = len(solution)

    #gyldig løsning
    if row == n:
        return solution

    for col in range(n):
        allowed = True
        for r in range(row):
            if not valid(r, solution[r], row, col):
                allowed = False
                break

        if allowed:
            result = solve(solution + [col], n)
            if result is not None:
                return result

    return None


def main():
    n = int(input("Angiv n: "))
    solution = solve([], n)

    if solution:
        print_solution(solution, n)
    else:
        print("Findes ingen løsning.")


if __name__ == "__main__":
    main()