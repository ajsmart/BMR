import serial
import multiprocessing
import time
import math
import matplotlib.pyplot as plt
import csv

##################################################
## Define how long the program will last.  Time limit is measured in seconds.
##################################################
def close(timelimit):
    time.sleep(timelimit)

##################################################
def take_measurements(con2):
    conn = 'COM3'
    baud = 38400
    port = serial.Serial(conn,baud)
    datstr = ''
    numval = ''
    #numvec = []
    while 1:
        x = port.read(size=1)
        if x == '\n':
            print(datstr)
            #numvec.append(float(numval))
            con2.send(float(numval))
            datstr = ''
            numval = ''
        elif x == ' ':
            x = ''
            #do nothing
        else:
            if x == 'g' or x == '\r':
                datstr = datstr + x
            else:
                numval = numval + x
                datstr = datstr + x
##################################################
def getdata():
    conn = 'COM3'
    baud = 38400
    x = ''
    numval = ''
    port = serial.Serial(conn,baud)
    loop = 1

    while loop == 1:
        x = port.read(size=1)
        if x == '\n':
            port.close()
            return numval
            print(numval)
            loop = 0
            break
        elif x == ' ':
            x = ''
        else:
            if x == 'g' or x == '\r':
                x = ''
            else:
                numval = numval + x
##################################################
if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    timelimit = 30*200

    #initial measurements
    tmp = raw_input("Press enter when you are ready to measure weight \nof current collector minus slurry.")
    w1 = float(getdata())
    #tmp = raw_input("\nPlace current collector on scale.\nPress enter when ready to take accurate measurement.")
    total_w = w1#float(getdata())
    colctr_w = w1#total_w-w1
    #print("\n\nWeight of measurement apparatus: " +str(w1)+" g")
    print("Weight of collector: "+str(colctr_w)+" g\n\n")
    tmp = raw_input("Press enter when you have applied solvent, \nand are ready to take measurements for 3 Hours and 20 Minutes.")

    #measurements over time
    p1 = multiprocessing.Process(target=close, args=(timelimit,)) #timer
    p2 = multiprocessing.Process(target=take_measurements, args=(child_conn,)) #data acquisition
    p1.start() #start timer
    p2.start() #start data collection
    #initialize weight, porosity, and time vectors
    numvec = []
    numvec2 = []
    t = []
    #collect data while time counts down.
    while p1.is_alive():
        dat = parent_conn.recv()
        numvec.append(dat - w1)
        a = time.clock()
        t.append(a)
        numvec2.append(float(((dat - total_w)/.7893)/(3.141592*1*.06)))
    #time's up, terminate all processes
    p2.terminate()
    #print(numvec)
    #print(t)
    #print(len(numvec))

    #plot weight over time
    plt.figure(1) 
    plt.plot(t,numvec)
    #plt.plot(t,numvec2,'r')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Weight')

    #plot porosity over time
    plt.figure(2) 
    plt.plot(t,numvec2,'r')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Porosity (red)')
    plt.show()

    name = raw_input('Input File Name:  ')
    with open('data/'+name+'.csv', 'wb') as output:
        writer = csv.writer(output,delimiter=',')
        writer.writerow(["TIME","WEIGHT","POROSITY"])
        for x in range(0,len(t)):
            writer.writerow([str(t[x]), str(numvec[x]), str(numvec2[x])])
    print("collector weight: " +str(colctr_w))
   
    print("\n\nMeasurement program has successfully ended.\n\n")

