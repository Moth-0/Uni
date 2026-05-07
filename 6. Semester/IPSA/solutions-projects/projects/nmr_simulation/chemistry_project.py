import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import csv
import time
from math import sqrt

coupling_file = 'projects\\nmr_simulation\\couplings.csv'
polygon_points = 10000
padding_factor = 0.05  # fraction of space outside leftmost and rightmost peak

linewidth = {
  'default': 4,
  'H': 6,  # applies to all amnio acids
  'ASN,HD21': 25,
  'ASN,HD22': 25,
  'GLN,HE21': 25,
  'GLN,HE22': 25
}


def Lorentz(x, x0=0.0, height=1.0, width=2.0):
    '''Compute the Lorentz function with FWHH = width and
       peak at (x0,heigh) at value x'''
    
    return height / (1 + (2*(x - x0) / width)**2)


def peak_width(amino, atom_id):
    '''Lookup peak width in linewidth table'''
    
    for key in [amino + ',' + atom_id, atom_id, 'default']:
        if key in linewidth:
            return linewidth[key]


def atom_peak(amino, atom_id, Hz):
    '''Return peak (mu, height, width) for atom_id in amino
       with area below curve equal to standard Lorentz curve
    '''
    
    width = peak_width(amino, atom_id)
    height = 2.0 / width
    return (Hz, height, width)
    

def atoms_to_peaks(atoms, input_MHz):
    return [atom_peak(atom['Comp_ID'],
                      atom['Atom_ID'],
                      input_MHz * float(atom['Val'])
                     )
            for atom in atoms]


def eval_peak(x, peak):
    nu, height, width = peak
    return Lorentz(x, x0=nu, height=height, width=width)


def eval_peaks(x, peaks):
    return sum(eval_peak(x, p) for p in peaks)


###################
# Coupling


def apply_coupling(A, B, J, B_peaks=None):
    '''Apply coupling effect of peak A to B_peaks with magnitude J
       and return list of resulting new B peaks.
       B_peaks = the list of already slittings of B (default [B])
    '''

    nu_A, _, _ = A
    nu_B, _, _ = B

    if B_peaks == None:
        B_peaks = [B]
    
    if nu_A == nu_B:
        return B_peaks

    Q = sqrt(J ** 2 + (nu_B - nu_A) ** 2)

    ampl_outer = (1 - J / Q) / 2
    ampl_inner = (1 + J / Q) / 2
    nu_m = (nu_A + nu_B) / 2
    
    SIGN = 1 if nu_A < nu_B else -1

    nu_inner = nu_m + SIGN * (Q - J) / 2
    nu_outer = nu_m + SIGN * (Q + J) / 2
    
    new_peaks = []
    for nu, height, width in B_peaks:
        D = nu - nu_B
        new_peaks.extend([
          (D + nu_inner, ampl_inner * height, width),
          (D + nu_outer, ampl_outer * height, width)
        ])
    return new_peaks


def apply_couplings(couplings, B):
    '''Apply sequence of couplings (A1, J1), (A2, J2),... to B'''

    B_peaks = [B]
    for A, J in couplings:
        B_peaks = apply_coupling(A, B, J, B_peaks)
    return B_peaks


def split_aminos(atoms):  # Are atoms in 'sorted' order wrt Seq_ID ?
    '''Split list of atoms into sublists based on Seq_ID'''

    def key(atom):
        return (atom['Entity_ID'], atom['Seq_ID'])
    
    seq_ids = sorted({key(atom) for atom in atoms})
    aminos = {seq: [] for seq in seq_ids}
    for atom in atoms:
        aminos[key(atom)].append(atom)
    return list(aminos.values())


def amino_peaks(amino, couplings, input_MHz): 
    '''Compute all peaks for a given amino acid'''

    amino_id = amino[0]['Comp_ID']
    atoms = {atom['Atom_ID']: atom for atom in amino}
    peak = {atom_id: atom_peak(amino_id, atom_id, input_MHz * float(atom['Val']))
            for atom_id, atom in atoms.items()}

    peaks = []

    for B_id in atoms:
        As = []
        if B_id in couplings[amino_id]:
            for A_id, J in couplings[amino_id][B_id].items():
                if A_id in atoms:
                    As.append((peak[A_id], J))
        peaks.extend(apply_couplings(As, peak[B_id]))
    
    return peaks


def protein_peaks(atoms, couplings, input_MHz):
    peaks = []
    for amino in split_aminos(atoms):
        peaks.extend(amino_peaks(amino, couplings, input_MHz))
    return peaks


###############
# File IO

def read_molecule(molecule_file):
    '''Read molecule as list of atoms (dictionaries) from csv file'''
    
    with open(molecule_file, 'r', newline='') as file:
        csv_in = csv.reader(file) #, delimiter=";")
        header = next(csv_in)
        atoms = [dict(zip(header, row)) for row in csv_in]
    return atoms


