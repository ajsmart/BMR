from numpy import median as med
from numpy import max, min
import pandas as pd
from pylab import plot, show, figure
#from normalized_weight_plots import getScaleFiles

def medfilt(ipt):
    med_len = 31
    output = []
    for i in range(0,len(ipt)):
        #get the values you want the median of
        tmp = []
        for x in range(i-med_len/2, i+med_len/2):
            if x < 0: #out of bounds
                if ipt[0] < 0:
                    tmp.append(.5)
                else:
                    tmp.append(ipt[0])
            elif x >= len(ipt):
                if ipt[len(ipt)-1] < 0:
                    tmp.append(.5)
                else:
                    tmp.append(ipt[len(ipt)-1])
            else:
                if ipt[x] < 0:
                    tmp.append(.5)
                else:
                    tmp.append(ipt[x])
        output.append(med(tmp))
    return output


if __name__ == "__main__":
    #-------------------------------------------------------
    #-start by reading in data and saving it as a list item-
    #-------------------------------------------------------
    files = getScaleFiles()
    #get array of arrays of data
    tDat = []
    wDat = []
    for f in files:
        tmp = pd.read_csv('data/Scale/'+f)
        tDat.append(tmp['TIME'].values.tolist())
        wDat.append(tmp['WEIGHT'].values.tolist())
    #find maximum values in data

    #filter the data
    fDat = []
    for w in wDat:
        fDat.append(medfilt(w))
    
    #plot the data
    figure()
    for f in range(0,len(fDat)):
        plot(tDat[f],fDat[f])
    
    show()
