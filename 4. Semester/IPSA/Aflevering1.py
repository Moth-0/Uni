"""
HANDIN 1 (down payment)

This handin is done by: 
    202307989 Mikkel Moth Billing 

Reflection upon solution: 
    Fixed to solve the excersise, if the loan can not be payed off, 
    (because the interest is bigger then the pay)
    the while loop breaks. 
"""

loan = float(input("Size of initial loan: "))
rate = float(input("Monthly intrest rate: "))
pay = int(input("Monthly payment: "))

months = 0 

while loan > 0: 
    months += 1
    intrest = loan * rate
    if intrest >= pay: 
        print("Montly payment not enough to pay off loan!")
        break
    loan = loan + intrest - pay
    print(f"Month: {months}, Remaining loan: {loan:.2f}") # Now solves the excesice! 
