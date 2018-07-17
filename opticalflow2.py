# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 16:53:40 2018

@author: Student
"""
from scipy.ndimage import sobel
from scipy.misc import toimage,imread
im1=imread('OF11.png')
im2=imread('OF22.png')
from PIL import Image 
im=Image.open('OF1.png').convert('L')
#im.show()
im.save('OF11.png')
size=im.size
conv_mat1=np.array([[-0.25,0.25],[-0.25,0.25]])
conv_mat2=np.array([[-0.25,-0.25],[0.25,0.25]])
conv_mat3=np.array([[0.25,0.25],[0.25,0.25]])
conv_mat4=np.array([[-0.25,-0.25],[-0.25,-0.25]])

from scipy.signal import convolve2d as cc
conv10=cc(im1,conv_mat1,mode='same')
conv20=cc(im1,conv_mat2,mode='same')
conv30=cc(im1,conv_mat3,mode='same')

conv11=cc(im2,conv_mat1,mode='same')
conv21=cc(im2,conv_mat2,mode='same')
conv41=cc(im2,conv_mat4,mode='same')

Ix=conv10+conv11
Iy=conv20+conv21
It=conv30+conv41

kernel=np.array([[1/12 ,1/6,1/12],[1/6,0,1/6],[1/12,1/6,1/12]])

v=np.zeros((size[1],size[0]))
u=np.zeros((size[1],size[0]))

for i in range(0,100):
    uavg=cc(u,kernel,mode='same')
    vavg=cc(v,kernel,mode='same')
    
    z1=np.multiply(Ix,u) + np.multiply(Iy,v) + It
    z2=1 + np.square(Ix) +np.square(Iy)
    z3=np.multiply(Ix,z1)
    z4=np.multiply(Iy,z1)
    u=uavg-(z3/z2)
    v=vavg-(z4/z2)
import matplotlib.pyplot as plt
x,y=np.meshgrid(np.linspace(0,719,5),np.linspace(0,1279,10))
fig, ax = plt.subplots()
ax.imshow(im)
#plt.hold
ax.quiver(y,x,u/np.max(u),v/np.max(v),color='red',scale=10)
plt.show()
    