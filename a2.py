# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:04:00 2018

@author: VRIPLAB4
"""
from PIL import Image as im
import numpy as np
from scipy.misc import imread,toimage
from scipy.ndimage.filters import gaussian_filter as gf
sigma=1.6
k=np.sqrt(2)
# **********************************************************
i=im.open('cam.png')
size=i.size
res0=np.zeros((5,size[0],size[1]))
p=0
while(p<5):
    g=gf(i,sigma*np.power(k,p))
    res0[p]=g
    p=p+1
toimage(res0[0]).save('b00.png')
toimage(res0[1]).save('b01.png')
toimage(res0[2]).save('b02.png')
toimage(res0[3]).save('b03.png')
toimage(res0[4]).save('b04.png')
# ***********************************************
i1=i.resize((128,128))
res1=np.zeros((5,128,128))
p=2
while(p<7):
    g=gf(i1,sigma*np.power(k,p))
    res1[p-2]=g
    p=p+1
toimage(res1[0]).save('b10.png')
toimage(res1[1]).save('b11.png')
toimage(res1[2]).save('b12.png')
toimage(res1[3]).save('b13.png')
toimage(res1[4]).save('b14.png')
# *************************************************
i2=i.resize((64,64))
res2=np.zeros((5,64,64))
p=4
while(p<9):
    g=gf(i2,sigma*np.power(k,p))
    res2[p-4]=g
    p=p+1
toimage(res2[0]).save('b20.png')
toimage(res2[1]).save('b21.png')
toimage(res2[2]).save('b22.png')
toimage(res2[3]).save('b23.png')
toimage(res2[4]).save('b24.png')
# ******************************************************
i3=i.resize((32,32))
res3=np.zeros((5,32,32))
p=6
while(p<11):
    g=gf(i3,sigma*np.power(k,p))
    res3[p-6]=g
    p=p+1
toimage(res3[0]).save('b30.png')
toimage(res3[1]).save('b31.png')
toimage(res3[2]).save('b32.png')
toimage(res3[3]).save('b33.png')
toimage(res3[4]).save('b34.png')
#------------------Step 2-----------------------------------
dog0=np.zeros((4,size[0],size[1]))
dog1=np.zeros((4,128,128))
dog2=np.zeros((4,64,64))
dog3=np.zeros((4,32,32))

for p in range(0,4):
    dog0[p] = res0[p+1] - res0[p]
    dog1[p] = res1[p+1] - res1[p]
    dog2[p] = res2[p+1] - res2[p]
    dog3[p] = res3[p+1] - res3[p]
toimage(dog0[0]).save('dog00.png')
toimage(dog0[1]).save('dog01.png')
toimage(dog0[2]).save('dog02.png')
toimage(dog0[3]).save('dog03.png')

toimage(dog1[0]).save('dog10.png')
toimage(dog1[1]).save('dog11.png')
toimage(dog1[2]).save('dog12.png')
toimage(dog1[3]).save('dog13.png')

toimage(dog2[0]).save('dog20.png')
toimage(dog2[1]).save('dog21.png')
toimage(dog2[2]).save('dog22.png')
toimage(dog2[3]).save('dog23.png')

toimage(dog3[0]).save('dog30.png')
toimage(dog3[1]).save('dog31.png')
toimage(dog3[2]).save('dog32.png')
toimage(dog3[3]).save('dog33.png')
#-----------------Step 3-------Finding keypoints-----------------------
keypoint=[]
for p in range(1,3):
    for i in range(2,size[0]-3):
        for j in range(2,size[1]-3):
            array = np.array([dog0[p][i][j],dog0[p-1][i][j],dog0[p+1][i][j],dog0[p][i-1][j],dog0[p][i+1][j],dog0[p][i][j-1],dog0[p][i][j+1],dog0[p][i-1][j-1],dog0[p][i+1][j+1],dog0[p-1][i-1][j],dog0[p-1][i+1][j],dog0[p-1][i][j-1],dog0[p-1][i][j+1],dog0[p-1][i-1][j-1],dog0[p-1][i+1][j+1],dog0[p+1][i-1][j],dog0[p+1][i+1][j],dog0[p+1][i][j-1],dog0[p+1][i][j+1],dog0[p+1][i-1][j-1],dog0[p+1][i+1][j+1],dog0[p][i-1][j+1],dog0[p][i+1][j-1],dog0[p-1][i-1][j+1],dog0[p-1][i+1][j-1],dog0[p+1][i-1][j+1],dog0[p+1][i+1][j-1]])
            key=np.argmax(array)
            if(key==0 or key==1 or key==2 ):
                x=i 
                y=j
            elif(key==3 or key==9 or key==15 ):
                x=i-1
                y=j
            elif(key==4 or key==10 or key==16 ):
                x=i+1
                y=j
            elif(key==5 or key==11 or key==17 ):
                x=i
                y=j-1
            elif(key==6 or key==12 or key==18 ):
                x=i
                y=j+1
            elif(key==7 or key==13 or key==19 ):
                x=i-1
                y=j-1
            elif(key==8 or key==14 or key==20 ):
                x=i+1
                y=j+1
            elif(key==21 or key==23 or key==25 ):
                x=i-1
                y=j+1
            elif(key==22 or key==24 or key==26 ):
                x=i+1
                y=j-1
            
#            if(np.size(keypoint)!= 0):
#                l=0
#                for k in range(0,np.size(keypoint)[0]):
#                    if(key[1]!=keypoint[k][0] and key[2]!=keypoint[k][1]):
#                        l=l+1
#            if(l==0):
    
            keypoint.append(key)
                
    
