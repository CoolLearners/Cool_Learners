# -*- Sustainability project -*-
"""
Created on Tue Jan  9 20:30:55 2018
@author: Aditya Linngam, Rishik Reddy
"""
import numpy as np
import matplotlib.pyplot as mplp
import pandas as pd
dataset1 = pd.read_csv("Global Climate Change.csv")
#dataset2 = pd.read_csv("Global Climate Change.csv")
#dataset3 = pd.read_csv("Global Climate Change.csv")
xArray1 = []
xArray2 = []
xArray3 = []
count = 1
graphs= 1
columnumbers = "d1y1"
power1 = 2
power2 = 2
power3 = 2
length = len(dataset1.loc[:,'dt'])
while(count != 3):
    start = 1
    Array = []
    print("the length of the dataset is equal to ", length)
    while(start != length + 1):
        xArray1 += [start]
        start = start +1
    if(count == 1): 
        xArray1 = Array
        #length = len(dataset2.loc[:,'dt'])
    elif(count == 2):
        xArray2 = Array
    else:
        xArray3 = Array
        #length = len(dataset3.loc[:,'dt'])
    print(xArray1)
    count += 1
d1y1 = dataset1.loc[:,'LandAverageTemperature']
d1y2 = dataset1.loc[:,'LandMaxTemperature']
d1y3 = dataset1.loc[:,'LandMinTemperature']
d1y4 = dataset1.loc[:,'LandAndOceanAverageTemperature']
#d2y1 = dataset1.loc[:,'LandAverageTemperature']
#d2y2 = dataset1.loc[:,'LandMaxTemperature']
#d2y3 = dataset1.loc[:,'LandMinTemperature']
#d2y4 = dataset1.loc[:,'LandAndOceanAverageTemperature']
#d3y1 = dataset1.loc[:,'LandAverageTemperature']
#d3y2 = dataset1.loc[:,'LandMaxTemperature']
#d3y3 = dataset1.loc[:,'LandMinTemperature']
#d3y4 = dataset1.loc[:,'LandAndOceanAverageTemperature']
slope_d1y1 = np.polyfit(xArray1,d1y1,power1)
slope_d1y2 = np.polyfit(xArray1,d1y2,power1)
slope_d1y3 = np.polyfit(xArray1,d1y3,power1)
slope_d1y4 = np.polyfit(xArray1,d1y4,power1)
#slope_d2y1 = np.polyfit(xArray2,d2y1,power2)
#slope_d2y2 = np.polyfit(xArray2,d2y2,power2)
#slope_d2y3 = np.polyfit(xArray2,d2y3,power2)
#slope_d2y4 = np.polyfit(xArray2,d2y4,power2)
#slope_d3y1 = np.polyfit(xArray3,d3y1,power3)
#slope_d3y2 = np.polyfit(xArray3,d3y2,power3)
#slope_d3y3 = np.polyfit(xArray3,d3y3,power3)
#slope_d3y4 = np.polyfit(xArray3,d3y4,power3)
print(slope_d1y1)
print(slope_d1y2)
print(slope_d1y3)
print(slope_d1y4)
numX = 0
columns = []
count = 1
arrayName = xArray1
plotX = []
a = 1
while(count != graphs + 1):
    while(columnumbers != "end"):
        print("what are the colum numbers for graph ", count)
        columnumbers = str(input())
        if(columnumbers=="1"or columnumbers=="2"or columnumbers=="3"or columnumbers=="4"):
            if(columnumbers == "1"):
                columns += d1y1          
            elif(columnumbers == "2"):
                columns += d1y2
            elif(columnumbers == "3"):
                columns += d1y3
            elif(columnumbers == "4"):
               columns += d1y4
            arrayName = xArray1
        #if(columnumbers=="5"or columnumbers=="6"or columnumbers=="7"or columnumbers=="8"):
            #elif(columnumbers == "5"):
                #columns = d2y1
            #elif(columnumbers == "6"):
                #columns = d2y2
            #elif(columnumbers == "7"):
                #columns = d2y3
            #elif(columnumbers == "8"):
                #columns = d2y4
            #arrayName = xArray2
        #if(columnumbers=="9"or columnumbers=="10"or columnumbers=="11"or columnumbers=="12"):
            #elif(columnumbers == "9"):
                #columns = d3y1
            #elif(columnumbers == "10"):
                #columns = d3y2
            #elif(columnumbers == "11"):
                #columns = d3y3
            #elif(columnumbers == "12"):
                #columns = d3y4
            #arrayName = xArray3
        else:
            print("eror")
            count -= 1
            numX -= 1
        numX += 1
    while(a != numX):
        plotX += arrayName
        a += 1
    mplp.plot(plotX, columns,"o")
    count += 1
