import rgmol
import rgmol.plot_pyvista
import rgmol.examples

file = rgmol.examples.molden_H2CO
mol = rgmol.extract_molden.extract(file,do_find_bonds=1)
mol.plot_AO(delta=5,grid_points=(80,80,80))