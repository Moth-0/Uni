import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit 
import scipy.stats as ss

plt.rc("axes", labelsize=16)   
plt.rc("xtick", labelsize=16, top=True, direction="in")  
plt.rc("ytick", labelsize=16, right=True, direction="in")
plt.rc("axes", titlesize=18)
plt.rc("axes", grid=True)

def dSHB(t, A, bm, w, φ, x0):
    return A*np.exp(-bm*t)*np.cos(w*t+φ)+x0

filA = "Data4A.txt"
filB = "Data4B.txt"


m = 0.015 # kg, masse lille kugle (Spec)
rm = 0.0075 #m, radius lille kugle (Spec)
M = 1.500 # kg, masse stor kugle  (Spec)
d = 0.05 # m, afstand fra kugle til rotationsakse (Kan måles)
r = 0.0465 # m, afstand fra stor til lille kugle (Spec)
dotr = 0.05/2 # m, radius af lysprik (måles)

I = 2*m*(d**2 + 2/5*rm**2) # Inertimoment 


# Afstand fra spejl til væg
y = 5.3 # m

tA, xA = np.loadtxt(filA, skiprows=10, max_rows=300).T
tB, xB = np.loadtxt(filB, skiprows=20, max_rows=300).T

xerrA = np.ones_like(xA)*1/3*dotr
xerrB = np.ones_like(xB)*1/3*dotr


p0A = [0.04, 0.001, 0.02, 2, 0]
p0B = [0.02, 0.001, 0.02, 3, 0]


# Figur funktion 
fig, ax = plt.subplots(2, 2, sharex=True, sharey="row", figsize=(10, 8), 
                       gridspec_kw={'height_ratios': [3, 1], "hspace": 0.1, "wspace": 0.02})
fig.suptitle("Position som funktion af tid", size=20)

def figs(t,x, xerr, p0, axi, cold='C0', coll='C1'):
    t0 = t[0]
    t = t-t0
    tlin = np.linspace(0, t[-1], 1000)

    ax[0, axi].plot(t,x,'o', ms=4, color=cold, label="Data")
    #ax[0, axi].plot(tlin, dSHB(tlin, *p0), label="p0") # plot gæt
    
    popt, pcov = curve_fit(dSHB, t,x, p0=p0, sigma=xerr, 
                           absolute_sigma=True, maxfev=10000, xtol=1e-4, ftol=1e-4)
    
    ax[0, axi].plot(tlin, dSHB(tlin, *popt), color=coll, label="Fit")
    ax[0, axi].axhline(popt[4], t[0], t[-1], color='black')
    ax[1, axi].set_xlabel("tid (s)")
    ax[0, 0].set_ylabel("x (m)")
    
    #data-fir/sqrt(err)
    resid = (x-dSHB(t, *popt))/np.sqrt(xerr)
    ax[1, axi].plot(t, resid, 'o', color=cold, ms=4, alpha=0.5)
    ax[1, 0].set_ylabel("Residual")
    ax[1, axi].axhline(0, t[0], t[-1], color='black')
    
    ax[0, axi].legend()
    
    print(f"Værdier: {popt}")
    perr = np.sqrt(np.diag(pcov))
    print('usikkerheder:',perr)
    chmin = np.sum(((x-dSHB(t, *popt))/xerr)**2)
    print(f'chi2: {chmin:} ---> p: {ss.chi2.cdf(chmin,4)}')
    print("-----------")
    return [popt, pcov]

poptA, pcovA = figs(tA,xA,xerrA,p0A, 0)
poptB, pcovB = figs(tB,xB,xerrB,p0B, 1, 'C2', 'C3')

usikA = np.sqrt(np.diag(pcovA))
usikB = np.sqrt(np.diag(pcovB))

T = (2*np.pi/abs(poptA[2])+2*np.pi/abs(poptB[2]))/2
Tu = abs(T-(2*np.pi/abs(poptA[2]+usikA[2])+2*np.pi/abs(poptB[2]+usikB[2]))/2)
print(f"Periode: {T/60:.2f} \u00B1 {Tu/60:.2f} min")


κ = I*((2*np.pi)/T)**2
κu = abs(κ-I*((2*np.pi)/(T+Tu))**2)
κs = 8.5*10**-9 # N*m / rad

print(f"k: {κ:.6g} \u00B1 {κu:.3g}")

xA0 = poptA[4]
xB0 = poptB[4]
xB0 = -0.02
θA = np.arctan(xA0/y) # radianer
θB = np.arctan(xB0/y) # radianer 

#print(f"mak vinkel fit A: {θA*180/np.pi}")
#print(f"mak vinkel fit B: {θB*180/np.pi}")

Δθ = abs((θA-θB)/4)
Δθu = abs(Δθ-abs((np.arctan((xA0+usikA[4])/y)-np.arctan((xB0+usikB[4])/y))/4))

print(f"Vinkeludsving: {Δθ:.6g} \u00B1 {Δθu:.3g}")


G = κ*Δθ*r**2/(M*m*d*2)
Gu = abs(G - ((κ+κu)*(Δθ+Δθu)*r**2/(M*m*d*2)))

print(f"G: {G:.6g} \u00B1 {Gu:.3g}")

af = (G - 6.67508*10**(-11))/(6.67508*10**-11)*100
afu = abs(af - (((G+Gu) - 6.6743*10**(-11))/(6.6743*10**-11)*100))

print(f"Procentvis afvigelse: {af:.6g}% \u00B1 {afu:.3g}%")

print(κ*Δθ*r**2/(M*m*d*2)-κ*Δθ*r**2/(M*m*d*2)*np.cos(Δθ))

