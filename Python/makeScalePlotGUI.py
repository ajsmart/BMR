from appJar import gui
from os import walk
#import csv
#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot(fn,val):
    wdata = pd.read_csv('data/Scale/'+fn)
    timevec = wdata['TIME'].values.tolist()
    weightvec = wdata['WEIGHT'].values.tolist()
    porosityvec = wdata['POROSITY'].values.tolist()
    
    if val == 1:
        plt.figure(1)
        plt.plot(timevec,weightvec)
        plt.title('Scale Measurements')
        plt.ylabel('Weight (grams)')
        plt.xlabel('Time (seconds)')
        plt.grid('on')
        plt.show()
        return
    else:
        plt.plot(timevec,porosityvec)
        plt.title('Scale Measurements')
        plt.ylabel('Porosity')
        plt.xlabel('Time (seconds)')
        plt.grid('on')
        plt.show()
        return

def press(button):
    if button == "Exit":
        app.stop()
    elif button == "Plot Weight":
        fn = app.getOptionBox("File Name")
        plot(fn,1)
    else:
        fn = app.getOptionBox("File Name")
        plot(fn,2)


if __name__ == '__main__':
    app = gui("Selection Window","500x200")
    app.setBg("LightPink")
    app.setFont(12)

    app.addLabel("title", "Scale Data Plotter")
    app.setLabelBg("title", "Blue")
    app.setLabelFg("title", "LightPink")
    
    #get list of filenames
    mypath = ".\data\Scale"
    files = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        files.extend(filenames)
        break
    #file selection
    app.addLabelOptionBox("File Name",files) 

    app.addButtons(["Plot Porosity","Plot Weight","Exit"], press)
    app.setButtonBg("Exit","IndianRed")
    app.setButtonFg("Exit","NavajoWhite")
	
    app.go()
