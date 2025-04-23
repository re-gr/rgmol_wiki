import rgmol
import rgmol.examples

list_molecules = []

file = rgmol.examples.adf_CH4
mol = rgmol.extract_adf.extract(file)
list_molecules.append(mol)

file2 = rgmol.examples.adf_CH3Cl
mol2 = rgmol.extract_adf.extract(file2)
list_molecules.append(mol2)

group_mol = rgmol.group_molecules(list_molecules)
group_mol.plot_radius()