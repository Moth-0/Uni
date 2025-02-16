from itertools import permutations

n = int(input("n: "))

outstring = ''.join([str(i) for i in range(1, n + 1)])


def perm_list(n):
    num_string = ''.join(map(str, range(1, n + 1)))
    all_permutations = [''.join(p) for p in permutations(num_string)]
    return all_permutations


for p in perm_list(n):
    if p not in outstring: 
        #check the shortes way to get p in 
        l = 1
        while l < n:
            if p[:-l] not in outstring:
                l += 1
            

print(f"n={n}, lenght={len(outstring)}, {outstring}")