# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 17:45:05 2018

@author: user
"""
import scipy
from scipy import ndimage
import numpy as np
from PIL import Image as im

im1=im.open('square1.png').convert('1')
size=im1.size
im1.save('square2.png')
im1=scipy.misc.imread('square2.png')
scipy.misc.toimage(im1).show()
dx = ndimage.sobel(im1, 0)  # horizontal derivative
dy = ndimage.sobel(im1, 1)  # vertical derivative
mag = np.hypot(dx, dy)
d=dy/dx
grad = np.arctan(d)
mag *= 255.0 / np.max(mag)
scipy.misc.toimage(mag).show()

# Creating R table-----------------------------------------------
theta =np.unique(grad)
theta_len = theta.size
n=np.nan
p=0
for i in range(0,theta_len-1):
    if(np.isnan(theta[i]) == True):
        p=p+1
res_unique_length = theta_len - p
res_unique = np.zeros((res_unique_length,1))
for i in range(0,res_unique_length ):
    res_unique[i] = theta[i]#------list of theta values present in the gradient image-------
xr = np.int(size[1]/2)
yr = np.int(size[0]/2)
#R=np.zeros((res_unique_length,50))
R=np.zeros((res_unique_length,261,2))
count = np.zeros((res_unique_length,1))

for x in range(0,size[1]-1):
    for y in range(0,size[0]-1):
        if(mag[x][y] >200):
            r=np.sqrt((x-xr)^2 + (y-yr)^2)
            s=(y-yr)/(x-xr)
            alpha = np.arctan(s)
            for i in range(0,res_unique_length):
                if(grad[x][y]==res_unique[i]):
                     R[i][np.int(count[i])] = np.array([s,alpha])
                     count[i]=count[i] + 1
#########Created R table#################################################
i=im.open('square2.png')
size=i.size
test_image = scipy.misc.imread('square2.png')
dx = ndimage.sobel(test_image, 0)  # horizontal derivative
dy = ndimage.sobel(test_image, 1)  # vertical derivative
mag = np.hypot(dx, dy)
d=dy/dx
grad = np.arctan(d)
mag *= 255.0 / np.max(mag)
scipy.misc.toimage(mag).show()
A=np.zeros((size[1],size[0]))
r=np.zeros((2))
for x in range(0,size[1]-1):
    for y in range(0,size[0]-1):
       
        for i in range(0,res_unique_length):
            if(grad[x][y] == res_unique[i]):
                for j in range(0,np.int(count[i])-1):
                    r=R[i][np.int(count[i])]
                    rc = r[0]*np.cos(r[1])
                    rs = r[0]*np.sin(r[1])
                    xc = np.int(x + rc)
                    #print(xc)
                    yc = np.int(y + rs)
                    #print(yc)
                    A[xc][yc] = A[xc][yc] + 1
B=np.zeros((100,100))
for a in range(0,99):
    for b in range(0,99):
        B[a][b] = A[a+300][b+300]
        #print(A[a][b])
        
i,j= np.unravel_index(B.argmax(), B.shape)
image=im.open('square2.png')
import matplotlib.pyplot as plt
fig,ax=plt.subplots()
ax.imshow(image)
ax.plot([i+300],[j+300],'o',color='red')
plt.show()        
                
                    
