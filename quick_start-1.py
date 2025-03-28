import rgmol
import rgmol.examples

file = rgmol.examples.adf_CH3Cl
mol = rgmol.extract_adf.extract(file)
mol.plot_radius()