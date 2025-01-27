# Import
import numpy as np
import matplotlib.pyplot as plt
import random
    
    
# Plot settings
plt.rc("axes", labelsize=18, titlesize=22)   # skriftstørrelse af `xlabel`, `ylabel` og `title`
plt.rc("xtick", labelsize=16, top=True, direction="in")  
plt.rc("ytick", labelsize=16, right=True, direction="in") # samme som ovenstående
plt.rc("legend", fontsize=16) # skriftstørrelse af figurers legends


# Parametre 
h = 1 # Planks konstant 
ω = 1 # Omega
λ = 0 # Driving strenght
γ = 0.2 # Rate of interection
Δt = 0.01 # Timestep
time = 10 # Total tid
steps = 100 # Antal simuleringer

ψ1 = np.array([[1],[0]])
ψ2 = np.array([[0],[1]])

σp = np.array([[0,0],[1,0]])
σm = np.array([[0,1],[0,0]])


ρ_ensemble = np.zeros((2, 2, int(time/Δt)), dtype=complex)  # Til at opbevare densitetsmatricer

# Monte Carlo
for s in range(steps): 

    c1 = 0
    c2 = 1
    ψi = c1*ψ1 + c2*ψ2  # initial
    ψ = ψi              # initial copy
    
    
    Pi = []  
    ρ_list = []

    print(f"Nr:{s}")
    for t in range(int(time/Δt)):
        
        # Densitet
        ρ = np.dot(ψ,ψ.conj().T)
        ρt = ρ[0][0]*np.dot(ψ1,ψ1.conj().T)+ρ[1][1]*np.dot(ψ2,ψ2.conj().T)
        ρ_ensemble[:, :, t] += ρt  # Tilføj til ensemble 
        
        # Kvantetal
        n = np.real(ρ[0][0]*1+ρ[1][1]*2)
        
        # Hamiltonian 
        H_s = (h*ω*np.array([[1/2,0],[0,3/2]])                           # Harmonisk oscilator
                 + h*λ*(σp+σm)                                           # Driving field 
               )  

        H_eff = H_s - (1j*h*γ/2*((n+1)*np.dot(σp,σm) + n*np.dot(σm,σp))) # Lindblad
        
        # Operatorer
        L0 = γ*np.sqrt(n+1)*σm
        L1 = γ*np.sqrt(n)*σp
        
        p = random.random()         # Vælg p 
        
        # Δp
        L0L0 = np.dot(L0.T,L0)
        L1L1 = np.dot(L1.T,L1)
        ψL0L0ψ = np.real(np.vdot(ψ,np.dot(L0L0,ψ)))
        ψL1L1ψ = np.real(np.vdot(ψ,np.dot(L1L1,ψ)))
        Δp0 = Δt*ψL0L0ψ
        Δp1 = Δt*ψL1L1ψ
        Δp = Δp0+Δp1
        
    
        if Δp > p: 
            #print(f"p:{p:.2g}, Δp:{Δp:.2g}, Δp0:{Δp0:.2g}, Δp1:{Δp1:.2g}")
            
            if Δp0 > p:                         # Hop ned
                ψ = np.sqrt(Δt/Δp0)*np.dot(L0,ψ)   # (6.1)
                print("Down")
            
            elif Δp0+Δp1 > p:                   # Hop op
                ψ = np.sqrt(Δt/Δp1)*np.dot(L1,ψ)   # (6.2)
                print("Up")
            
            else:
                print("Something Wrong!")       # Debugging 
        
        else:                                   # No Jump
            ψ = np.dot((np.eye(2) + H_eff*Δt/(1j*h)) ,ψ)/np.sqrt(np.vdot(ψ,ψ)) # (4)
        #print(f"{np.real(np.vdot(ψ,ψ)):.4f}")
    
        Pi.append(np.abs(np.vdot(ψi, ψ)) ** 2)  # Sandsynlighed for ψi
        
# Gennemsnit af densitetsmatricer
ρ_ensemble /= steps

# Sandsynligheder        
P1 = [ρ_ensemble[0, 0, t].real for t in range(int(time/Δt))]
P2 = [ρ_ensemble[1, 1, t].real for t in range(int(time/Δt))]

# Plots
plt.plot(np.linspace(0, time, int(time/Δt)), P1, label='P(|ψ1⟩)')
plt.plot(np.linspace(0, time, int(time/Δt)), P2, label='P(|ψ2⟩)')

plt.xlabel('Tid (s)')
plt.ylabel('Sandsynlighed')
plt.title(f"Densitets udvikling, λ:{λ}, γ:{γ}")
plt.legend()
plt.show()
