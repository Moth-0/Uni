import numpy as np

def F_bar(y):
    n = len(y)
    # Create the Fourier matrix
    omega = np.exp(-2j*np.pi / n)  # ω = e^(-2πi/n)
    F = np.array([[omega**(i * j) for j in range(n)] for i in range(n)])
    # Compute the DFT
    #print(F)
    return F @ y

def F(y): 
    n = len(y)
    # Create the Fourier matrix
    omega = np.exp(2j * np.pi / n)  # ω = e^(2πi/n)
    F = np.array([[omega**(i * j) for j in range(n)] for i in range(n)])
    F = F/n
    # Compute the DFT
    #print(F)
    return F @ y

# Example for n = 6
y = np.array([0,1,2,3,4,5], dtype=complex)  # Replace y with your values
y_bar = F_bar(y)

print("F")


print("Discrete Fourier Transform:")
print(np.round(F_bar(y),3))

print("Inverse")
print(np.round(F(y_bar),3))