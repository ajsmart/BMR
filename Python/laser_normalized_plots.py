import os
import matplotlib.pyplot as p
import numpy as np
import pandas as pd

#returns all of the filenames in /data/Scale
def getScaleFiles():
    #get list of filenames
    mypath = ".\data\Laser"
    files = []
    for (dirpath, dirnames, filenames) in os.walk(mypath):
        files.extend(filenames)
        break
    return files

if __name__ == '__main__':
    #start by getting the list of all of the files in /data/Scale
    files = getScaleFiles()
    #get array of arrays of data
    rDat = []
    for f in files:
        mdata = pd.read_csv('data/Laser/'+f)
        tmp = mdata['-999.999'].values.tolist()
        #determine start time...
        started = False #we have not started the data recording yet
        mvec = []
        for x in tmp:
            if x <-10 and started == False:
                continue
            elif x > -10 and started == False:
                started = True
            if started == True:
                mvec.append(x)
        rDat.append(mvec)
    datlen = len(rDat)

    #normalize data
    maxvals = []
    for r in rDat:
        maxvals.append(np.max(r))

    nDat = []
    for x in range(0,datlen):
        a = []
        for v in rDat[x]:
            a.append(v/maxvals[x])
        nDat.append(a)
    
    #average data -- not sure how to handle this one...
    
    #plot raw laser data
    p.figure(1)
    for r in rDat:
        p.plot(r)
    p.title('Raw laser Data')
    p.ylabel('Distance from laser (mm)')
    p.xlabel('Number of samples')

    #plot normalized laser data
    p.figure(2)
    for n in nDat:
        p.plot(n)
    p.title('Normalized laser Data')
    p.ylabel('Normalized Distance from laser (mm)')
    p.xlabel('Number of samples')

    p.show()