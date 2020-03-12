# Ryan Patout
# ECE 49022
# Senior Design Team 11
# Load Cell Data

import math

def main():
    dataSet = {}                            # setting an empty dictionary
    filenames = ['percentiles']             # referencing the data filenames
    for file in filenames:                  # loop to get data
        data = getData(file)
        dataSet[file] = data
    print(dataSet)
    

def getData(file):
    myFile = open(file + ".txt", 'r')       # open in read mode
    data = myFile.readlines()               # read lines into list
    myFile.close()                          # close file
    data = [float(d) for d in data]         # convert data to float
    data = [(v/3*4096) for v in data]       # convert to ADC values
    data = [round(x, 3) for x in data]      # set precision of floats
    return data


main()
