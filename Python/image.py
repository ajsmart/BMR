import numpy as np
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt

width_of_glass=1 ##mm
#####THRESHOLD, 0 is white, 255 is black#####
threshhold=150
width=25
t_aluminium=20
t_other=150

im=Image.open("data\por\sideview.png")
x,y= im.size
im = im.convert('L')

county=0

def changepix(t):
    im=Image.open("data\por\sideview.png")
    x,y= im.size
    im1 = im.convert('L')

    print t
    for i in range (x):
        for j in range (y):
            if j==0:
                im1.putpixel((i,j),0)
            if j==y-1:
                im1.putpixel((i,j),0)
            if im1.getpixel((i,j))<=t:
                im1.putpixel((i,j),0)
            elif im1.getpixel((i,j))>t:
                im1.putpixel((i,j),255)
    #im1.save("data\por\electrodebw.jpg","JPEG")
    return im1,x,y

xplot=np.arange(x)
#xstart,xend=np.arange(x)
start=np.zeros(x)
end=np.zeros(x)
def countwidth(iml,x,y,t,start=np.zeros(x),end=np.zeros(x),factor=1): 
    ###factor means go top to bottom(1) or bottom to top(-1)###   
    th=t
    iml,x,y=changepix(th)
    if factor==1:
        f=factor
        z=0
    if factor==-1:
        f=factor
        z=1
    ###### if factor=1,  z*(y-1)+f*j=j   ### top to bottom
    ###### if factor=-1, z*(y-1)+f*j=y-1-j ###  bottom to top
    i,j=0,0
    for i in range(x):
        county=0
        for j in range(y):
            if iml.getpixel((i,z*(y-1)+f*j))==0:
                county+=1
                if start[i]==0:
                    ystart=z*(y-1)+f*j
                    start[i]=ystart
            elif iml.getpixel((i,z*(y-1)+f*j))==255:
                if county<width:
                    county=0
                    start[i]=0
                if county>width:
                    if end[i]==0:    
                        end[i]=z*(y-1)+f*j
    for k in range(x):
        if start[k]==y-1:
            start[k]=0        
    start=np.ma.masked_equal(start,0)
    end=np.ma.masked_equal(end,0)
    return start,end

def findcontrast():
    for i in range x:
        for j in range y:
            if iml.getpixel((i,j))==0:
                if j>0:
                    if iml.getpixel((i,j-1))==255:
                        b_w=np.append(b_w,[(i,j)],axis=0)
            elif iml.getpixel((i,j))==255:
                if j>0:
                    if iml.getpixel((i,j-1)):
                        w_b=np.append(w_b,[(i,j)],axis=0)
    w_b1=[]
    for k in range(len(w_b)-1):
        if abs(w_b[k+1]-w_b[k])<5:
            w_b1=np.append(w_b1,w_b[k])
        else:
            


def smallersize(x,y):
    x1=x/10
    y1=y/10
    xbe=[]
    while 

def changethreshold():


#for k in range(len(start)): 
#    if start[k]==0:
#        xstart=np.delete(xstart,k)
#for l in range(len(end)):
#    if end[l]==0:
#        xend=np.delete(xend,l)
def calclength(start,end):
    #print end.mean()
    #print start.mean()
    length = end.mean()-start.mean()
    return abs(length)
def calcelectrode(sg,ea,sa,ee):
    mm*width_of_glass=calclength(sg,ea)
    ewidth=calclength(sa,ee)/mm
    return ewidth
    
#countwidth(t,width,start=np.zeros(x),end=np.zeros(x),factor=1) factor is 
###### Aluminum ######
sa,ea=countwidth(20,25)
lengthaluminum=calclength(sa,ea)
##### Electrode #####
se,ee=countwidth(150,20,start=np.zeros(x),end=np.zeros(x))
lengthelectrode=calclength(se,ee)
##### glass #####
sg,eg=countwidth(150,20,factor=-1)
lengthglass=calclength(sg,eg)
#print lengthalu


#iml.save("data\por\electrodebw.jpg","JPEG")
plt.plot(xplot,sa)
plt.plot(xplot,ea)
#plt.plot(xplot,se)
plt.plot(xplot,ee)
plt.plot(xplot,sg)
plt.show() 
print calcelectrode(sg,ea,sa,ee)