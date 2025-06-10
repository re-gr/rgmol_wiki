import rgmol
import rgmol.examples

file = rgmol.examples.cube_H2CO_MO59
mol = rgmol.extract_cube.extract(file,do_order_bonds=1)
mol.plot_isodensity()