def read_couplings(coupling_file):
    '''Read coupling among atoms in amino acids from csv file
        * coupling[amino][atom1][atom2] = Coupling value
    '''
    
    couplings = {}
    with open(coupling_file, 'r', newline='') as file:
        csv_in = csv.reader(file)  #, delimiter=';')
        header = next(csv_in)  # Currently ignored
        for row in csv_in:
            amino, atom1, atom2, J = row  # Modify to generic input!!!
            if amino not in couplings:
                couplings[amino] = {}
            for atom in [atom1, atom2]:
                if atom not in couplings[amino]:
                    couplings[amino][atom] = {}
            if atom2 in couplings[amino][atom1]:
                print(f'WARNING: couplings ({atom1}, {atom2}) already defined for {amino}')
            couplings[amino][atom1][atom2] = float(J)
            couplings[amino][atom2][atom1] = float(J)
    return couplings

def csv_extract(file_name_in, file_name_out, conditions):
    '''Extract rows from large csv file to (smaller) filer
         * file_name_in input csv file
         * file_name_out output csv file
         * only rows matching conditions = {column: value, ...}
    '''

    filters = " ".join(f'{column}={value}' for column, value in conditions.items())
    print(f'Extracting {file_name_in} -> {file_name_out} ({file_name_out})')

    start = time.time()
    count = 0

    with open(file_name_in, 'r', newline='') as file_in:
        with open(file_name_out, 'w', newline='') as file_out:

            csv_in = csv.reader(file_in)
            csv_out = csv.writer(file_out)

            header = next(csv_in)
            csv_out.writerow(header)

            for column in set(conditions) - set(header):
                print(f'WARNING: Column {column} does not exist')
            filters = [(header.index(column), value)
                for column, value in conditions.items() if column in header]
            for row in csv_in:
                if all(row[column] == value for column, value in filters):
                    csv_out.writerow(row)
                    count += 1

    end = time.time()
    duration = end - start
    print(f'Duration: {duration:.1f} seconds, {count} lines selected')


#######################################
#  PLOT FIGURES
#######################################


def plot_lorentz_line():
    '''Plot Lorentz line (standard parameters)'''
    
    X = np.linspace(-10, 10, polygon_points)
    plt.plot(X, Lorentz(X), label='Lorentz line')
    plt.plot([-1, 1], [0.5, 0.5], '-', label='width')
    plt.plot(0, 1, 'o', label='(x$_0$, height)')
    plt.xticks([-10, -5, 0, 5, 10])
    plt.yticks([0, 0.5, 1])
    plt.legend()


def plot_lorentz_examples():
    '''Plot Lorentz lines with parameters'''

    X = np.linspace(-10, 10, polygon_points)
    peaks = [(-5, 5, 1), (2, 2, 6), (5, 3, 0.5)]
    for x0, height, width in peaks:
        plt.plot(X,
                 Lorentz(X, x0=x0, height=height, width=width),
                 label=f'({x0}, {height}, {width})')
    plt.plot(X, eval_peaks(X, peaks), label='sum')
    plt.xticks([-10, -5, 0, 5, 10])
    plt.yticks([0, 1, 2, 3, 4, 5])
    plt.title('Lorentz lines (x$_0$, height, width)')
    plt.legend()


def plot_atom_examples():
    X = np.linspace(1000, 4000, polygon_points)
    atoms = [(8.7, 'PHE', 'H'), (7.63, 'ASN', 'HD21'), (4.18, 'ILE', 'HA')]
    peaks = []
    for ppm, amino, atom_id in atoms:
        nu = ppm * 400.13
        peak = atom_peak(amino, atom_id, nu)
        plt.plot(X,
                 eval_peak(X, peak),
                 label=f'{amino} {atom_id} $\\nu$={nu:.0f}')
        peaks.append(peak)
    plt.xlabel("Hz")
    plt.plot(X, eval_peaks(X, peaks), ":", label="sum")
    plt.ylim(0, 0.6)
    plt.legend()


def plot_two_coupled_peaks():
    J = 10
    A = (25, 1, 1)
    B = (75, 1, 1)
    
    X = np.linspace(0, 150, polygon_points)
    plt.plot(X, eval_peak(X, A), "C0:", label=f"{A = }")
    plt.plot(X, eval_peak(X, B), "C1:", label=f"{B = }")

    As = apply_coupling(B, A, J)
    for idx, peak in enumerate(As):
        plt.plot(X, eval_peak(X, peak), "C0", label="A splits" if idx == 0 else None)
    Bs = apply_coupling(A, B, J)
    for idx, peak in enumerate(Bs):
        plt.plot(X, eval_peak(X, peak), "C1", label="B splits" if idx == 0 else None)

    plt.xlabel("Hz")
    plt.legend(title=r"Coupling J$_{\mathrm{AB}}$=10")


