'''
HANDIN 5 (eight queens puzzle)

This handin is done by (study ids and names of up to three students):

    202406267 Andreas Wind

Reflection upon solution:
    Det var en rigtig svær opgave det her, og en del af den er løst med
    hjælp fra AI. Jeg har primært brugt AI til at hjælpe mig med at bygge
    en struktur for rektusionen. 
    Derfor har jeg skrevet en masse kommentarer for at sørge for at jeg 
    forstår det hele. Specielt det her med True og False inde i loopet 
    er vanskeligt at forstå, men det er en rigtig smart måde at holde 
    styr på at kunne vise programmet om der er fundet en løsning endnu.

    
'''


def valid(r1, c1, r2, c2):
    # de må ikke dele række, søjle eller diagonal
    # hvis de er på samme diagonal er forskellen i abs-værdi af
    # differensen af rækker og søjler 0
    if (r1 != r2) and (c1 !=c2) and (abs(r1 - r2) - abs(c1-c2) != 0):
        return True
    else:
        return False
    

def print_solution(solution, n):
    print(f"Size of board: {n}")
    print(solution)
    for i in range(n):
        col = solution[i] # der skal være et Q ved dette index
        print("." * col + "Q" + "." * (n - col - 1))

def solve(solution, n):

    # base case. Hvis der er n dronninger placeret og alle er valid så
    # er problemet løst.
    if len(solution) == n:
        print_solution(solution, n)
        return True # returner true for at "fortælle" ydre funktioner at
                    # der er fundet en løsning
    
    else:
        r2 = len(solution)
        for c2 in range(n):

            all_OK = True # når ingen dronninger er placeret er løsningen
                          # som udgangspunkt valid
            for r1, c1 in enumerate(solution): # looper over tidligere løsninger
                if not valid(r1, c1, r2, c2):
                    all_OK = False # nu er alle ikke okay længere
                    break
            if all_OK: # hvis alle er kørt igennem og ingen er "invalid"
                if solve(solution + [c2], n):
                    return True # returnerer True for at vise at her er en løsning
        return False # return false sker hvis der ikke er fundet en løsning



solutions = []
n_inp = int(input("> "))

løsning = solve([], n_inp)

if not løsning:
    print("No solution")