import numpy as np

def SEMF(Z,A,a_v,a_s,a_c,a_a,a_p):
    def f_1(A): return A
    def f_2(A): return A**(2/3)
    def f_3(A,Z): return Z**2/(A**(1/3))
    def f_4(A,Z): return (A-2*Z)**2/A
    def f_5(A,Z):
        if A%2==0 and Z%2==0:
            return A**(-1/2)
        elif A%2==1 and Z%2==1:
            return -A**(-1/2)
        else:
            return 0
    return Z*(1.67e-27+9.11e-31)+(A-Z)*1.67e-27-a_v*f_1(A)-a_s*f_2(A)-a_c*f_3(A,Z)-a_a*f_4(A,Z)-a_p*f_5(A,Z)

print(SEMF(1,1,1,1,1,1,1))