def plot_three_coupled_peaks():
    J_A1 = 1
    J_A2 = 2
    
    A1 = (3, 1, 1)
    A2 = (5, 1, 1)
    B = (9, 1, 1)
    
    X = np.linspace(0, 25, polygon_points)
    plt.plot(X, eval_peak(X, A1), "C0:", label=f"A$_1$ = {A1}")
    plt.plot(X, eval_peak(X, A2), "C1:", label=f"A$_2$ = {A2}")
    plt.plot(X, eval_peak(X, B), "C2:", label=f"B = {B}")

    Bs = apply_couplings([(A1, J_A1), (A2, J_A2)], B)
    for idx, peak in enumerate(Bs):
        plt.plot(X, eval_peak(X, peak), "C2", label="B splits" if idx == 0 else None)
    plt.plot(X, eval_peaks(X, Bs), label="B splits, sum")

    plt.xlabel("Hz")
    plt.xticks(range(0, 26, 5))
    plt.legend(title=r"Coupling J$_{\mathrm{A}_1\mathrm{B}}$=%s J$_{\mathrm{A}_2\mathrm{B}}$=%s" % (J_A1, J_A2))


def plot_spectra(peaks, input_MHz, title, plot_args={}):
    '''Plot the sum of a list of peaks, converting
       x values from MHz to PPM by ppm = nu / MHZ
    '''

    x = [x0 for x0, height, width in peaks]
    min_x = min(x)
    max_x = max(x)
    padding = padding_factor * (max_x - min_x)
    
    X = np.linspace(min_x - padding, max_x + padding, polygon_points)
    plt.plot(X / input_MHz, eval_peaks(X, peaks), label=title, **plot_args)
    plt.xlabel('ppm (parts per million)')
    plt.ylabel('intensity')
    ax = plt.gca()
    ax.invert_xaxis()  # make x-axis decreasing left-to-right
    plt.legend()


def plot_molecule(csv_file, title, input_MHz):
    atoms = read_molecule(csv_file)
    peaks = atoms_to_peaks(atoms, input_MHz)
    print(csv_file, "uncoupled peaks", len(peaks))
    print('Peaks:', peaks)
    plot_spectra(peaks, input_MHz, "no coupling", plot_args={"alpha": 0.25})
    coupled_peaks = protein_peaks(atoms, couplings, input_MHz)
    print(csv_file, "coupled peaks", len(coupled_peaks))
    plot_spectra(coupled_peaks, input_MHz, "with coupling")
    print('Coupled peaks:', coupled_peaks)

    plt.xlabel('ppm (parts per million)')
    plt.ylabel('intensity')
    ax = plt.gca()
    ax.invert_xaxis()  # make x-axis decreasing left-to-right
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    plt.legend(title=f"{title} ({input_MHz} MHz)")
    

###########
# MAIN

couplings = read_couplings(coupling_file)
for i, k in enumerate(couplings):
    print(f'\n{i} - {k}: ') 
    for v in couplings[k]:
        print(f'{v}: {couplings[k][v]}')

# plt.rcParams.update({'legend.fontsize': 9})

# plt.subplot2grid((2, 3), (0, 0))
# plot_lorentz_line()
# plt.subplot2grid((2, 3), (0, 1))
# plot_lorentz_examples()
# plt.subplot2grid((2, 3), (0, 2))
# plot_atom_examples()

# plt.subplot2grid((2, 3), (1, 0))
# NFGAIL_atoms = read_molecule("projects\\nmr_simulation\\NFGAIL.csv")
# NFGAIL_peaks = atoms_to_peaks(NFGAIL_atoms, 400.13)

# print(f'{len(NFGAIL_peaks)}')

# plot_spectra(NFGAIL_peaks, 400.13, "NFGAIL")

# plt.subplot2grid((2, 3), (1, 1))
# plot_two_coupled_peaks()
# plt.subplot2grid((2, 3), (1, 2))
# plot_three_coupled_peaks()

# #plt.tight_layout()
# plt.show()

# #csv_extract("Atom_chem_shift.csv", "entry68.csv", {"Entry_ID": "68"})
# #csv_extract("Atom_chem_shift.csv", "entry6203.csv", {"Entry_ID": "6203"})

# plt.subplot2grid((3, 1), (0, 0))
# plot_molecule("projects\\nmr_simulation\\NFGAIL.csv", "Peptide NFGAIL", 400.13)
# plt.subplot2grid((3, 1), (1, 0))
# plot_molecule("projects\\nmr_simulation\\68_ubiquitin.csv", "Ubiquitin", 500)
# plt.subplot2grid((3, 1), (2, 0))
# plot_molecule("projects\\nmr_simulation\\entry6203.csv", "ThrB12-DKP-insulin", 500)

# #plt.tight_layout()
# plt.show()

# # EOF 
