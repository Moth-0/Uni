import matplotlib.pyplot as plt
import numpy as np
import pandas

# Question 2

def Lorentz(x):
    return 1 / (1 + x ** 2)

plt.subplot(4, 2, 1)
x = np.linspace(-10, 10, 1000)
plt.plot(x, Lorentz(x), label="default")

# Question 3
def Lorentz(x, x0=0, height=1, width=2):
    return height / (1 + (2 * (x - x0) / width) ** 2)

plt.subplot(4, 2, 2)
for (x0, height, width) in [(-5, 5, 1), (2, 2, 6), (5, 3, 0.5)]:
    plt.plot(x, Lorentz(x, x0=x0, width=width, height=height))

# Question 4
def peak_width(amino, atom_id):
    if atom_id == 'H': return 6
    if (amino, atom_id) in {('ASN', 'HD21'), ('ASN', 'HD22'),
                            ('GLN', 'HE21'), ('GLN', 'HE22')}:
        return 25
    return 4

# Question 5
def atom_peak(amino, atom_id, MHz):
    width = peak_width(amino, atom_id)
    height = 2 / width
    x0 = MHz
    return (x0, height, width)

peaks = [atom_peak(amino, atom_id, MHz) for amino, atom_id, MHz in
         [('PHE', 'H', 3481), ('ASN', 'HD21', 3053), ('ILE', 'HA', 1673)]]

x = np.linspace(1500, 4000, 1000)

plt.subplot(4, 2, 3)
for x0, height, width in peaks:
   plt.plot(x, Lorentz(x, x0=x0, height=height, width=width))

plt.subplot(4, 2, 4)
plt.plot(x, sum(Lorentz(x, x0=x0, height=height, width=width)
                for x0, height, width in peaks), 'k', alpha=0.7)

# Question 6
def read_molecule(filename):  # returns pandas dataframe
    return pandas.read_csv(filename)

# Question 7
NFGAIL = read_molecule('NFGAIL.csv')

MHz = 400.13

peaks = [atom_peak(row['Comp_ID'], row['Atom_ID'], row['Val'] * MHz)
          for idx, row in NFGAIL.iterrows()]

plt.subplot(4, 2, 5)
xs = [x0 for (x0, height, width) in peaks]
xmin = min(xs)
xmax = max(xs)
padding = (xmax - xmin) * 0.1
xmax += padding
xmin -= padding
x = np.linspace(xmin, xmax, 1000)
plt.plot(x / MHz, sum(Lorentz(x, *peak) for peak in peaks))
plt.xlim(xmax / MHz, xmin / MHz)  # revert axis
    
# Question 8

def apply_coupling(A, B, J):
    nu_A, height_A, width_A = A
    nu_B, height_B, width_B = B

    if J == 0 or nu_A == nu_B:
        return [B]

    Q = np.sqrt((nu_A - nu_B) ** 2 + J **2)
    nu_m = (nu_A + nu_B) / 2
    sign = 1 if nu_A < nu_B else -1
    a_in = (1 + J / Q) / 2
    a_out = (1 - J / Q) / 2

    B_in  = (nu_m + sign * (Q - J) / 2, a_in  * height_B, width_B)
    B_out = (nu_m + sign * (Q + J) / 2, a_out * height_B, width_B)

    return [B_in, B_out]

A = (25, 1, 1)
B = (75, 1, 1)
J = 10

peaks = apply_coupling(A, B, J) + apply_coupling(B, A, J)

plt.subplot(4, 2, 6)
x = np.linspace(0, 100, 1000)
for peak in peaks:
    plt.plot(x, Lorentz(x, *peak))

# Question 9

def apply_coupling(A, B, J, B_=None):
    if B_ is None:
        B_ = B
        
    nu_A, height_A, width_A = A
    nu_B, height_B, width_B = B
    nu_B_, height_B_, width_B_ = B_

    if J == 0 or nu_A == nu_B:
        return [B]

    Q = np.sqrt((nu_A - nu_B) ** 2 + J **2)
    nu_m = (nu_A + nu_B) / 2
    sign = 1 if nu_A < nu_B else -1
    a_in = (1 + J / Q) / 2
    a_out = (1 - J / Q) / 2

    B_in  = (nu_B_ - nu_B + nu_m + sign * (Q - J) / 2, a_in  * height_B_, width_B)
    B_out = (nu_B_ - nu_B + nu_m + sign * (Q + J) / 2, a_out * height_B_, width_B)

    return [B_in, B_out]

def apply_couplings(couplings, B):
    Bs = [B]
    for (A, J) in couplings:
        Bs = [B_new for B_ in Bs for B_new in apply_coupling(A, B, J, B_)]

    return Bs

A1 = (3, 1, 1)
A2 = (5, 1, 1)
B = (9, 1, 1)
J1 = 1
J2 = 2

peaks = apply_couplings([(A1, J1), (A2,J2)], B)

plt.subplot(4, 2, 7)
x = np.linspace(0, 20, 1000)
for peak in [A1,A2,B]:
    plt.plot(x, Lorentz(x, *peak), 'k:')
for peak in peaks:
    plt.plot(x, Lorentz(x, *peak))

# Question 10 # returns pandas dataframe

couplings = pandas.read_csv('couplings.csv')

# Question 11

def split_comps(molecules): # molecules = pandas dataframe
    return molecules.groupby(['Seq_ID'])

# Question 12 

def comp_peaks(comp, couplings, input_MHz): # comp pandas dataframe
    atoms = [(row['Comp_ID'], row['Atom_ID'], row['Val'] * MHz)
             for idx, row in comp].iterrows()]
    peaks = []
    for B_amino, B_atom_id, B_nu in atoms:
        As = []
        for A_amino, A_atom_id, A_nu in atoms:
            for idx, row in couplings.iterrows():
                if (row['Amino acid'] == B_amino and
                    ((row['Atom 1'] == B_atom_id and
                      row['Atom 2'] == A_atom_id) or
                     (row['Atom 2'] == B_atom_id and
                      row['Atom 1'] == A_atom_id))
                    ):
                    J = row['Coupling']
                    As.append((atom_peak(A_amino, A_atom_id, A_nu), J))
                    break
        B = atom_peak(B_amino, B_atom_id, B_nu)
        peaks += apply_couplings(As, B)             
    return peaks

# Question 13

def protein_peaks(atoms, couplings, input_MHz):
    comps = split_comps(atoms) # pandas data frames
    peaks = []
    for idx, comp in comps:
        peaks += comp_peaks(comp, couplings, input_MHz)
    return peaks

peaks = protein_peaks(NFGAIL, couplings, 400.13)

plt.subplot(4, 2, 8)
xs = [x0 for (x0, height, width) in peaks]
xmin = min(xs)
xmax = max(xs)
padding = (xmax - xmin) * 0.1
xmax += padding
xmin -= padding
x = np.linspace(xmin, xmax, 1000)
plt.plot(x / MHz, sum(Lorentz(x, *peak) for peak in peaks))
plt.xlim(xmax / MHz, xmin / MHz)  # revert axis

plt.show()

