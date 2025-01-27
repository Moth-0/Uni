# Import
import numpy as np
import matplotlib.pyplot as plt
import os as os
    
    
# Plot settings
plt.rc("axes", labelsize=18, titlesize=22)   # skriftstørrelse af `xlabel`, `ylabel` og `title`
plt.rc("xtick", labelsize=16, top=True, direction="in")  # skriftstørrelse af ticks, vis også ticks øverst og vend ticks indad
plt.rc("ytick", labelsize=16, right=True, direction="in") # samme som ovenstående
plt.rc("legend", fontsize=16) # skriftstørrelse af figurers legends
 
#%% Plot alle filerne og deres fit:
    
diameter = [0.03, 0.03, 0.03, 0.03, 0.03]
tykkelse = [0.003, 0.007, 0.009, 0.011, 0.015]
θ = 16.8 * np.pi / 180
  
  
l_folders = sorted(os.listdir("dag_2/rullende"))
  
j = 0
for l_folder in l_folders:
    j = j + 1
    i = 0
    r_folders = sorted(os.listdir("dag_2/rullende/" + str(l_folder)))
    print("Legeme: " + str(j))
      
    for r_folder in r_folders:
        files = os.listdir("dag_2/rullende/" + str(l_folder) + "/" + str(r_folder))
              
        for file in files:
            i = i + 1
             
            file_path = "dag_2/rullende/" + str(l_folder) + "/" + str(r_folder) + "/" + str(file)
            # Print navn
            #print(str(i) + str(file_name))
            
            data = np.loadtxt(file_path, skiprows=3, max_rows=850)
             
            data = data[data[:, 1] != 0]
            a,b = data.T
            t = np.array(a/1000)
            u = np.array(b)
              
                
            # Fit
            A,B,C = np.polyfit(t, u, 2)
              
            a = -0.38478
            b =  0.64889
              
              
            # Første plot
            fig, axes = plt.subplots(1,2, figsize=[8,4])
            ax1, ax2 = axes
            plt.sca(ax1)
            plt.plot(t,u, label="Data")
            plt.xlabel("Tid (s)")
            plt.ylabel("Spændingsforskel (V)")
            plt.title("Legeme: " + str(j) + ", rul: " + str(i))
            plt.plot(t, A*t**2+B*t+C, label="Fit")
            plt.ylim(0,1.6)
            plt.legend(loc='lower left')
                
            #Andet plot
            plt.sca(ax2)
            plt.plot(t, a*(A*t**2+B*t+C) + b, color="tab:orange", label="Data")
            plt.xlabel("Tid (s)")
            plt.ylabel("Position (m)")
            plt.title("Position som funktion af tid")
            plt.legend(loc='upper left')
              
              
            # Udskriver koefficienterne
            print("rul: " + str(i))
            print("A =", a*A)
            print("B =", a*B)
            print("C =", a*C + b)
            print(" ")
              
            plt.tight_layout()
              
#%% Plot acceleration som funktion af indre radius:
    
diameter = [0.03, 0.03, 0.03, 0.03, 0.03]
tykkelse = [0.003, 0.007, 0.009, 0.011, 0.015]
θ = 16.8 * np.pi / 180
  
a_t =[]
a_d =[]
sd_a =[]
R_x =[]
  
l_folders = sorted(os.listdir("dag_2/rullende"))
  
