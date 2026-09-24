'''
    DEVIATION

    Write a function deviation(x, y, z) that takes three floats x, y, and z as
    arguments and returns the absolut difference between the average of the 
    maximum and minimum (known as the mid-range) and the median of the three 
    values.

    If the the input values are 1.0, 6.0, and 10.0, then the minimum is 1.0, 
    the maximum is 10.0, the median is 6.0, and the mid-range is 
    (1.0 + 10.0) / 2 = 5.5. The output is abs(5.5 - 6.0) = 0.5.

    Input:  Three lines, each containing a single float x, y, and z, 
            respectively. 

    Output: The absolut difference between the average of the maximum and 
            minimum and the median of the three values, i.e., the result
            of calling deviation(x, y, z).

    Example:

      Input:  10.0
              1.0 
              6.0

      Output: 0.5

    Note: The below code already handles reading the input and printing the
          result of calling deviation(x, y, z).
'''


def deviation(x, y, z):
    # insert code
    l = sorted([x,y,z])
    return abs((l[2] + l[0])/2 - l[1])



x = float(input())
y = float(input())
z = float(input())
print(deviation(x, y, z))
