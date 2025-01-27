import numpy as np										# Vi starter med at importere
import matplotlib.pyplot as plt							
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
import os as os
 
  														
plt.rc("axes", labelsize=18, titlesize=22)   # skriftstørrelse af `xlabel`, `ylabel` og `title`
plt.rc("xtick", labelsize=16, top=True, direction="in")  # skriftstørrelse af ticks, vis også ticks øverst og vend ticks indad
plt.rc("ytick", labelsize=16, right=True, direction="in") # samme som ovenstående
plt.rc("legend", fontsize=16) # skriftstørrelse af figurers legends
plt.rc("axes", grid='on')

#%%
#Kalibrering 
														# Her er værdierne for vores kalibrering
t_list = np.array([90,70,50,30,10,0,-10,-30,-50,-70,-90])
v_list = np.array([2.410, 2.242, 1.904, 1.398, 0.616, 0.073, -0.583, -2.502, -4.334, -5.810, -7.007])

v_a = np.linspace(-8, 3, 1000)
t_a = np.linspace(-90,90, 1000)

def θ(V, a,b,c,d): 										# Her definere vi funktion for vinkel 
    return -1/c*np.log(1/b*(a/(V+d)-1))					# som funktion af spændingsfald. 
    
def V(t, a,b,c,d):										# Her definere vi spændingsfald som funktion
    return a/(1+b*np.exp(-c*t))-d						# af vinkel 

gæt = [2,1,1,1]

θ_params, pcov = curve_fit(V, t_list, v_list, p0=gæt)	# Vi bruger curve_fit
a,b,c,d = θ_params
print(f"a = {a:.3f}, b = {b:.3f}, c = {c:.3f}, d = {d:.3f}")
 
fig, [ax1, ax2] = plt.subplots(1,2, figsize=(8,4))		# Og plotter de to funktioner 

ax1.plot(t_list, v_list, label ="Data")
ax1.plot(t_a, V(t_a,*θ_params), label ="Fit")
ax1.plot(t_a, V(t_a, *gæt), label="Gæt")
ax1.set_title("Kalibrering")
ax1.set_xlabel("Vinkel (grader)")
ax1.set_ylabel("Spænding (V)")
ax1.legend()

ax2.plot(v_list, t_list, label ="Data")
ax2.plot(v_a, θ(v_a, *θ_params), label ="Fit")
ax2.set_title("Kalibrering")
ax2.set_ylabel("Vinkel (grader)")
ax2.set_xlabel("Spænding (V)")
ax2.legend()

plt.tight_layout()
plt.show()

#%%
#Fit Dataen
 
folder = "dag_2/tvungende_sving"						# Hvis directory er i ovelse_2, vælger vi mappen dag 2
max_d = []

for file in os.listdir(folder):							# Vi går igennem alle datafiler, og får dataen ud af dem
    file_path = folder + "/" + str(file)				# Derefter plotter vi dataen
    data = np.loadtxt(file_path, skiprows=3)
      
    data = data[data[:, 1] != 0]
    t,a,b = data.T
       
    fig, [ax1,ax3] = plt.subplots(2,1, figsize=(8,6), sharex=True)
    ax1.plot(t,a, color="tab:blue")
    ax1.set_xlim(-2.5, 2.5)
    ax1.set_ylim(-400, 400)
    #ax1.set_xlabel("Tid (s)")
    ax1.set_ylabel("Pendul (mV)")
     
    ax2 = ax1.twinx()
     
    ax2.plot(t,b, color="tab:orange")
    ax2.set_ylim(-2,2)
    ax2.set_ylabel("Funktionsgenerator (V)")
    ax2.spines['right'].set_color('tab:orange')
     
    
    a = a/1000 # Til volt
                        								# Her sætter vi dataen ind i vinkel som funktion
    ax3.plot(t,θ(a, *θ_params))							# af spændingsfald, og plotter vinkel som funktion
    ax3.set_xlabel("Tid (s)")							# af tiden 
    ax3.set_ylabel("Vinkel")
    ax3.set_ylim(-5,3)
    plt.tight_layout() 
														# Vi finder amplituden af θ(t)
    max_d.append((max(θ(a, *θ_params))-min(θ(a, *θ_params)))/2)
    #max_d.append((np.average()))
    peaki = find_peaks(θ(a, *θ_params), -0.5, 0, 2000)[0]
    lowi = find_peaks(-θ(a, *θ_params), 1.7, 0, 2000)[0]
    θmax = np.average(θ(a[peaki], *θ_params))
    ax3.scatter(t[peaki], θ(a[peaki], *θ_params), color="tab:green")
    ax3.scatter(t[lowi], θ(a[lowi], *θ_params), color="tab:red")
    
#%%
# max grader som funktion af frekvens
 
fig, [ax4, ax5] = plt.subplots(1,2, sharey=True)

frekvens = np.linspace(0.5,1.2,13)   					# Frekvensen vi har målt med på dag 2
ax4.scatter(frekvens,max_d, color="tab:blue", )
ax4.set_xlim(0.4, 1.3)
ax4.set_ylim(0, 5)
ax4.set_xlabel("                               Frekvens (Hz)")
ax4.set_ylabel("$θ_{max}$")


folder = "dag_3/tvungende_sving_mikro"					# Hvis directory er i ovelse_2, vælger vi mappen dag 2
max_d2 = []

for file in os.listdir(folder):							
    file_path = folder + "/" + str(file)				
    data = np.loadtxt(file_path, skiprows=3)
      
    data = data[data[:, 1] != 0]
    t,a,b = data.T

    a = a/1000 # Til volt
                        																								
    max_d2.append((max(θ(a, *θ_params))-min(θ(a, *θ_params)))/2)
    
                                                        # Frekvensen vi har målt med på dag 3
frekvens = [0.803, 0.816, 0.829, 0.842, 0.855, 0.868, 0.881, 0.895, 0.909, 0.923, 0.937, 0.951, 0.874, 0.879, 0.888]
ax5.scatter(frekvens,max_d2, color="tab:orange")

ax5.set_xlim(0.8, 1)
ax5.set_ylim(0, 5)

print(f"Resonans frekvens: {frekvens[max_d2.index(max(max_d2))]}, θ_max: {max(max_d2)}")
plt.show()