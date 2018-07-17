# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:14:57 2018

@author: VRIPLAB8
"""
from scipy.misc import imread,toimage
from PIL import Image 
from scipy import ndimage
import numpy as np
import math

im=Image.open('a1.png')
size=im.size
im.show()
im = imread('a1.png');
toimage(im).show()
dx=ndimage.sobel(im,0)
dy=ndimage.sobel(im,1)
#toimage(dx).show()
#toimage(dy).show()

m = np.sqrt(np.square(dx) + np.square(dy))
orn = np.arctan2(dy,dx)
mag=np.zeros((size[1],size[0]))
orien=np.zeros((size[1],size[0]))

for i in range(0,size[1]-1):
    for j in range(0,size[0]-1):
        mag[i][j]= np.max(m[i][j])
        orien[i][j] = np.max(orn[i][j])

#-----------Step 2 ------------------------------------------------------
b=np.zeros((8,8))
o=np.zeros((8,8))
hist=np.zeros((128,9))
p=0
n=0
z=0
for l in range(0,63):
    k=0
    for k in range(0,127):
        
        for i in range(0,7):    
            for j in range(0,7):
                b[i][j]=mag[i+k][j+l]
                o[i][j]=orien[i+k][j+l]
                o[i][j]=o[i][j] * 180 / np.pi
                if((o[i][j]>0 and o[i][j]<10) or (o[i][j]>170 and o[i][j]<180)):
                    hist[z][0] = hist[z][0] + b[i][j]
                elif(o[i][j]>10 and o[i][j]<30):
                    hist[z][1] = hist[z][1] + b[i][j]
                elif(o[i][j]>30 and o[i][j]<50):
                    hist[z][2] = hist[z][2] + b[i][j]
                elif(o[i][j]>50 and o[i][j]<70):
                    hist[z][3] = hist[z][3] + b[i][j]
                elif(o[i][j]>70 and o[i][j]<90):
                    hist[z][4] = hist[z][4] + b[i][j]
                elif(o[i][j]>90 and o[i][j]<110):
                    hist[z][5] = hist[z][5] + b[i][j]
                elif(o[i][j]>110 and o[i][j]<130):
                    hist[z][6] = hist[z][6] + b[i][j]
                elif(o[i][j]>130 and o[i][j]<150):
                    hist[z][7] = hist[z][7] + b[i][j]
                elif(o[i][j]>150 and o[i][j]<170):
                    hist[z][8] = hist[z][8] + b[i][j]
                elif(o[i][j] == 10):
                    hist[z][0] = hist[z][0] + (b[i][j]*(20-o[i][j])/20)
                    hist[z][1] = hist[z][1] + (b[i][j]*(o[i][j]-0)/20)
                elif(o[i][j] == 30):
                    hist[z][1] = hist[z][1] + (b[i][j]*(40-o[i][j])/20)
                    hist[z][2] = hist[z][2] + (b[i][j]*(o[i][j]-20)/20)
                elif(o[i][j] == 50):
                    hist[z][2] = hist[z][2] + (b[i][j]*(60-o[i][j])/20)
                    hist[z][3] = hist[z][3] + (b[i][j]*(o[i][j]-40)/20)
                elif(o[i][j] == 70):
                    hist[z][3] = hist[z][3] + (b[i][j]*(80-o[i][j])/20)
                    hist[z][4] = hist[z][4] + (b[i][j]*(o[i][j]-60)/20)
                elif(o[i][j] == 90):
                    hist[z][4] = hist[z][4] + (b[i][j]*(100-o[i][j])/20)
                    hist[z][5] = hist[z][5] + (b[i][j]*(o[i][j]-80)/20)
                elif(o[i][j] == 110):
                    hist[z][5] = hist[z][5] + (b[i][j]*(120-o[i][j])/20)
                    hist[z][6] = hist[z][6] + (b[i][j]*(o[i][j]-100)/20)
                elif(o[i][j] == 130):
                    hist[z][6] = hist[z][6] + (b[i][j]*(140-o[i][j])/20)
                    hist[z][7] = hist[z][7] + (b[i][j]*(o[i][j]-120)/20)
                elif(o[i][j] == 150):
                    hist[z][7] = hist[z][7] + (b[i][j]*(160-o[i][j])/20)
                    hist[z][8] = hist[z][8] + (b[i][j]*(o[i][j]-140)/20)
                elif(o[i][j] == 170):
                    hist[z][8] = hist[z][8] + (b[i][j]*(0-o[i][j])/20)
                    hist[z][0] = hist[z][0] + (b[i][j]*(o[i][j]-160)/20)
    k=k+8
    z=z+1
        #p=p+1
l=l+8
    #n=n+1
#--------------------Step 3------------------------------------------
j=0
a=np.zeros((105,36))
while(j<105):
    h1=np.ndarray.tolist(hist[j])
    h2=np.ndarray.tolist(hist[j+1])
    h3=np.ndarray.tolist(hist[j+8])
    h4=np.ndarray.tolist(hist[j+9])
    x=0
    x=np.concatenate((h1,h2),0)
    x=np.append(x,h3)
    x=np.append(x,h4)
    x_norm =np.linalg.norm(x)
    if(x_norm>0):
        a[j]=x/x_norm
    else:
         a[j]=x    
    j=j+1
feature_giant = np.reshape(a,(105*36 , 1))  
           
               
#----------------------Step 4 -Visualization-------------------------------
import numpy as np
import matplotlib.pyplot as plt
p=plt.subplot(111,projection='polar')
r=hist[0]/(np.linalg.norm(hist[0]))
theta=np.array([0,20,40,60,80,100,120,140,160])
theta=theta*(np.pi)/180
p.stem(theta,r)
p.axis('off')
p.savefig('h0.png')
#------------------------------------------------------------------
v=np.zeros((8,8))
q=hist[0]/np.linalg.norm(hist[0])
theta=np.array([0,20,40,60,80,100,120,140,160])
theta=theta*(np.pi)/180
q_c=q*np.cos(theta)
q_s=q*np.sin(theta)
for n in range(0,8):
    q1=np.int(q_c[n])
    q2=np.int(q_s[n])
    i=0
    j=0
    while(i<=q1 and j<=q2):
        v[3+i][3+j] = 255
        i=i+1
        j=j+1
toimage(v).show()
#--------------------------------------------------------------------------
#import plotly.plotly as py
#import plotly.figure_factory as ff
#x,y = np.meshgrid(np.arange(0, 64, 128), np.arange(0, 128, 8))
#fig = ff.create_quiver(x, y, hist[0],0)
#py.iplot(fig, filename='Quiver Plot Example')
im=Image.open('a1.png').convert('L')
import matplotlib.pyplot as plt
x,y=np.meshgrid(np.linspace(0,133,8),np.linspace(0,69,8))
fig, ax = plt.subplots()
ax.imshow(im)
u=[]
v=[]
for i in range(0,105):
    t1 = np.argmax(a[i])
    t2 = np.amax(a[i])
    u.append(t2*np.sin(t1*20))
    v.append(t2*np.cos(t1*20))
ax.quiver(y,x,v,u,color='red',scale=1)
plt.show()
