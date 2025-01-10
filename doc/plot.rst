Plotting Methods
================

| The plotting methods produce visual outputs for multiple visualization packages.
| In order to chose which package will be used, one needs to 

| All the plotting functions are identical regardless of the visualization package.
| Some of the functions are still not implemented for all packages, but will eventually.
| The recommended visualization package is **pyvista** as most of the methods are tested on it. 
| The other packages : matplotlib and plotly are not guaranteed to work properly.


General Molecule Methods
------------------------

.. list-table::
	
    * - :doc:`molecule.plot_radius<plot/plot_radius>`
      - plot the radius of each atom   
    * - :doc:`molecule.plot_property<plot/plot_property>`
      - plot a property for each atom
    * - :doc:`molecule.plot_vector<plot/plot_vector>`
      - plot a vector on each atom
    * - :doc:`molecule.plot_isodensity<plot/plot_isodensity>`
      - plot the isodensity of a density
	  
	  
Orbitals Molecule Methods
-------------------------

.. list-table::

	 * - :doc:`molecule.plot_AO<plot/plot_AO>`
      - plot the atomic orbitals
	 * - :doc:`molecule.plot_MO<plot/plot_MO>`
      - plot the molecular orbitals
	  * - :doc:`molecule.plot_transition_density<plot/plot_transition_density>`
      - calculate the transition densities from the MO and plot them
	  
CDFT Molecule Methods
---------------------	  
	 
.. list-table::
    * - :doc:`molecule.plot_diagonalized_condensed_kernel<plot/plot_diagonalized_condensed_kernel>`
      - diagonalize and plot each eigenmode of a condensed kernel
	  * - :doc:`molecule.plot_diagonalized_kernel<plot/plot_diagonalized_kernel>`
      - calculate, diagonalize and plot the eigenmode of a non condensed kernel
	  
	 



   
