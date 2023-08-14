#import sys
#sys.path.append('/anaconda3/bin')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

sheet_name = str(sys.argv[1])

sheet_id = "1BuyxFfV0C_RqYA_5UKN6eLL2XMXL2SHtLsfW-oIPg88"
sheet_url = "https://docs.google.com/spreadsheets/d/"  + sheet_id + "/gviz/tq?tqx=out:csv&sheet=" + sheet_name

table = pd.read_csv(sheet_url)
#print(table.dtypes)
#print(table.keys())
#table["Value "] = table["Value "].astype('str')
#print(table.dtypes)
#print(table)
fp = "modParameters.dat"
originalParams = open(fp, "r").read()

lines = originalParams.splitlines()

listOfVars = table["Parameter "].values.tolist()
#print("listOfVars: ", listOfVars)

def replaceValue(line, index, newVal):
    first = line[:index]

    second = line[index+1:]

    return first + [newVal] + second

with open("modParametersNEW.dat", "w") as f:
    for line in lines:
        line = line.split(" ")
        #print("split line: ", line)
        varName = line[0]
        #print("varName: ", varName)
        if varName in listOfVars:
            #index = listOfVars.index(varName)
            row = table.loc[table["Parameter "] == varName]
            newVal = row["Value "].tolist()
            #print("newValList: ", newVal)
            newVal = newVal[0]
            #print("new value: ", newVal)
            if 'nphot' in varName:
                newVal = int(newVal)
            newVal = str(newVal)
            valIndex = 1
            line = replaceValue(line, valIndex, newVal)

        outputLine = ""
        for item in line:
            outputLine += str(item) + " "
        f.write(outputLine + '\n' )
    f.close()
