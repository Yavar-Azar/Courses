import argparse
import numpy as np
import matplotlib.pyplot as plt
from ase.io import read
from ase.calculators.espresso import Espresso
from ase.dft.kpoints import BandPath
from ase.spectrum.band_structure import BandStructure

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Plot band structure from QE.')
parser.add_argument('cif_file', help='Path to the CIF file')
args = parser.parse_args()

# Define the pseudopotentials dictionary
pseudo_dict = {
    "Ti": "Ti_pbe_v1.4.uspp.F.UPF",
    "Ba": "Ba.pbe-spn-kjpaw_psl.1.0.0.UPF",
    "O": "O.pbe-n-kjpaw_psl.0.1.UPF"
}

# Read the CIF file
ase_obj = read(args.cif_file)
input_data={
        "pseudo_dir": "./",
        'control': {
            'calculation': 'scf',
            'verbosity': 'high',
            'pseudo_dir': "./",
            'restart_mode': 'from_scratch',
            'tstress': True
        },
        'ecutrho': 240,
        'ecutwfc': 30,
        'diagonalization': 'david',
        'occupations': 'smearing',
        'smearing': 'mp',
        'mixing_mode': 'plain',
        'mixing_beta': 0.7,
        'degauss': 0.001,
        'nspin': 1
    }
# Set up the calculator
calc = Espresso(
    pseudopotentials=pseudo_dict,
    kpts=(4, 4, 4),input_data=input_data)

# Attach the calculator to the ASE object and calculate the energy
ase_obj.calc = calc
ase_obj.get_potential_energy()


# Get the Fermi level
fermi_level = calc.get_fermi_level()

# Get the lattice and band path
lattice = ase_obj.get_cell()
bandpath = lattice.bandpath(npoints=100)

# Set up the calculator for band structure calculation
input_data['control'].update({'calculation':'bands','restart_mode':'restart','verbosity':'high'})

calc.set(kpts=bandpath, input_data=input_data)
calc.calculate(ase_obj)

# Get the band structure and modify the energies
bs = calc.band_structure()
new_band = BandStructure(energies=bs.energies - fermi_level * np.ones_like(bs.energies), path=bs.path)

new_band.plot()
# Plot and save the band structure

plt.savefig("band.png", dpi=300)
plt.show()

