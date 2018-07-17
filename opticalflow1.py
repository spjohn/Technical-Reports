# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 15:26:13 2018

@author: Student
"""
from PIL import Image,ImageDraw 
im=Image.open('OF1.png').convert('L')

#im.show()
im.save('OF11.png')
size=im.size
im=Image.open('OF2.png').convert('L')
#im.show()
im.save('OF22.png')
size=im.size

from scipy.ndimage import sobel
from scipy.misc import toimage,imread
im1=imread('OF11.png')
im2=imread('OF22.png')
ix=sobel(im1,0)
iy=sobel(im1,1)
it=im1-im2
toimage(ix).save('Ix.png')
toimage(iy).save('Iy.png')
toimage(it).save('It.png')
import numpy as np
ix_sq=np.square(ix)
iy_sq=np.square(iy)
ix_iy=np.multiply(ix,iy)
ix_it=np.multiply(ix,it)
iy_it=np.multiply(iy,it)
u=np.zeros((size[1],size[0]))
v=np.zeros((size[1],size[0]))
toimage(ix_sq).save('Ixsquare.png')
toimage(iy_sq).save('Iysquare.png')
toimage(ix_iy).save('IxIy.png')
toimage(ix_it).save('IxIt.png')
toimage(iy_it).save('IyIt.png')
im=Image.open('OF11.png')
for i in range(2,size[1]-3):
    for j in range(2,size[0]-3):
        int1=0
        int2=0
        int3=0
        int4=0
        int5=0
        for m in range(-2,2):
            for n in range(-2,2):
            
                int1=int1+ix_sq[i+m][j+n]
                int2=int2+iy_sq[i+m][j+n]
                int3=int3+ix_iy[i+m][j+n]
                int4=int4+ix_it[i+m][j+n]
                int5=int5+iy_it[i+m][j+n]
        
        mat1=np.array([[int1,int3],[int3,int2]])
        
        int4=(-1)*int4
        int5=(-1)*int5
        mat2=np.array([int4,int5])
        if(np.linalg.det(mat1)!=0):
            mat1=np.linalg.inv(mat1)
        else:
            mat1=np.identity(2)
        
        u1=np.dot(mat1,mat2)
        u[i][j]=u1[0]
        v[i][j]=u1[1]
           
import matplotlib.pyplot as plt
x,y=np.meshgrid(np.linspace(0,719,10),np.linspace(0,1279,20))
fig, ax = plt.subplots()
ax.imshow(im)
ax.quiver(y,x,u/np.max(u),v/np.max(v),color='red',scale=10)
plt.show()
