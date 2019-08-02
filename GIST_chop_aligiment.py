#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:15:31 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Tom Kurtzman's Lab
"""


## this script require pymol module, you may need to use the python path that same as pymol
# or you will not able to import pymol

## required files:  ID_protein.pdb ID_ligand.mol2 from PDBbind, traj_MD.pdb

import os
os.getcwd()

import pymol
import __main__
## Here I take the ID=ib8n for example.
##After I have the all protein list, I can read the pdb id and ligand names automatically

pdb_id="1b8n"
ligand_id="IMG"
#### Using pymol to align the pdb structure with the traj_MD.pdb file 

# For the structure in PDBbind, use the ID_protein.pdb and ID_ligand.mol2 file from
#pdbbind

# Merge the protein with the ligand (from PDBBind database) and output a combinded.pdb file

__main__.pymol_argv=['pymol','-qc'] # load the pymol quietly and with GUI

pymol.cmd.load(pdb_id+"_protein.pdb","protein")

pymol.cmd.remove("resn hoh") # strip the water molecule

pymol.cmd.load(pdb_id+"_ligand.mol2","ligand")

pymol.cmd.save("combined.pdb","all") # conbind.pdb is the protein-ligand complex structure

pymol.cmd.delete("all")

pymol.cmd.load("combined.pdb","combined")

pymol.cmd.load("traj_MD.pdb","reference") # load the gist protein

pymol.cmd.align("combined","reference")

pymol.cmd.save("aligned_complex.pdb","combined")

pymol.cmd.remove("all")

pymol.cmd.load("aligned_complex.pdb","aligned")

pymol.cmd.select("aligned_ligand","resn "+ligand_id)

pymol.cmd.save("aligned_ligand.pdb","aligned_ligand")
 # Save the aligned ligand pdb file to the find the GIST center.










