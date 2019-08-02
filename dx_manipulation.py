#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 15:53:36 2018

@author: eric
"""

from gridData import Grid



g=Grid("gist-order-norm.dx")
print(g.grid)

n=g.grid

print(type(n))
edge=g.edges
print(edge)
print(edge[0].size)
print(edge[1].size)
print(edge[2].size)

print((edge[0][-1]+edge[0][0])/2)

print((edge[1][-1]+edge[0][0])/2)

print((edge[2][-1]+edge[0][0])/2)




print(n)
print(n.shape)
print(n.dtype)

print(n[0,0,0])
print(n[0,1,0])
print(n[0,0,1])
print(n[1,0,0])

print(n[0,2,0])



import matplotlib.pyplot as plt


x=[]
y=[]
point=0

for i in range(48):
    for j in range(48):
        for k in range(48):
            y.append(n[i,j,k])
            if n[i,j,k]>3 or n[i,j,k]<-3:
                print("the big value is: ")
                print(n[i,j,k])
                
                print("the position is: " + str(i)+" " +str(j)+ " " +str(k))
                n[i,j,k]=3
            k=k+1
            point=point+1
            x.append(point)
        j=j+1
    i=i+1

fig=plt.figure()

ax1=fig.add_subplot(211)
ax1.set_ylabel("voxel value")
ax1.set_xlabel("voxel position")
ax1.set_title("order-norm voxel value distribution")
ax1.plot(x,y,c='b')
leg=ax1.legend()

plt.show()

fig.savefig("order-norm_distribution.png")



            
            
            
