# Imports 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os as os 

plt.rc("axes", labelsize=16)   
plt.rc("xtick", labelsize=16, top=True, direction="in")  
plt.rc("ytick", labelsize=16, right=True, direction="in")
plt.rc("axes", titlesize=18)
plt.rc("axes", grid=True)

# funktion til at regne normen (1,N) af en (2,N) matrix
def længde(A):
    return np.linalg.norm(A, axis=0)

# For at fikse at der kommer et hop i vinklen, fordi at skiven roterer over x-aksen, 
# har vi lavet en funktion der checker om der er et hop mellem alle punkterne.  
# Hvis den springer så lægger vi 2π til resten af punkterne. 
def fixθ(v): 
    for i in range(len(v)-1): 
        if v[i + 1]-v[i] >= np.pi:
            v[i+1:] -= 2*np.pi
            continue
        elif v[i + 1]-v[i] <= -np.pi:
            v[i+1:] += 2*np.pi
            continue
    return v


# Her defineres 2 forskellige funktioner, dder bruges til at fitte dataen 
def lin_funk(x,a):
    return a*x

def lin_funk2(x, a, y0):
    b = y0 - x[0]*a
    return a*x+b

#%%

# Her defineres masser, radius og impulsmoment for de to pucke
m1 = 0.0205 #kg
m2 = 0.0277 #kg
R1 = 0.075/2 #m
R2 = 0.081/2 #m
I1 = 1/2*m1*R1**2
I2 = 1/2*m2*R2**2

folder = "dag_3/Data"

b_l = []
dK = []

# Alle datafilerne gennemgåes 
for file in os.listdir(folder):
    print(file)
    data = np.loadtxt(folder + "/" + str(file), skiprows=3, usecols=range(9))
    t,xA,yA,xB,yB,xC,yC,xD,yD = data.T
    
    # Her opstilles positions vektorer 
    r1 = np.array([xA,yA])
    r2 = np.array([xC,yC])
    r21 = r2-r1
    
    # Her findes indexet af for kollisions-tidspunktet, 
    # ved at finde der hvor afstanden mellem de to er mindst
    col_i = længde(r21).argmin()
    
    # Puckenes vinkel findes ud fra dataen 
    θ1 = np.arctan2((yB-yA),(xB-xA))
    θ2 = np.arctan2((yD-yC),(xD-xC))
    
    # Vi bruger den absolutte ændringen i vinkel 
    dθ1 = abs(fixθ(θ1)-θ1[0])
    dθ2 = abs(fixθ(θ2)-θ2[0])
    
    # Her laves curvefit, for at fitte ændringen af vinklen 
    popt1_A, pcov1_A = curve_fit(lin_funk, t[:col_i-1], dθ1[:col_i-1])
    
    popt1_B, pcov1_B = curve_fit(lambda x,a: lin_funk2(x,a,dθ1[col_i+1]), t[col_i+1:], dθ1[col_i+1:])
    
    popt2_A, pcov2_A = curve_fit(lin_funk, t[:col_i-1], dθ2[:col_i-1])
    
    popt2_B, pcov2_B = curve_fit(lambda x,a: lin_funk2(x,a,dθ2[col_i+1]), t[col_i+1:], dθ2[col_i+1:])
    
    tA_lin = np.linspace(0,t[col_i],100)
    tB_lin = np.linspace(t[col_i],t[-1],100)
    
    # Her plottes ændringen i vinkel, som funktion af tid, 
    # sammen med vores fit 
    fig, ax = plt.subplots(2,1,sharex=True)
    ax[0].plot(t,dθ1, label="data")
    ax[0].plot(tA_lin, lin_funk(tA_lin,*popt1_A), label="$θ_{fit,F}$")
    ax[0].plot(tB_lin, lin_funk2(tB_lin, *popt1_B, dθ1[col_i+1]), label="$θ_{fit,E}$")
    ax[0].set_ylabel("Δθ (rad)")
    ax[0].set_title(str(file))
    ax[0].legend()
    
    # Her regnes den rotationelle kinetiske energi, 
    # for begge pucke og sammenlagt 
    Kr1_A = 1/2*I1*popt1_A[0]**2
    Kr1_B = 1/2*I1*popt1_B[0]**2 
    
    Kr2_A = 1/2*I2*popt2_A[0]**2
    Kr2_B = 1/2*I2*popt2_B[0]**2
    
    Krt_A = Kr1_A+Kr2_A
    Krt_B = Kr1_B+Kr2_B
    
    
    ax[1].plot(tA_lin, np.ones_like(tA_lin)*Kr1_A, color="tab:blue", label=("$K_{rot,1}$"))
    ax[1].plot(tB_lin, np.ones_like(tB_lin)*Kr1_B, color="tab:blue")
    
    ax[1].plot(tA_lin, np.ones_like(tA_lin)*Kr2_A, color="tab:orange", label=("$K_{rot,2}$"))
    ax[1].plot(tB_lin, np.ones_like(tB_lin)*Kr2_B, color="tab:orange")
    
    ax[1].plot(tA_lin, np.ones_like(tA_lin)*Krt_A, color="tab:green", label=("$K_{rot,T}$"))
    ax[1].plot(tB_lin, np.ones_like(tB_lin)*Krt_B, color="tab:green")
    
    ax[1].set_ylabel("K (J)")
    ax[1].set_xlabel("Tid (s)")
    ax[1].legend()
    
    # impactparameteren vælges som afstanden til koordinatsystemets, 
    # x-akse ved indexet for kolissionen 
    b_l.append(abs(yA[col_i]))
    dK.append(Krt_B-Krt_A)
    
# Figeuren for ændring i rotationel kinetisk energi plottes, 
# som funktion af impactparameteren b    
fig, ax = plt.subplots()
ax.plot(b_l,dK,"o")
ax.set_ylabel("$ΔK_{rot}$ (J)")
ax.set_xlabel("impact parameter (m)")
ax.set_title("Ændring i Kinetisk rotations energi")
    