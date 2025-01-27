import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os as os
from scipy.optimize import minimize
from scipy.fft import fft, fftfreq
 
  
plt.rc("axes", labelsize=18, titlesize=22)   # skriftstørrelse af `xlabel`, `ylabel` og `title`
plt.rc("xtick", labelsize=16, top=True, direction="in")  # skriftstørrelse af ticks, vis også ticks øverst og vend ticks indad
plt.rc("ytick", labelsize=16, right=True, direction="in") # samme som ovenstående
plt.rc("legend", fontsize=16) # skriftstørrelse af figurers legends
 
#%%
#Fit Dataen
 
folder = "dag_2/tvungende_sving"
 
def funk(t, A, ω, y):
    return A*np.sin(ω*t)+y

def θ(V, a,b,c,d): 
    return -1/c*np.log(1/b*(a/(V+d)-1))

θ_params = [10.946, 0.291, 0.034, 8.447]
 
 
for file in os.listdir(folder):
    file_path = folder + "/" + str(file)
    data = np.loadtxt(file_path, skiprows=3)
      
    data = data[data[:, 1] != 0]
    t,a,b = data.T
       
    fig, [ax1,ax3] = plt.subplots(2,1, figsize=(8,6), sharex=True)
    ax1.plot(t,a, color="tab:blue")
    ax1.set_xlim(-2.5, 2.5)
    ax1.set_ylim(-500, 500)
    #ax1.set_xlabel("Tid (s)")
    ax1.set_ylabel("Pendul (mV)")
     
    ax2 = ax1.twinx()
     
    ax2.plot(t,b, color="tab:orange")
    ax2.set_ylim(-2,2)
    ax2.set_ylabel("Funktionsgenerator (V)")
    ax2.spines['right'].set_color('tab:orange')
     
    
    a = a/1000 # Til volt
    
    print(θ(a, *θ_params))
    ax3.plot(t,θ(a, *θ_params))
    ax3.set_xlabel("Tid (s)")
    ax3.set_ylabel("Vinkel")
    ax3.set_ylim(-4,4)
    plt.tight_layout() 
    

 
#%%
# max grader som funktion af frekvens
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    data = np.loadtxt(file_path, skiprows=3)
    
    data = data[data[:, 1] != 0]
    t, a, b = data.T
    # Anvend Fourier-transformation
    data_fft = fft(b)
    
    # Beregn frekvenserne
    n = len(b)
    timestep = t[1] - t[0]
    freq = fftfreq(n, d=timestep)
    
    # Plot frekvensspektret
    plt.plot(freq, np.abs(data_fft))
    plt.xlabel('Frekvens (Hz)')
    plt.ylabel('Amplitude')
    plt.xlim(0,2)
    plt.show()
    
    # Find den dominerende frekvens
    dominant_frequency = freq[np.argmax(np.abs(data_fft))]
    print(f"Dominerende frekvens: {dominant_frequency:.3f} Hz")
    
#%%
# max grader som funktion af frekvens
 
fig, ax4 = plt.subplots()
 
frz = []
max_d = []
 
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    data = np.loadtxt(file_path, skiprows=3)
    
    data = data[data[:, 1] != 0]
    t, a, b = data.T
    a = a/1000 # Til volt

     
    # Perform Fast Fourier Transform (FFT)
    fft_result = fft(b)
     
    # Calculate frequency spectrum
    n = len(b)
    frequencies = np.fft.fftfreq(n, d=t[1]-t[0])
     
     
    frequencies = frequencies[:n//2] 
     
    # Find dominant frequency
    dominant_frequency = frequencies[np.argmax(np.abs(fft_result[:n//2]))]
     
    frz.append(dominant_frequency)
    max_d.append((max(θ(a, *θ_params))-min(θ(a, *θ_params)))/2)
 
 
#print(max_d) 
ax4.plot(np.linspace(0.5,1.2,13),max_d,'.', color="tab:blue")
ax4.set_xlim(0.4, 1.3)
ax4.set_ylim(0, 4)
ax4.set_xlabel("Frekvens")
ax4.set_ylabel("$θ_{max}$")