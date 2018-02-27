import numpy as np
import cv2
import time
import multiprocessing
from readScale import getdata
import os

#cap = cv2.VideoCapture(0)
#while(True):
#    # Capture frame-by-frame
#    ret, frame = cap.read()
#    #ret=cap.set(3,1280)
#    #ret=cap.set(4,960)
#    # Our operations on the frame come here
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#    # Display the resulting frame
#    cv2.imshow('frame',frame)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break

# When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()
#newpath=r'data/por/test'

#os.makedirs(newpath)
timelimit=30
#t = []
#weighvec=[]
#img=[]
#a=0
#count=0
#collect data while time counts down.
#camera=cv2.VideoCapture(0)
#while a<timelimit:
#    other,camcap= camera.read()
#    cv2.imwrite("data/por/test/"+str(count)+".png",camcap)
#    weight=float(getdata())
#    count+=1
#    a = time.clock()
#    t.append(a)
#    weighvec.append(weight)
#    time.sleep(1.7)
#    #time's up, terminate all processes
#=======
#os.makedirs(r'data/photo/testing')


##############
# Trying to display video while taking pictures
##############
a=0
count=0
acount1=0
sleeptime=10
while a<timelimit:
    cam=cv2.VideoCapture(0)
    ret,img=cam.read()
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('name',gray)
    a=time.clock()
cam.release()

#while a<timelimit:
#    #display video
#    b=0
#    while b<sleeptime:
#        camera = cv2.VideoCapture(0)
#        ret,image=camera.read()
#        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#        cv2.imshow('image',gray)
#        b+=.0001
#    cv2.destroyAllWindows()    
#    camera.release()
#    time.sleep(1)
    #camera1 = cv2.VideoCapture(0)
    #image1 = camera1.read()[1]
    #cv2.imwrite("data/photo/testing/"+str(count)+".png",image1)
    #count+=1
    #camera1.release()
#    a=time.clock()



