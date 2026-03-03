#%%
#Exercise 6.3 - handin 3 (triplet distance - part I)
'''
HANDIN 3 (Triplet distance - part 1)

This handin is done by 
    202305360: Arunchand Suriyakumar

Reflection upon solution:
    In part A: The idea has been to generate the list with n string-elements using the chr-function. Notice that chr(65) generates the letter A. The
    list comprehension has been used for the list generation

    In part B: We generate a new list by randomly drawing an element from the original list. We make sure to remove the element from the original list
    to avoid picking the same, using "pop"

    In part C: Here we take an element from a list and compare with all the others, as strings of letters can be compared directly. Notice, that the code
    could be more efficient if it was sorted and then not checking element already checked previously. But as the list are quite short, this wasn't done

    In part D: Looking at the result, we saw that the first element of each tuple was the element in the first list and the second element was the elements
    in the pair-function used on list 2. 

    In part E: Similar to D, we noticed that this was the function made in part D used on list L, R and then in reverse (and then summed)
'''

from random import randint

#a
def generate_labels(n):
    list = [chr(65+x) for x in range(n)]
    return list


#b
def permute(L):
    permuted_list = [L.pop( randint(0, len(L)-1) ) for _ in range(len(L))]
    return permuted_list
    

#c
def pairs(L):
    pairs = [(x,y) for x in L for y in L if x<y]
    return pairs


#d
def canonical_triplets(L1, L2): 
    result = [(x, y) for x in L1 for y in pairs(L2)]
    return result

#e
def anchored_triplets(L, R): 
    result1 = canonical_triplets(L,R)
    result2 = canonical_triplets(R,L)
    result = result1 + result2
    return result

