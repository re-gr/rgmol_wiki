import rgmol
import rgmol.plot_pyvista
import rgmol.examples

file = rgmol.examples.adf_CH3Cl
mol = rgmol.extract_adf.extract(file)
mol.plot_radius()