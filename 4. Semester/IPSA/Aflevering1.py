"""
HANDIN 1 (down payment)

This handin is done by: 
    202307989 Mikkel Moth Billing 

Reflection upon solution: 
    I used int for the payment, so you cant pay with decimal increments. 
    Off course you have to overshoot the loan payment, and therefore get an interger number of months,
    i guess you could make it to calculate the last payment so you hit 0.0. 
"""

loan = float(input("Size of initial loan: "))
rate = float(input("Monthly intrest rate: "))
pay = int(input("Monthly payment: "))

months = 0 

while loan > 0: 
    months += 1
    intrest = loan * rate
    loan = loan + intrest - pay

print(f"Months to pay off loan: {str(months)}")