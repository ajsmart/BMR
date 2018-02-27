import numpy as np
from readScale import getdata
from readScale import close
from readScale import take_measurements
import csv
import sys
import pandas as pd

wp_Active=.92
wp_Carbon=.04
wp_PVDF=.04
p_Active=4.9  #g/cm3
p_Carbon=1.9  #g/cm3
p_PVDF=1.78   #g/cm3
p_NMP=1.03    #g/cm3

def porosity(w1,w2,w3,d1,d2,d3):
     v_electrode=(w3-w1)*(wp_Active/p_Active+wp_Carbon/p_Carbon+wp_PVDF/p_PVDF)
     v_nmp=(w2-w3)/p_NMP
     v_procent=(d3-d1)/(d2-d1)
     return ((v_electrode+v_nmp)*(v_procent)-v_electrode)/((v_electrode+v_nmp)*v_procent)

### record samples
def get_one_sample():
     w1=float(getdata())
     d1=input("Enter distance through laser:",)
     return w1,d1

def mainthing():
     w1,w2,w3,d1,d2,d3=0,0,0,0,0,0
     name = raw_input("File name:") 
     answer=raw_input("Is data for plate and beginning already stored? y/n:")
     if answer == "n":  
          x1=raw_input("Ready to collect plate data? y/n:")
          if x1 == "y":
               a=input("weigh")
               w1,d1=get_one_sample()
          x2=raw_input("Ready to collect beginning data? y/n:")
          if x2=="y":
               a=input("weigh")
               w2,d2=get_one_sample()
          with open('data/por/'+name+'.csv', 'wb') as output:
               writer = csv.writer(output,delimiter=',')
               writer.writerow([" ","WEIGHT","DISTANCE"])
               writer.writerow(["Plate", w1, d1])
               writer.writerow(["Beginning", w2, d2])
     elif answer=="y":
          data=pd.read_csv('data/por/'+name+'.csv')
          weightvec=data['WEIGHT'].values.tolist()
          disvec=data['DISTANCE'].values.tolist()
          w1,w2=weightvec[0],weightvec[1]
          d1,d2=disvec[0],disvec[1]               

     answer2=raw_input("Is data for the end already stored? y/n:")
     if answer2=="n":
          print('')
          x3=raw_input("Ready to collect ending data? y/n:")
          if x3=="y":
               w3,d3=get_one_sample()
               with open('data/por/'+name+'.csv', 'wb') as output:
                    writer = csv.writer(output,delimiter=',')
                    writer.writerow([" ","WEIGHT","DISTANCE"])
                    writer.writerow(["Plate", w1, d1])
                    writer.writerow(["Beginning", w2, d2])
                    writer.writerow(["Ending", w3, d3])
          else:
               print "Thanks, Come back when drying is finished"
               sys.exit()

     elif answer2=="y":
          data=pd.read_csv('data/por/'+name+'.csv')
          weightvec=data['WEIGHT'].values.tolist()
          disvec=data['DISTANCE'].values.tolist()
          w3=weightvec[2]
          d3=disvec[2] 

     print "Porosity:",porosity(w1,w2,w3,d1,d2,d3)
     with open('data/por/'+name+'.csv', 'wb') as output:
          writer = csv.writer(output,delimiter=',')
          writer.writerow([" ","WEIGHT","DISTANCE"])
          writer.writerow(["Plate", w1, d1])
          writer.writerow(["Beginning", w2, d2])
          writer.writerow(["Ending", w3, d3])
          writer.writerow(["Porosity", porosity(w1,w2,w3,d1,d2,d3)])

if __name__=='__main__':
     mainthing()