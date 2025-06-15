'''
    BUDGET

    Print a budget overview based on a list of transactions.
 
    Input:  A single line with a list of at most 100 transactions,
            each transaction a pair (value, text) where value is a
            number that is positive for an income and negative for
            an expense. The text is at most 35 characters long.
            Each value has absolute value <= 100_000.
            There is at least one income and one expense.

    Output: A print out of the budget as shown in the example below.
            Each line should be 50 characters long, except for
            the lines 'Income' and 'Expenses'. The budget should
            consist of three parts: Income, Expenses, and Total.
            Total is the sum of all values in the transactions.
            Income and expense tranactions should be ordered by
            decreasing absolute value, and alphabetically if
            several values are equal. 
            In lines with values, the text and value should be
            separated by a sequence of '.', with a SINGLE SPACE
            AT EACH END. Values should be printed with two decimals.

    Example:

      Input:  [(-500.00, 'Insurance'), (-2000.00, 'Food'), (-3500.00, 'Rent'),
               (-150.00, 'Hair cut'), (200.00, 'Loan'), (6000.00, 'Salary')]

      Output: ==================================================
              Income
              --------------------------------------------------
              Salary ................................... 6000.00
              Loan ...................................... 200.00
              ==================================================
              Expenses
              --------------------------------------------------
              Rent .................................... -3500.00
              Food .................................... -2000.00
              Insurance ................................ -500.00
              Hair cut ................................. -150.00
              ==================================================
              Total ...................................... 50.00
              ==================================================

    Note: The below code already handles reading the input.
'''


def budget(transactions):
    # insert code
    trans = sorted(transactions, key=lambda x: (-abs(x[0]), x[1]))
    income = [x for x in trans if x[0] > 0]
    expenses = [x for x in trans if x[0] < 0]
    total = f"{sum([x[0] for x in trans]):.2f}"

    print(50*"=" + "\nIncome\n" + 50*"-")
    for i in income: 
        num = f"{i[0]:.2f}"
        dots = 48-len(num)-len(i[1])
        print(f"{i[1]} " + dots*"." + f" {num}")

    print(50*"=" + "\nExpenses\n" + 50*"-")
    for e in expenses: 
        num = f"{e[0]:.2f}"
        dots = 48-len(num)-len(e[1])
        print(f"{e[1]} " + dots*"." + f" {num}")

    print(50*"="+ "\nTotal " + (48-5-len(total))*"." + f" {total}\n" + 50*"=")



budget(eval(input()))
