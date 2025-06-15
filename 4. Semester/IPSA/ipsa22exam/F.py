'''
    SELECT

    Write a function that reads a list of column names to extract from a table,
    and then reads a table, and extracts the required columns.

    Input:  Line 1: comma separated list of 1 or more columns to extract.
            Line 2: integer rows, the number of rows in the table.
            Line 3: comma separated list of column names in the table.
            Next rows lines: comma separated list of values for each table row.

            The table has between 1 and 10 columns, all columns have a
            unique column name, and there at most 100 rows in the table.
            At least one column should be extracted, and extracted columns
            are distinct.

    Output: For each row in the table, print a single line with the extracted
            column values in the requested order, separated by comma.

    Example:

      Input:  name,symbol
              5
              id,symbol,name,weight
              1,H,Hydrogen,1.008
              2,He,Helium,4.0026
              3,Li,Lithium,6.94
              4,Be,Beryllium,9.0122
              5,B,Boron,10.81

      Output: Hydrogen,H
              Helium,He
              Lithium,Li
              Beryllium,Be
              Boron,B
'''


# insert code
req = input().split(",")
rows = int(input())
keys = input().split(",")
items = [{k:v for (k,v) in zip(keys, input().split(","))} for _ in range(rows)]

for i in items: 
    print(",".join([i[r] for r in req]))