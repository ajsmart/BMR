import os
import matplotlib.pyplot as p
import numpy as np
import pandas as pd
from filterMedian import medfilt

#returns all of the filenames in /data/Scale
def getScaleFiles():
    #get list of filenames
    mypath = ".\data\Scale"
    files = []
    for (dirpath, dirnames, filenames) in os.walk(mypath):
        files.extend(filenames)
        break
    return files

if __name__ == '__main__':
    #start by getting the list of all of the files in /data/Scale
    files = getScaleFiles()
    #get array of arrays of data
    tDat = []
    wDat = []
    for f in files:
        tmp = pd.read_csv('data/Scale/'+f)
        tDat.append(tmp['TIME'].values.tolist())
        wDat.append(tmp['WEIGHT'].values.tolist())
   
       #filter data
    fDat = []
    for w in wDat:
        fDat.append(medfilt(w))
    
    #find maximum values in data
    maxvals = []
    for f in fDat:
        max = 0
        for x in range(0,10000):
            if f[x] > max and f[x] < 1:
                max = f[x]
        maxvals.append(max)

    #normalize the weights
    nDat = []
    for x in range(0,len(fDat)):
        a = []
        for v in fDat[x]:
            a.append(v/maxvals[x])
        nDat.append(a)
    
    #average samples together
    #start by figuring out minimum data length
    minlength = len(tDat[0])
    for x in range(1,len(tDat)):
        if len(tDat[x])<minlength:
            minlength = len(tDat[x])
    #average time vector
    tAvg = []
    len_t = len(tDat)
    for x in range(0,minlength):
        avg = 0
        for i in range(0,len_t):
            avg = avg + tDat[i][x]
        tAvg.append(avg/len_t)
    #average normalized weight vector
    nAvg = []
    for x in range(0,minlength):
        avg = 0
        for i in range(0,len_t):
            avg = avg + nDat[i][x]
        nAvg.append(avg/len_t)

    #plot raw data vs time
    p.figure(1)
    for x in range(0,len(tDat)):
        p.plot(tDat[x],wDat[x])
    p.title('True Weight vs Time')
    p.ylabel('Weight (grams)')
    p.xlabel('Time (seconds)')
    #plot raw data vs time
    p.figure(2)
    for x in range(0,len(tDat)):
        p.plot(tDat[x],fDat[x])
    p.title('Filtered Weight vs Time')
    p.ylabel('Weight (grams)')
    p.xlabel('Time (seconds)')
    #plot normalized data vs time
    p.figure(3)
    for x in range(0,len(tDat)):
        p.plot(tDat[x],nDat[x])
    p.title('Normalized Weight vs Time')
    p.ylabel('Weight')
    p.xlabel('Time (seconds)')
    p.figure(4)
    p.plot(tAvg,nAvg)
    p.title('Average Normalized Weight vs Time')
    p.ylabel('Weight')
    p.xlabel('Time (seconds)')
    #lets see what happens
    p.show()


