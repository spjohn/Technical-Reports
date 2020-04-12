# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 08:13:31 2018

@author: user
"""
import scipy
from scipy import ndimage
import numpy as np
from PIL import Image as im
im1=im.open('circle.gif').convert('1')
size=im1.size
im1.save('circle1.png')
im1=scipy.misc.imread('circle1.png')
scipy.misc.toimage(im1).show()
dx = ndimage.sobel(im1, 0)  # horizontal derivative
dy = ndimage.sobel(im1, 1)  # vertical derivative
mag = np.hypot(dx, dy)
d=dy/dx
grad = np.arctan(d)
mag *= 255.0 / np.max(mag)
scipy.misc.toimage(mag).show()

rmax=np.int(0.5*np.sqrt(size[0]^2 + size[1]^2))
rmin=1
r=np.array([range(rmin,rmax)])
sr=r.size
A=np.zeros((size[1],size[0],sr+1))
for r in range(rmin,rmax):
    for i in range(0,size[1]-1):
        for j in range(0,size[0]-1):
            if(mag[i][j]>180):
                phi = grad[i][j]
                a=np.int(i - r*np.sin(phi))
                b=np.int(j - r*np.cos(phi))
                A[a][b][r] = A[a][b][r] + 1
B=np.zeros((100,100,sr+1))
for a in range(0,99):
    for b in range(0,99):
        for r in range(rmin,rmax):
            B[a][b][r] = A[a+240][b+310][r]
        
#m =np.argmax(A)
i,j,k= np.unravel_index(B.argmax(), A.shape)

#p=0
#for a in range(0,size[1]-1):
#        for b in range(0,size[0]-1):
#            for r in range(rmin,rmax):
#                if(A[a][b][r] == m):
#                    out = np.array([a,b,r])
#                    print(out)
#                    p=p+1
import matplotlib.pyplot as plt
fig,ax=plt.subplots()
ax.imshow(im1)
for l in range(0,1):
    ax.plot([i+240],[j+310],'o',color='red')
plt.show()        

            