j = 0
for l_folder in l_folders:
    j = j + 1
    i = 0
    r_folders = sorted(os.listdir("dag_2/rullende/" + str(l_folder)))
    print("Legeme: " + str(j))
    a_r = []
      
    for r_folder in r_folders:
        files = os.listdir("dag_2/rullende/" + str(l_folder) + "/" + str(r_folder))
              
        for file in files:
            i = i + 1
            # Get the file name without the extension
            file_path = "dag_2/rullende/" + str(l_folder) + "/" + str(r_folder) + "/" + str(file)
            # Print the file name
            #print(str(i) + str(file_name))
            
            data = np.loadtxt(file_path, skiprows=3, max_rows=850)
             
            data = data[data[:, 1] != 0]
            a,b = data.T
            t = np.array(a/1000)
            u = np.array(b)
              
                
            # Fit
            A,B,C = np.polyfit(t, u, 2)
              
            a = -0.38478
            b =  0.64889
              
            # Bedømmelse
            
            R2 = diameter[(j - 1)]/2
            R1 = R2 - tykkelse[(j - 1)]
               
            a_r = np.append(a_r,a*A*2)
                
          
    a_t = np.append(a_t, 2*9.82*R2**2*np.sin(θ)/(R1**2 + 3*R2**2)) #teoretisk acceleration for hver legeme
       
    a_d = np.append(a_d, np.mean(a_r)) #middelværdi for målt acceleration pr legeme
       
    sd_a = np.append(sd_a, np.std(a_r, ddof=1)) #standard afvigelsen for målt acceleration pr legeme
       
    R_x = np.append(R_x, R1) #indre radius pr legeme
  
# Plot 3
fig, ax = plt.subplots() 

        
R_t = np.linspace(0, 0.012, 1000)
a_t = lambda R1: 2*9.82*R2**2*np.sin(θ)/(R1**2 + 3*R2**2)
ax.set_title('Acceleration som funtion af indre radius')    
ax.plot(R_t, a_t(R_t), "b", label="Teori", )
ax.plot(R_x, a_d, "ro", label="Data")
ax.errorbar(R_x, a_d, np.mean(sd_a), fmt="ro", ms=8, capsize=4)
ax.set_xlabel("Indre radius (m)")
ax.set_ylabel("Acceleration $(m/s^2)$")
   
ax.legend(loc='lower left')
                
#%%
# Glidende
  
l_folders = os.listdir("dag_2/glidende")
θ = 16.8 * np.pi / 180
 
μ_t = [0.25, 0.19]
i = -1
 
a_t =[]
a_d =[]
sd_a =[]
R_x =[]
 
for folder in l_folders:
    print(folder)
    files = os.listdir("dag_2/glidende/" + str(folder) + "/")
    a_r = []
    μ_r = []
    i = i + 1
      
    for file in files:
        file_path = "dag_2/glidende/" + str(folder) + "/" + str(file)
        data = np.loadtxt(file_path, skiprows=3)
          
        data = data[data[:, 1] != 0]
        a,b = data.T
        t = np.array(a)
        u = np.array(b)
          
        # Fit
        A,B,C = np.polyfit(t, u, 2)
          
        a = -0.38478
        b =  0.64889
          
        # Bedømmelse
           
        a_r = np.append(a_r,a*A*2)
         
        μ_r = np.append(μ_r, (np.sin(θ)-a_r/9.82)/(np.cos(θ)))
         
         
    a_t = 9.82*(np.sin(θ)-μ_t[i]*np.cos(θ)) #teoretisk acceleration for hver legeme
       
    a_d = np.mean(a_r) #middelværdi for målt acceleration pr legeme
        
    sd_a = np.std(a_r, ddof=1) #standard afvigelsen for målt acceleration pr legeme
     
    μ_d = np.mean(μ_r)
     
    sd_μ = np.std(μ_r, ddof=1)
            
    print(f"Data: accelaration: {a_d :.2f}, Gnidning: {μ_d :.2f}")
    print(f"Teori: accelaration: {a_t :.2f}, Gnidning: {μ_t[i] :.2f}")
     
    plt.errorbar(i, μ_d, np.mean(sd_μ), fmt="ro", ms=8, capsize=4, label="Data")
    plt.plot(i, μ_t[i], "bo", label="Teori")
     
    plt.xlabel("Hul stål                    Massiv messing")
    plt.ylabel("μ")
    #plt.legend()