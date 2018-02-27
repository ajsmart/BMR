import csv
#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    #Get the Data from the scale reading program
    wdata = pd.read_csv('data/10.26.m2.csv')
    timevec = wdata['TIME'].values.tolist()
    weightvec = wdata['WEIGHT'].values.tolist()
    porosityvec = wdata['POROSITY'].values.tolist()

    #Get the data from the laser
    #mdata = pd.read_csv('alcolhol.csv')
	
	####################################################
	####################################################
	####################################################
    mdata = pd.read_csv('data/11-27-2017-001 -LiCoO.csv') #CHANGE THIS LINE!
	####################################################
	####################################################
	####################################################

    #tmp = mdata['0.089'].values.tolist()
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
    plt.figure(1)
    plt.plot(mvec)
    plt.title('Laser Measurements')
    plt.ylabel('Distance from laser (mm)')
    plt.xlabel('Number of samples')
    plt.grid('on')
    #plt.figure(2)
    #plt.plot(timevec,porosityvec,'r-')
    #plt.grid('on')
    #plt.title('Porosity Measurements')
    #plt.ylabel('Porosity')
    #plt.xlabel('Time (seconds)')
    #plt.figure(3)
    #plt.plot(tmp)
    plt.show()
    #Determine aproximate time when the laser measurement has leveled off

    #grab that approximate time and print the weight and porosity associated with that time.

    #print(wdata)
