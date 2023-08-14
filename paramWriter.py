"""
Writes a new parameters file from a default file (modParameters.dat) and parameters given in a Google sheet.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

sheet_name = str(sys.argv[1])

sheet_id = "1BuyxFfV0C_RqYA_5UKN6eLL2XMXL2SHtLsfW-oIPg88"
sheet_url = "https://docs.google.com/spreadsheets/d/"  + sheet_id + "/gviz/tq?tqx=out:csv&sheet=" + sheet_name

table = pd.read_csv(sheet_url)

fp = "modParameters.dat"
originalParams = open(fp, "r").read()

lines = originalParams.splitlines()

listOfVars = table["Parameter "].values.tolist()

def replaceValue(line, index, newVal):
    first = line[:index]
    second = line[index+1:]
    return first + [newVal] + second

with open("modParametersNEW.dat", "w") as f:
    for line in lines:
        line = line.split(" ")
        varName = line[0]
        if varName in listOfVars:
            row = table.loc[table["Parameter "] == varName]
            newVal = row["Value "].tolist()
            newVal = newVal[0]
            if 'nphot' in varName: # defaults to float but nphot, nphotimage, etc. need ints
                newVal = int(newVal)
            newVal = str(newVal)
            valIndex = 1
            line = replaceValue(line, valIndex, newVal)
        outputLine = ""
        for item in line:
            outputLine += str(item) + " "
        f.write(outputLine + '\n' )
    f.close()
