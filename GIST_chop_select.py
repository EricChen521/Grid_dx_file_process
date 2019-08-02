#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:03:58 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

## find the ligand center of the aligned ligand
x=[]
y=[]
z=[]

ligand_file=open("aligned_ligand.pdb","r+").readlines()

for line in ligand_file:
    if "HETATM" in line:
        x.append(float(line[30:38]))
        y.append(float(line.split[38:46]))
        z.append(float(line.split[46:54]))

x_center=round(sum(x)/len(x),3)
y_center=round(sum(y)/len(y),3)
z_center=round(sum(z)/len(z),3)

## get the edges of GIST box

import glob,os
import numpy as np

from gridData import Grid

gist_data=sorted(glob.glob("gist*dx")) 

g1=Grid(gist_data[0])


coordinate=g1.edges

closest_x=min(coordinate[0],key=lambda x:abs(x-x_center))

x_index,=np.where(coordinate[0]==closest_x)

closest_y=min(coordinate[1],key=lambda y:abs(y-y_center))

y_index,=np.where(coordinate[1]==closest_y)

closest_z=min(coordinate[2],key=lambda z:abs(z-z_center))

z_index,=np.where(coordinate[2]==closest_z)


choped_x_array=coordinate[0][x_index[0]-24:x_index[0]+25]
choped_y_array=coordinate[1][y_index[0]-24:y_index[0]+25]
choped_z_array=coordinate[2][z_index[0]-24:z_index[0]+25]


choped_coordinate=[choped_x_array,choped_y_array,choped_z_array]

## get the values from the whole protien GIST
for dx in gist_data:
    g=Grid(dx)
    values=g.grid 


    choped_values=np.zeros((48,48,48))

    for i in range(48):
        for j in range(48):
            for k in range(48):
                choped_values[i,j,k]=values[x_index[0]-24+i,y_index[0]-24+j,z_index[0]-24+k]
                k+=1
            j+=1
        i+=1

    g_choped=Grid(choped_values,edges=choped_coordinate)
    g_choped.export(dx.split(".")[0]+"-LC.dx","DX")



