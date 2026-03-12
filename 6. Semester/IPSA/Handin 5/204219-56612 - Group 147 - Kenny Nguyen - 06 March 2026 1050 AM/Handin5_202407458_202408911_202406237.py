'''
HANDIN 5 (eight queen puzzle)

This handin is done by (study ids and names of up to three students):

    202407458 Kenny Nguyen
    202408911 Safiya Chebil 
    202406237 Marie Schnoor - Madsen 

    
Reflection upon solution:

    Det svære i denne aflevering var opstilling af de forskellige funktioner og der egenskaber. 
    Et andet problem var at strukturere selve koden og forstå hvad de forskellige funktioners 
    formål var. 
'''



solution = []

def tegn_bræt(D): 
    for i in range(0,len(solution)):
        string = f'{i} |'
        for j in range(0,D):
            if j == solution[i] :
                string += f"  Q  "
            else: 
                string += f"  .  "
        print(string)


def valid(r1, c1, r2, c2): 
    if abs(r1 - r2) == abs(c1 - c2) or r1 == r2 or c1 == c2:
        return False
    return True


def løs_bræt(D):
    r2 = len(solution)
    for c2 in range(0, D): 
        gyldig = True 
        for idx, i in enumerate(solution): 
            r1 = idx ; c1 = i
            if not valid(r1, c1, r2, c2): 
                gyldig = False
                break
        if gyldig: 
            solution.append(c2)
            break

def solve(D, solution=[]):
    if len(solution) == D:
        return [solution]

    r2 = len(solution)
    out = []
    for c2 in range(0, D):
        gyldig = True
        for idx, i in enumerate(solution):
            r1 = idx; c1 = i
            if not valid(r1, c1, r2, c2):
                gyldig = False
                break
        if gyldig:
            out += solve(D, solution + [c2])
    return out


n = int(input("Indtast n for n-dronning-problemet: "))
løsninger = solve(n)
print(f"Antal løsninger for {n}×{n}: {len(løsninger)}")
print("Første løsning:", løsninger[0] if løsninger else "ingen")

if løsninger:
    solution = løsninger[0]
    tegn_bræt(n)