# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:56:49 2018

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
p4=np.array([650,195])

P1=np.array([418,321])
P2=np.array([188,304])
P3=np.array([307,252])
P4=np.array([421,258])

T=np.array([[p1[0],p1[1],1,0,0,0,-(p1[0]*P1[0]),-(p1[1]*P1[0])],
            [p2[0],p2[1],1,0,0,0,-(p2[0]*P2[0]),-(p2[1]*P2[0])],
            [p3[0],p3[1],1,0,0,0,-(p3[0]*P3[0]),-(p3[1]*P3[0])],
            [p4[0],p4[1],1,0,0,0,-(p4[0]*P4[0]),-(p4[1]*P4[0])],
            [0,0,0,p1[0],p1[1],1,-(p1[0]*P1[1]),-(p1[1]*P1[1])],
            [0,0,0,p2[0],p2[1],1,-(p2[0]*P2[1]),-(p2[1]*P2[1])],
            [0,0,0,p3[0],p3[1],1,-(p3[0]*P3[1]),-(p3[1]*P3[1])],
            [0,0,0,p4[0],p4[1],1,-(p4[0]*P4[1]),-(p4[1]*P4[1])]])
p=np.array([P1[0],P2[0],P3[0],P4[0],P1[1],P2[1],P3[1],P4[1]])

D=np.dot(np.transpose(T),T)
Dinv=inv(D)
D1=np.dot(np.transpose(T),p)
res=np.dot(Dinv,D1)

hom_mat=np.array([[res[0],res[1],res[2]],
                  [res[3],res[4],res[5]],
                  [res[6],res[7],1]])

im=Image.open('Image1.jpg')
size=im.size

newmat=np.zeros((size[0],size[1],3))

for i in range(0,size[0]-1):
    for j in range(0,size[1]-1):
        a=im.getpixel((i,j))
        hc=np.array([i,j,1])
        newhc=np.dot(hom_mat,hc)
        x=newhc[0]/newhc[2]
        y=newhc[1]/newhc[2]
        print(x)
        print(y)
        if(x>0 and x<size[0]-1 and y>0 and y<size[1]-1):
            newmat[x,y]=a
toimage(np.transpose(newmat)).save('homographym.png')    
        

