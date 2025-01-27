# Import
import numpy as np
import matplotlib.pyplot as plt
  
  
# Plot settings
plt.rc("axes", labelsize=18, titlesize=22)   # skriftstørrelse af `xlabel`, `ylabel` og `title`
plt.rc("xtick", labelsize=16, top=True, direction="in")  # skriftstørrelse af ticks, vis også ticks øverst og vend ticks indad
plt.rc("ytick", labelsize=16, right=True, direction="in") # samme som ovenstående
plt.rc("legend", fontsize=16) # skriftstørrelse af figurers legends
#%%
  
diameter = [0.02984, 0.02984, 0.02985, 0.02974, 0.02984, 0.02964, 0.02964]
tykkelse = [0.00381, 0.005, 0.00679, 0.00851, 0.01, 0.01199, 0.01482]
θ = 16.7 * np.pi / 180
  
for j in [1,3,5,7]:
    print("Legeme: " + str(j))
    for i in range(1,4):
          
        # File import
        filename = "ovelse_1/dag_1/legeme_" + str(j) + "/rul_" + str(i) + ".txt"
          
        data = np.loadtxt(filename, skiprows=3, max_rows=850)
        #data = data[~np.all(data == 0.0000000000, axis=1)]# fjerner alle rækker med et 0 i anden kolonne
        data = data[data[:, 1] != 0]
        a,b = data.T
        t = np.array(a/1000)
        u = np.array(b)
        
          
        # Fit
        A,B,C = np.polyfit(t, u, 2)
          
          
        # Første plot
        fig, axes = plt.subplots(1,2, figsize=[8,4])
        ax1, ax2 = axes
        plt.sca(ax1)
        plt.plot(t,u, label="Data")
        plt.xlabel("Tid (s)")
        plt.ylabel("Spændingsforskel (V)")
        plt.title("Legeme: " + str(j) + ", rul: " + str(i))
        plt.plot(t, A*t**2+B*t+C, label="Fit")
        plt.legend(loc='lower left')
          
          
        #Andet plot
        plt.sca(ax2)
        plt.plot(t, (-0.3723)*(A*t**2+B*t+C) + 0.6413, color="tab:orange", label="Data")
        plt.xlabel("Tid (s)")
        plt.ylabel("Position (m)")
        plt.title("Position som funktion af tid")
        plt.legend(loc='upper left')
          
          
        # Udskriver koefficienterne
        print("rul: " + str(i))
        print("A =", (-0.3723)*A)
        print("B =", (-0.3723)*B)
        print("C =", (-0.3723)*C + 0.6413)
        print(" ")
  
          
        plt.tight_layout()
  
#%%
 
fig1, axes1 = plt.subplots(2,1, figsize=[8,8], sharex=True,
                           gridspec_kw={'height_ratios': [2, 1], "hspace": 0.05}) #Gør så vi ikke bygger videre på plottet over
ax1_1, ax1_2 = axes1
 
a_t =[]
a_d =[]
sd_a =[]
R_x =[]
  
for j in [1,3,5,7]:
     
    a_r =[]
    for i in range(1, 4):
          
        # File import
        filename = "ovelse_1/dag_1/legeme_" + str(j) + "/rul_" + str(i) + ".txt"
          
        data = np.loadtxt(filename, skiprows=3, max_rows=850)
        #data = data[~np.all(data == 0.0000000000, axis=1)]# fjerner alle rækker med et 0 i anden kolonne
        data = data[data[:, 1] != 0]
        a,b = data.T
        t = np.array(a/1000)
        u = np.array(b)
         
          
        # Fit
        A, B, C = np.polyfit(t, u, 2)
          
        # Bedømmelse
      
        R2 = diameter[(j - 1)]/2
        R1 = R2 - tykkelse[(j - 1)]
         
        a_r = np.append(a_r,(-0.3723)*A*2)
          
    
    a_t = np.append(a_t, 2*9.82*R2**2*np.sin(θ)/(R1**2 + 3*R2**2)) #teoretisk acceleration for hver legeme
     
    a_d = np.append(a_d, np.mean(a_r)) #middelværdi for målt acceleration pr legeme
     
    sd_a = np.append(sd_a, np.std(a_r, ddof=1)) #standard afvigelsen for målt acceleration pr legeme
     
    R_x = np.append(R_x, R1) #indre radius pr legeme
     
     
#R_x, a_t, sd_a, a_d = R_x.T, a_t.T, sd_a.T, a_d.T
 
 
plt.sca(ax1_1)
plt.plot(R_x, a_t, "bo", label="Teori")
plt.plot(R_x, a_d, "ro", label="Data")
plt.errorbar(R_x, a_d, sd_a, fmt="ro", ms=8, capsize=4)
plt.ylim(0, 2) # definere y-aksen
plt.ylabel("Acceleration $(m/s^2)$")
plt.title('Acceleration som funtion af indre radius')
   
     
plt.sca(ax1_2)
plt.plot(R_x, a_t, "bo", label="Teori", )
plt.plot(R_x, a_d, "ro", label="Data")
plt.errorbar(R_x, a_d, sd_a, fmt="ro", ms=8, capsize=4)
plt.xlabel("Indre radius (m)")
plt.ylabel("Acceleration $(m/s^2)$")
 
 
plt.sca(ax1_1)
plt.legend(loc='lower left')
plt.show()

#%%
# Histogram
