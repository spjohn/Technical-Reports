# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 14:40:37 2018

@author: VRIPLAB4
"""
from PIL import Image as im
import numpy as np
from scipy.misc import toimage,imread

i1=im.open('cam.tif')
i1.save('cam.png')
i2=im.open('cam.png')
size=i2.size

tx=25
ty=4
t=np.array([[1,0,tx],[0,1,ty],[0,0,1]])

c=np.cos(np.pi/8)
s=np.sin(np.pi/8)
r=np.array([[c,-s,0],[s,c,0],[0,0,1]])

sx=2
sy=2

new=np.zeros((size[0],size[1]))
rotated=np.zeros((size[0],size[1]))
scale=np.zeros((sx*size[0],sy*size[1]))


for i in range(0,size[1]-1):
    for j in range(0,size[0]-1):
        hc=np.array([i,j,1])
        newhc=np.dot(t,hc)
        a=i2.getpixel((i,j))
        newr=np.dot(r,hc)
        s1=sx*i
        s2=sy*j
        
        if(newhc[0]>0 and newhc[0]<255 and newhc[1]>0 and newhc[1]<255):
            new[newhc[1],newhc[0]]=a
        if(newr[0]>0 and newr[0]<255 and newr[1]>0 and newr[1]<255):
            rotated[newr[1],newr[0]]=a   
        if(s1>0 and s1<255*sx and s2>0 and s2<255*sy):
            scale[s2,s1]=a
                 
toimage(new).show() 
toimage(new).save('Trans.png')       
toimage(rotated).show()
toimage(rotated).save('Rotated.png')
toimage(scale).show()
toimage(scale).save('Scaled.png')