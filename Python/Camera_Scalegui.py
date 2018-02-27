from appJar import gui
from readScale import getdata
from readScale import close
from readScale import take_measurements
import multiprocessing
import time
import matplotlib.pyplot as plt
import csv
import cv2
import numpy as np
import os
from PIL import Image

def getscale():
    while True:
        try:
            x=float(getdata())
            return x
        except TypeError:
            pass

def gatherdata(button):
    app.removeButton("Start")
    global newpath
    #set communication between processes and input variable data
    parent_conn, child_conn = multiprocessing.Pipe()
    
    timelimit =3600*app.getEntry("Time_Limit")
    s_s=app.getEntry("S/S")
    tmp = app.getLabel("total_w")
    twstr = ""
    for x in tmp:
        if x == " ":
             break
        else:
            twstr = twstr + x
    tot_w = float(twstr)
    
    #multithread the timer and the scale weight
    
    #declare result vectors
    numvec = []
    numvec2 = []
    t = []
    img=[]
    app.addLabel("output","")
    #collect data while time counts down.
#    p1 = multiprocessing.Process(target=close, args=(timelimit,)) #timer
#    p2 = multiprocessing.Process(target=take_measurements, args=#(child_conn,)) #data acquisition
#    p1.start() #start timer
#    p2.start()
    cap=cv2.VideoCapture(0)
    a=0
    count=0
    while a<timelimit:
        other,camcap=cap.read()
        cv2.imwrite(newpath+"/"+str(count)+".png",camcap)
        dat=getscale()
        numvec.append(dat - tot_w)
        a = time.clock()
        t.append(a)
        count+=1
        time.sleep(s_s-.5)
        #porosity estimate
        numvec2.append(float(((dat - tot_w)/.7893)/(3.141592*1*.06)))
   
    #time's up, terminate all processes
    cap.release()
#    p2.terminate()
    app.addLabel("finscale","Scale is Finished",colspan=2)

    #save the data
    name = app.getEntry("File Name:")
    with open('data/Scale/'+name+'.csv', 'wb') as output:
        writer = csv.writer(output,delimiter=',')
        writer.writerow(["TIME","WEIGHT","POROSITY"])
        for x in range(0,len(t)):
            writer.writerow([str(t[x]), str(numvec[x]), str(numvec2[x])])
    
    #print success message
    app.addLabel("success","SUCCESS!",colspan=2)


def getsample(button):
    app.removeButton("Weigh")
    app.removeLabel("zero_w")
    tmp = float(getdata()) #"12.3752"
    app.addLabel("total_w",str(tmp)+" grams",colspan=2)
    #print "getting sample"
    r=app.getRow()
    app.addLabel("prompt1","Time limit (hours):",r,0)
    app.addNumericEntry("Time_Limit",r,1)
    r1=app.getRow()
    app.addLabel("prompt2","1 Sample every __ seconds:",r1,0)
    app.addNumericEntry("S/S",r1,1)
    app.addLabel("msg1","Press 'Start' when you are ready to collect data.",colspan=2)
    app.addButton("Start", gatherdata,colspan=2)
#####################################################
def start_program():
    row = app.getRow()
    app.addButton("Weigh",getsample,row,0)
    app.addLabel("zero_w","0.0000 grams",row,1)
#####################################################
def press(button):
    global newpath

    if button == "Exit":
        app.stop()
    else:
        val = app.getEntry("File Name:")
        #the commented out code was an experiment that worked.  I'm leaving it here for future reference
        #app.setLabe("message","You just started recording")
        if val =="":
            app.setLabel("message","Error: No filename Designated")
            app.setLabelBg("message","red")
            app.setLabelFg("message","green")
        elif button =="Start Measurements":
            cap = cv2.VideoCapture(0)
            while(True):
                ret, frame = cap.read()
                # Our operations on the frame come here
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # Display the resulting frame
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            # When everything done, release the capture
            cap.release()
            cv2.destroyAllWindows()
            newpath=r"data/photo/"+val
            os.makedirs(newpath)
            app.setLabel("message","Put collector on scale and click \"weigh\" when you have a constant value.")
            app.setLabelBg("message","Green")
            app.setLabelFg("message","Black")
            app.removeButton("Start Measurements")
            start_program()
#####################################################
if __name__ == '__main__':
    #initiate app
    app = gui("Scale Window","500x200")
    app.setBg("PeachPuff")
    app.setFont(12)

    #title panel
    app.addLabel("title","Scale and Camera Reading System", colspan=2)
    app.setLabelBg("title","Maroon")
    app.setLabelFg("title","PeachPuff")

    #Filename input
    row = app.getRow()
    app.addLabelEntry("File Name:",row,0)
    app.addLabel(".csv",".csv",row,1)

    #declare buttons
    app.addButtons(["Start Measurements","Exit"],press, colspan=2)

    #message area
    app.addLabel("message","", colspan=2)
    #app.setLabelFg("message","Red")

    app.go()
