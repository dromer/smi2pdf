import sys, os
from oasa import smiles, cairo_out

for line in file(sys.argv[1]):

	smile, name = line.split()
	
	mol = smiles.text_to_mol(smile)
	mol.normalize_bond_length( 30)
	mol.remove_unimportant_hydrogens()
	cairo_out.mol_to_cairo( mol, name + ".pdf", format="pdf")

