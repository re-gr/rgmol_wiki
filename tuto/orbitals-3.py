import rgmol
import rgmol.examples

file = rgmol.examples.molden_H2CO
mol = rgmol.extract_molden.extract(file,do_order_bonds=1)
mol.plot_MO()