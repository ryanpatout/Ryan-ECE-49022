# Ryan Patout
# ECE 49022
# Senior Design Team 11
# Load Cell Data

import numpy as np

def main():
    dataSet=[]
    percentages = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    perc = [float(d) for d in percentages]
    filenames = ['bag1_test1', 'bag1_test2']                    # referencing the data filenames
    for file in filenames:                                      # loop to get data
        data = getData(file)                                    # returns data in list form
        dataSet.append(data)
    test1, test2 = dataSet
    test1 = test1[::-1]
    test2 = test2[::-1]
    a = 0.0274                                                  # coefficient of line of best fit
    b = 0.2924                                                  # coefficient of line of best fit
    predVout = predictedVal(perc, a, b)
    actVout = average(test1, test2)
    MSE = meanSquared(predVout, actVout)
    print('MSE:', MSE)

def getData(file):
    myFile = open(file + ".txt", 'r')                           # open in read mode
    data = myFile.readlines()                                   # read lines into list
    myFile.close()                                              # close file
    data = [float(d) for d in data]                             # convert data to float
    data = [(v/3*4096) for v in data]                           # convert to ADC values
    data = [round(x, 3) for x in data]                          # set precision of floats
    return data


def predictedVal(perc, a, b):
    Vout = []
    for x in perc:
        temp = a * x + b
        Vout.append(temp)
    Vout = [(v / 3 * 4096) for v in Vout]  # convert to ADC values
    Vout = [round(x, 3) for x in Vout]  # set precision of floats
    return Vout


def average(test1, test2):
    avg = []
    index = 0
    while index <= 20:
        temp = (test1[index]+test2[index])/2
        avg.append(temp)
        index += 1
        with open('predicted.txt', 'a') as file:                    # writing to a new file to store average values
            file.write(str(temp)+'\n')
    return avg


def meanSquared(pred, act):
    index = 0
    MSE = 0
    while index <= 20:
        squared = (act[index]-pred[index])**2
        MSE += squared
        index += 1
    MSE /= len(act)
    return MSE


main()
