#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HANDIN 5 (Eight Queens Puzzle)

This handin is done by:
    202405797 Johannes Bøgh Fangel
    202407470 Valdemar Scheel

Reflection upon solution:
    Implementation: We started by creating a function called 'valid' that returns True
    if two queens can't capture each other. We implemented this with if-statements 
    of the situations where they would be able to capture each other - in same row, 
    column or diagonal.
    
    We then also created a functions that can print a solution, but this is rather 
    straight forward, so we won't comment on the implementation. Then to find the 
    solutions, we have a recusive function 'solve' that takes a partial solution and
    the size of the board and then tries to expand the solution. We have implemented
    it, so the recursion will break, when the number of queens (the length of tuple 
    given in the solution parameter) is the same as the board size, n. Otherwise it
    uses the 'valid' function to create a list of all the valid columns to place a queen
    and then creates a list of new partial solution, which for each of them are then
    given as input in the 'solve' function - the recursive part. It then appends all the
    solutions to an empty list, and then returns that list.
    
    At last we have a last function 'queen_problem_', that finds the total number of 
    solutions for a given n. This is done by appending the solutions for every start point
    to an empty list and finding the length of that list.
"""

def valid(r1, c1, r2, c2):
    if r1 == r2 or c1 == c2:    # Checks that queens are not on same row or column
        return False
    
    elif abs(r2-r1) == abs(c2-c1):
        return False
    
    else:
        return True

def print_solution(solution, n):
    
    for queen_index in solution:
        print(queen_index*'.' + 'Q' + (n-1-queen_index)*'.')
    
    if len(solution) < max(solution):
        for i in range(max(solution)-len(solution)+1):
            print('.....')


def solve(solution, n):
    
    if len(solution) == n:
        return [solution]
    
    else:
        valid_columns = []
        for i in range(n):
            if all([valid(len(solution), i, j, solution[j]) for j in range(len(solution))]):
                valid_columns.append(i)
        
        new_solutions = [(*solution, valid_column) for valid_column in valid_columns]
        
        sol = []
        for i in new_solutions:
            sol += solve(i, n)
        
        return sol
    
def queen_problem_solver(n):
    sol = []
    for i in range(n):
        sol += solve(tuple([i]), n)
    return len(sol)
            
         
n = 8
import time
start_time = time.time()
print(queen_problem_solver(n))
end_time = time.time()

time_to_find = end_time - start_time

print(f'Time to finding number of solution for {n} x {n} board: {time_to_find*1000:0.2f} ms')

