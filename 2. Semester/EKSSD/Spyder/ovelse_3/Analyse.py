# Imports 
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import scipy.integrate as si
import pandas as pd
import os as os


plt.rc("axes", labelsize=16)   
plt.rc("xtick", labelsize=16, top=True, direction="in")  
plt.rc("ytick", labelsize=16, right=True, direction="in")
plt.rc("axes", titlesize=18)
plt.rc("axes", grid=True)

def cross_2d(A, B):
    cross_products = A[0,:] * B[1,:] - A[1,:] * B[0,:]
    return cross_products

def længde(A):
    return np.linalg.norm(A, axis=0)

def Hfind_F(A,B,c):
    if længde(A) > radius1+radius2: 
        F = np.zeros_like(A)
    else: 
        F = c*B/længde(A)
    return F

def find_F(A,B,c):
    if længde(A) == længde(r21).min():
        F = c*B/længde(A)
    else:
        F = np.zeros_like(A)
    return F

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

# Funktion til at beregne hastighed ved finitte differenser
def Hdiff_funk(x, t):
    # Beregn tidsintervaller
    dt = np.diff(t)
    # Beregn hastighed ved centrale finitte differenser
    central_diff = (x[2:] - x[:-2]) / (t[2:] - t[:-2])
    # Beregn hastighed ved fremad finitte differenser for det første punkt
    forward_diff = (x[1] - x[0]) / dt[0]
    # Beregn hastighed ved bagud finitte differenser for det sidste punkt
    backward_diff = (x[-1] - x[-2]) / dt[-1]
    
    # Kombiner alle hastigheder til en enkelt array
    velocities = np.concatenate(([forward_diff], central_diff, [backward_diff]))
    
    return velocities

