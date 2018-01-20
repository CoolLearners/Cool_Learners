# -*- Sustainability project -*-
"""
Created on Tue Jan  9 20:30:55 2018
@author: Aditya Linngam, Rishik Reddy
"""
import numpy as np
import matplotlib.pyplot as mplp
import pandas as pd

#datasetReader = []
count = 1
while(count != 5):
    print("data ",count, "/n")
    print("name of dataset including the suffix (example: MyDataset.csv)")
    datasetReader = pd.read_csv(input())
    print("name of column to read (example: AverageTempratures)")
    if(count == 1):
        data1 = datasetReader.loc[:,input()]
    if(count == 2):
        data1 = datasetReader.loc[:,input()]
    if(count == 3):
        data1 = datasetReader.loc[:,input()]
    if(count == 4):
        data4 = datasetReader.loc[:,input()]    
    count += 1

xArray1 = []
xArray2 = []
xArray3 = []
xArray4 = []
count = 1
columnumbers = "d1y1" #not numbers names
power1 = 2
length = len(data1)
while(count != 4):
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
slope_d1y1 = np.polyfit(xArray1,d1y1,power1)
slope_d1y2 = np.polyfit(xArray1,d1y2,power1)
slope_d1y3 = np.polyfit(xArray1,d1y3,power1)
slope_d1y4 = np.polyfit(xArray1,d1y4,power1)
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
    else:
        print("eror")
        count -= 1
        numX -= 1
    numX += 1
while(a != numX):
    plotX += arrayName
    a += 1
mplp.plot(plotX, columns,"o")

