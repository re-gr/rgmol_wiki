import rgmol
import rgmol.examples

file = rgmol.examples.molden_H2CO
mol = rgmol.extract_molden.extract(file,do_order_bonds=1)
rgmol.extract_orca.extract_properties(rgmol.examples.orca_H2CO,mol=mol)

file_m = rgmol.examples.molden_H2CO_m
mol_m = rgmol.extract_molden.extract(file_m,do_order_bonds=1)

mol.plot_fukui_function(mol_m=mol_m,fukui_type="f-")