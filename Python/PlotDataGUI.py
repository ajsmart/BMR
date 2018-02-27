from appJar import gui
from os import walk
import csv
#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot(fn):
    mdata = pd.read_csv('data/Laser/'+fn)
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
    plt.show()
    return

def press(button):
    if button == "Exit":
        app.stop()
    elif button == "Plot":
        fn = app.getOptionBox("File Name")
        plot(fn)
    else:
        a = 0

if __name__ == '__main__':
    app = gui("Selection Window","500x200")
    app.setBg("green")
    app.setFont(12)

    app.addLabel("title", "Welcome to the selector!")
    app.setLabelBg("title", "Blue")
    app.setLabelFg("title", "green")
    
    #get list of filenames
    mypath = ".\data\Laser"
    files = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        files.extend(filenames)
        break
    #file selection
    app.addLabelOptionBox("File Name",files) 

    app.addButtons(["Plot","Exit"], press)
    app.setButtonBg("Plot","white")
    app.setButtonFg("Plot","Navy")
    app.setButtonBg("Exit","Black")
    app.setButtonFg("Exit","green")
	
    app.go()
