import rgmol
import rgmol.examples

file = rgmol.examples.molden_H2CO
mol = rgmol.extract_molden.extract(file,do_find_bonds=1)
rgmol.extract_orca.extract_transition(rgmol.examples.orca_H2CO,mol=mol)

file_m = rgmol.examples.molden_H2CO_m
mol_m = rgmol.extract_molden.extract(file_m,do_find_bonds=1)

mol.plot_fukui_function(mol_m=mol_m,fukui_type="f-",grid_points=(100,100,100),delta=10)