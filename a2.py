# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:54:48 2018

@author: VRIPLAB4
"""
from PIL import Image
import numpy as np
from skimage.transform import AffineTransform
from numpy.linalg import inv
from scipy.misc import toimage

p1=np.array([646,263])
p2=np.array([411,251])
p3=np.array([526,195])

P1=np.array([418,321])
P2=np.array([188,304])
P3=np.array([307,252])

T=np.array([[p1[0],p1[1],1,0,0,0],
            [0,0,0,p1[0],p1[1],1],
            [p2[0],p2[1],1,0,0,0],
            [0,0,0,p2[0],p2[1],1],
            [p3[0],p3[1],1,0,0,0],
            [0,0,0,p3[0],p3[1],1]])
p=np.array([P1[0],P1[1],P2[0],P2[1],P3[0],P3[1]])

Tinv=inv(T)
res=np.dot(Tinv,p)

rmat=np.reshape(res,(2,3))

im=Image.open('Image1.jpg')
size=im.size

newmat=np.zeros((size[0],size[1],3))

for i in range(0,size[0]-1):
    for j in range(0,size[1]-1):
        a=im.getpixel((i,j))
        hc=np.array([i,j,1])
        newhc=np.dot(rmat,hc)
        if(newhc[0]>0 and newhc[1]<size[1]-1 and newhc[1]>0 and newhc[0]<size[0]-1):
            newmat[newhc[0],newhc[1]]=a

#toimage(np.transpose(newmat)).show()
toimage(np.transpose(newmat)).save('affine.png')
        



