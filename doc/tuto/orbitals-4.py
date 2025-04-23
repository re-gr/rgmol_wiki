import rgmol
import rgmol.examples

file = rgmol.examples.molden_CH3Cl
mol = rgmol.extract_molden.extract(file,do_order_bonds=1)
rgmol.extract_orca.extract_properties(rgmol.examples.orca_CH3Cl,mol=mol)
mol.plot_transition_density(delta=5,grid_points=(80,80,80),opacity_radius=.4)