def moving_average(data, window_size=3):
    # Glat data med en reflektion ved kanterne for at reducere kanthop
    ext_data = np.r_[data[window_size-1:0:-1], data, data[-1:-window_size:-1]]
    smooth_data = np.convolve(ext_data, np.ones(window_size)/window_size, mode='valid')
    return smooth_data[window_size//2:-window_size//2+1]

def diff_funk(positions, times):
    # Anvend glatning før differentiering
    smooth_positions = moving_average(positions, window_size=5)
    
    # Beregn hastigheder ved centrale finitte differenser
    dt = np.diff(times)
    velocities = np.empty_like(positions)
    
    # Brug centrale differenser, hvor det er muligt
    central_diff = np.diff(smooth_positions) / dt
    velocities[1:-1] = (central_diff[:-1] + central_diff[1:]) / 2

    # Brug fremad forskelle for det første punkt
    velocities[0] = (smooth_positions[1] - smooth_positions[0]) / dt[0]

    # Brug bagud forskelle for det sidste punkt
    velocities[-1] = (smooth_positions[-1] - smooth_positions[-2]) / dt[-1]

    return velocities

def poly_fit_and_diff(x, t, poly_order):
    # Fitte data til et polynomium
    coeffs = np.polyfit(t, x, poly_order)
    poly = np.poly1d(coeffs)
    
    # Differentier polynomiet for at finde omega
    d_poly = np.polyder(poly)
    
    # Beregn theta_fit og omega ved at evaluere det fittede polynomium og dets afledte
    theta_fit = poly(t)
    omega = d_poly(t)
    
    return theta_fit, omega

def r_og_R(x,y,radius):
    r = np.array([x,y])
    R = np.array([x+radius,np.zeros_like(x)])
    return r, R

#%%

m1 = 0.0277 #kg
m2 = 0.0205 #kg
R1 = 0.081/2
R2 = 0.074/2
I1 = 1/2*m1*R1**2
I2 = 1/2*m2*R2**2

folder = "dag_1/Data"

b_l = []
Kr_l = []
L_l = []

for file in os.listdir(folder):
    print(file)
    data = np.loadtxt(folder + "/" + str(file), skiprows=3, usecols=range(9))
    t,xA,yA,xB,yB,xC,yC,xD,yD = data.T
    col = np.genfromtxt(folder + "/" + str(file), skip_header=3, usecols=(9,10), delimiter='	', filling_values=0)
    t_c,b = abs(col[col != 0])
    
    
    print(t_c,b)
    
    θ1 = np.arctan2((yB-yA),(xB-xA))
    θ2 = np.arctan2((yD-yC),(xD-xC))
    
    dθ1 = fixθ(θ1)-θ1[0]
    dθ2 = fixθ(θ2)-θ2[0]

    
    # Beregn hastighedskomponenterne for begge pucke
    x1, vx1 = poly_fit_and_diff(xA, t, 4)
    y1, vy1 = poly_fit_and_diff(yA, t, 4)
    v1 = np.sqrt(vx1**2 + vy1**2)
    x2, vx2 = poly_fit_and_diff(xC, t, 4)
    y2, vy2 = poly_fit_and_diff(yC, t, 4)
    v2 = np.sqrt(vx2**2 + vy2**2)
    
    ax1 = diff_funk(vx1, t)
    ay1 = diff_funk(vy1, t)
    ax2 = diff_funk(vx2, t)
    ay2 = diff_funk(vy2, t)
    
    ω1 = diff_funk(dθ1, t)
    ω2 = diff_funk(dθ2, t)
    
    α1 = diff_funk(ω1, t)
    α2 = diff_funk(ω2, t)
    
    ft1, fω1 = poly_fit_and_diff(dθ1,t,5)
    ft2, fω2 = poly_fit_and_diff(dθ2,t,5)
    
    Fx1 = ax1*m1
    Fy1 = ay1*m1
    #F1 = np.sqrt(Fx1**2+Fy1**2)
    F1 = np.array([Fx1,Fy1])
    
    Fx2 = ax2*m2
    Fy2 = ay2*m2
    #F2 = np.sqrt(Fx2**2+Fy2**2)
    F2 = np.array([Fx2,Fy2])
    
    Kt1 = 1/2*m1*v1**2
    Kr1 = 1/2*I1*fω1**2
    K1 = Kt1 + Kr1
    Kt2 = 1/2*m2*v2**2
    Kr2 = 1/2*I2*fω2**2
    K2 = Kt2 + Kr2
    
    dL1dt = I1*α1
    dL2dt = I2*α2
    L1 = I1*fω1
    L2 = I2*fω2
    
    b_l.append(b)
    Kr_l.append([Kr1[-1]-Kr1[0],Kr2[-1]-Kr2[0]])
    L_l.append([L1[-1]-L1[0],L2[-1]-L2[0]])
    
    fig, ax = plt.subplots(1,1, sharex=True)
    ax.plot(t,ω1)
    ax.plot(t,fω1)
    """
    ax[0].set_title(str(file))
    ax[0].plot(t, fω1, label="$ω_1$")
    ax[0].plot(t, fω2, label="$ω_2$")
    ax[1].plot(t, Kr1, label="$Kr_1$")
    ax[1].plot(t, Kr2, label="$Kr_2$")
    ax[2].plot(t, L1, label="$L_1$")
    ax[2].plot(t, L2, label="$L_2$")
    ax[0].set_ylabel("V. Hastighed")
    ax[1].set_ylabel("Kinetisk")
    ax[2].set_ylabel("Impuls")
    ax[2].set_xlabel("Tid")
    ax[0].legend()
    ax[1].legend()
    ax[2].legend()
    
    """
    """
    #Test
    fig, ax = plt.subplots(2,1, sharex=True)
    ax[0].set_title(str(file))
    
    
    
    ax[0].plot(t, xA)
    ax[0].plot(t, xC)
    #ax[0].plot(t, x1)
    #ax[0].plot(t, x2)
    
    
    ax[1].plot(t, vx1)
    ax[1].plot(t, vx2)
    
    
    
fig,ax = plt.subplots(2,1,sharex=True)

ax[0].plot(np.array(b_l),np.array(Kr_l)[:,0],"o")
ax[0].plot(np.array(b_l),np.array(Kr_l)[:,1],"o")

ax[1].plot(np.array(b_l),np.array(L_l)[:,0],"o")
ax[1].plot(np.array(b_l),np.array(L_l)[:,1],"o")
"""

#%%
folder = "dag_1/data"
file = "data7.txt"

data = np.loadtxt(folder + "/" + str(file), skiprows=3, usecols=range(9))
t,xA,yA,xB,yB,xC,yC,xD,yD = data.T
b = np.genfromtxt(folder + "/" + str(file), skip_header=3, usecols=10, delimiter='	', filling_values=0)
b = abs(b[b != 0])

θ1 = np.arctan2((yB-yA),(xB-xA))
θ2 = np.arctan2((yD-yC),(xD-xC))

m1 = 0.0277 #kg
m2 = 0.0205 #kg
radius1 = 0.081/2
radius2 = 0.074/2
I1 = 1/2*m1*R1**2
I2 = 1/2*m2*R2**2

dθ1 = fixθ(θ1)-θ1[0]
dθ2 = fixθ(θ2)-θ2[0]


# Beregn hastighedskomponenterne for begge pucke
vx1 = diff_funk(xA, t)
vy1 = diff_funk(yA, t)
v1 = np.sqrt(vx1**2 + vy1**2)
vx2 = diff_funk(xC, t)
vy2 = diff_funk(yC, t)
v2 = np.sqrt(vx2**2 + vy2**2)

ax1 = diff_funk(vx1, t)
ay1 = diff_funk(vy1, t)
ax2 = diff_funk(vx2, t)
ay2 = diff_funk(vy2, t)

ω1 = diff_funk(dθ1, t)
ω2 = diff_funk(dθ2, t)


# Begyndelsesbetingelser
y0 = [xA[0], yA[0], vx1[0], vy1[0], dθ1[0], ω1[0], 
      xC[0], yC[0], vx2[0], vy2[0], dθ2[0], ω2[0]]

# Integrationstid
Tstart, Tstop = t[0], t[-1]

#Function
def system_dynamics(t, y):
    # Unpack dine variabler fra y-vektoren
    x1, y1, vx1, vy1, dθ1, ω1, x2, y2, vx2, vy2, dθ2, ω2 = y
    
    dx1dt = vx1
    dx2dt = vx2
    
    dy1dt = vy1
    dy2dt = vy2
    
    dθ1dt = ω1
    dθ2dt = ω2
    
    
    
    

#%%

folder = "dag_1/data"
file = "data7.txt"

data = np.loadtxt(folder + "/" + str(file), skiprows=3, usecols=range(9))
t,xA,yA,xB,yB,xC,yC,xD,yD = data.T
b = np.genfromtxt(folder + "/" + str(file), skip_header=3, usecols=10, delimiter='	', filling_values=0)
b = abs(b[b != 0])

θ1 = np.arctan2((yB-yA),(xB-xA))
θ2 = np.arctan2((yD-yC),(xD-xC))

m1 = 0.0277 #kg
m2 = 0.0205 #kg
radius1 = 0.081/2
radius2 = 0.074/2

dθ1 = fixθ(θ1)-θ1[0]
dθ2 = fixθ(θ2)-θ2[0]


# Beregn hastighedskomponenterne for begge pucke
vx1 = diff_funk(xA, t)
vy1 = diff_funk(yA, t)
vx2 = diff_funk(xC, t)
vy2 = diff_funk(yC, t)

ω1 = diff_funk(dθ1, t)
ω2 = diff_funk(dθ2, t)


# Begyndelsesbetingelser
y0 = [xA[0], yA[0], vx1[0], vy1[0], dθ1[0], ω1[0], 
      xC[0], yC[0], vx2[0], vy2[0], dθ2[0], ω2[0]]


# Integrationstid
Tstart, Tstop = t[0], t[-1]
c1 = 100.0
c2 = 50

r1, R1 = r_og_R(xA,yA,radius1)
r2, R2 = r_og_R(xC,yC,radius2)
r21 = r2-r1
n21 = np.array([-r21[1], r21[0]])


I1 = 1/2*m1*længde(R1)**2
I2 = 1/2*m2*længde(R2)**2
v1 = np.array([vx1,vy1])
v2 = np.array([vx2,vy2])
# Definer ændringer / afledede her. Dette eksempel antager nogle simple dynamikker
# og skal tilpasses for at matche den specifikke model og kræfter der arbejdes med


# Vekselvirkning
Fp1 = []
Fv1 = []
for i,j in zip(r21.T,n21.T):
    Fp1.append(find_F(i,i,c1))
    Fv1.append(find_F(i,j,c2))

Fp1 = np.array(Fp1).T
Fv1 = np.array(Fv1).T


F21 = Fp1 + Fv1
F12 = -F21


#Function
def system_dynamics(t, y):
    # Unpack dine variabler fra y-vektoren
    x1, y1, vx1, vy1, dθ1, ω1, x2, y2, vx2, vy2, dθ2, ω2 = y

    # Definer ændringer / afledede her. Dette eksempel antager nogle simple dynamikker
    # og skal tilpasses for at matche den specifikke model og kræfter der arbejdes med

    
    # Første puck
    dx1dt = vx1
    dy1dt = vy1
    dvx1dt = F21[0]/m1  # Eksempel på en simpel modellering af kraft
    dvy1dt = F21[1]/m1  # Ingen vertikal acceleration
    dθ1dt = ω1
    dω1dt = np.cross(R1,F21,axis=0)/I1 # Eksempel på en simpel modellering af momentpåvirkning
    
    # Gentag for den anden puck
    dx2dt = vx2
    dy2dt = vy2
    dvx2dt = F12[0]/m2
    dvy2dt = F12[1]/m2
    dθ2dt = ω2
    dω2dt = np.cross(R2,F12,axis=0)/I2
    
    
    return [dx1dt, dy1dt, dvx1dt, dvy1dt, dθ1dt, dω1dt, 
            dx2dt, dy2dt, dvx2dt, dvy2dt, dθ2dt, dω2dt]
   

# Løsning af ODE systemet
solution = si.solve_ivp(system_dynamics, [Tstart, Tstop], y0, t_eval=np.linspace(Tstart, Tstop, len(t)))

# solution.t er tidsvektoren, og solution.y er løsningerne (tilstande over tid)
# Tidsvektoren
ts = solution.t

# Udpak løsningerne
x1, y1, vx1, vy1, dθ1, ω1, x2, y2, vx2, vy2, dθ2, ω2 = solution.y

fig,ax = plt.subplots()
ax.plot(ts,vx1)

dE1dt = np.sum(F21*v1,axis=0)+længde(R1)*længde(Fp1)*ω1
dE2dt = np.sum(F12*v2,axis=0)+længde(R2)*længde(-Fp1)*ω2

dL1dt = np.cross(r1,Fp1, axis=0)+np.cross(r1+R1,Fv1,axis=0)
dL2dt = np.cross(r2,-Fp1, axis=0)+np.cross(r2+R2,-Fv1,axis=0)



