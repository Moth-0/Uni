#Exercise 9.5 - handin 5 (eight queens puzzle)

#%%
'''
Jeg har brugt Gerths tilgang med 3 funktioner. Min solve funktion er rekursiv og
bruger valid og print solution undervejs.

Først definerer vi valid for at tjekke om en ny dronningeplacering er lovlig.
Den tager fire koordinater, to for den gamle brik og to for den nye.
Vi har betingelserne at rækker og kolonner ikke må være ens, men også at 'hældningen'
skal være forskellig fra 1, som svarer til diagonalen: |r2-r1|/|c2-c1|/=1.
Dette dækker alle diagonaler og sørger for dronningerne ikke angriber hinanden.
Funktionen returnerer True kun hvis alle 3 betingelser er opfyldt.

Så definerer vi print_solution, som skal tage en færdig solution
og kunne printe den, men også vide hvilket n-dronningeproblem det drejer sig om.
Formateringen er muligvis lidt hardcodet, men rækkerne ordnes meget fint med
et for loop over enumerate(solution). Hver række r kan defineres som c prikker
indtil dronningen Q optræder og så n - c - 1 prikker mere, så summen svarer til
ledige felter for en n løsning med én dronning placeret.

Det sværeste skridt er at få solve til at køre... I starten var jeg ude i at prøve
med en lang liste, der skulle gemme dronningeplaceringer, der var gode nok, men
indså at recursion jo gør alt det for én, hvis man kan få det til at virke.
Jeg var også meget i tvivl om jeg behøvede at gemme et resultat og returnere det
noget sted, men kom frem til, at vi egentlig bare skal sørge for at kalde 
solve rekursivt, hvis en ny placering er god nok og sørge for at alle recursions
der når i mål printer deres løsning.

Vi starter med en tom tuple - ingen dronninger placeret i nogen kolonner.
Vi tjekker altid først om vores base case er opfyldt, dvs. om vi har placeret
n gyldige dronninger endnu og kan printe en fuld løsning. Hvis ikke, fokuserer
vi på en ny tom række row = len(solution). For hver mulig kolonne i denne
række skal vi sikre os, at ingen dronninger angriber dette felt med valid(). 
Hvis de er gyldige, kalder vi solve igen rekursivt indtil base case og printer
hver eneste løsning. Return afslutter processen.
Til sidst bøvlede jeg med at få base case til at returnere True op igennem
recursion træet så vi kan printe at der ikke findes løsninger, hvis ikke der er.

'''

def valid(r1, c1, r2, c2):
    return r1 != r2 and c1 != c2 and abs(r2-r1) != abs(c2-c1)

def print_solution(solution, n):

    print("column  :", " ".join(str(i) for i in range(n)))

    for r, c in enumerate(solution):
        row = ". " * c + "Q" + " ." * (n - c - 1)
        print(f"row {r}   : {row}")
    
    print()

def solve(n, solution = ()):

    if len(solution) == n: #base case
        print_solution(solution, n) #når vi når base case printer vi en fuld løsning
        return True
    
    row = len(solution)
    success = False

    for col in range(n): #for hver kolonne i rækkerne i løsningen tjekkes dronninger
        queen_conflicts = [valid(r, c, row, col) for r, c in enumerate(solution)] 

        if all(queen_conflicts): #hvis ingen gamle dronninger angriber den nye
                if solve(n, solution + (col,)): #concatenate tuple col som er gyldig dronning!
                    success = True

    if solution == () and not success:
        print(f"There is no solution for the {n} Queens problem.") 

    return success

solve(n=8)
# %%
