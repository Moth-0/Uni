import pandas as pb

# https://bmrb.io/ftp/pub/bmrb/relational_tables/nmr-star3.1/Atom_chem_shift.csv
shifts = pb.read_csv('Atom_chem_shift.csv')
shifts[shifts.Entry_ID == 68].to_csv('68_ubiquitin.csv', index=False)
shifts[shifts.Entry_ID == 6203].to_csv('ThrB12-DKP-insulin.csv', index=False)
