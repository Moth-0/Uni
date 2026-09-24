'''
    PROGRESSION

    Your task is to create a function progession(L), that takes a list L of one
    of the following three formats:

        [first, ..., end]
        [first, second, ..., end]
        [first, second, third, ..., end] 

    where first, second, and third are integers, and ... is the Ellipsis object.
    
    The function progression should return a list of integers, such that in the 
    first case it just returns all integers from first to end in increasing 
    order, including end (it is guaranteed that first < end). E.g., 
    
        progression([5, ..., 15]) = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    In the second case, an increasing sequence of integers should be returned, 
    with a step size between the integers of step = second - first. 
    The sequence should start with first and second, and the last integer the 
    largest in the sequence <= end (it is guaranteed first < second < end). E.g.,

        progression([4, 7, ..., 31]) = [4, 7, 10, 13, 16, 19, 22, 25, 28, 31]

    Finally, in the third case an increasing sequence of integers should be 
    returned where the gap between consecutive integers might increase. In
    particular if step_1 = second - first and step_2 = third - second, then
    we let delta = step_2 - step_1, and require that the gap between the i'th
    and (i+1)'st returned integer is step_1 + delta * (i - 1). The sequence 
    should start with first, second, and third integer, and the last integer
    should be the largest in the sequence <= end (it is guaranteed that 
    first < second < third < end and step_2 >= step_1). E.g., 

        progression([1, 3, 6, ..., 50]) = [1, 3, 6, 10, 15, 21, 28, 36, 45]

    where step_1 = 2, step_2 = 3, and delta = 1.
        
    Input:  A single Python list L in one of the three formats above, i.e., 
            a list with 3, 4, or 5 elements, where all elements are integers
            except the second last element which is the Ellipsis object.
            In all cases it is guaranteed that 0 <= start <= end <= 1000.

    Output: The result of calling progression(L).

    Example:

       Input:  [1, 3, 6, ..., 100]
       
       Output: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91]

    Note: The below code already reads the input and prints the result of
          calling the function progression.
'''


def progression(L):
    # insert code
    n = len(L)
    # First Case
    if n == 3: 
        return [i for i in range(L[0], L[-1]+1)]
    
    # Second Case
    if n == 4: 
        jump = L[1] - L[0]
        return [i for i in range(L[0], L[-1]+1, jump)]
    
    # Third Case
    if n == 5: 
        delta = L[0]+L[2]-2*L[1] # (L[2]-L[1]) - (L[1]-L[0])
        step = L[1]-L[0]
        i = L[0]
        out = []
        while i <= L[-1]: 
            out.append(i)
            i += step
            step += delta
        return out


print(progression(eval(input())))
