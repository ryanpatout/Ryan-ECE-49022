# Ryan Patout
# ECE 49022
# Senior Design Team 11
# Load Cell Data

from sklearn import	linear_model
from sklearn.metrics import r2_score


def main():
    x_train = [100.0, 90.0, 80.0, 70.0, 60.0, 50.0, 40.0, 30.0, 20.0, 10.0, 0.0]
    dataSet = {}                                                # setting an empty dictionary
    filenames = ['bag2_test1']                                  # referencing the data filenames
    for file in filenames:                                      # loop to get data
        data = getData(file)                                    # returns data in list form
        dataSet[file] = data                                    # adds data with name to dictionary
    y_train = []                                                # initializing empty list for y's
    for data in dataSet.values():
        y_train.append(data)                                    # append all y values
    regression(x_train, y_train)                                # sending data to regression
    

def getData(file):
    myFile = open(file + ".txt", 'r')                           # open in read mode
    data = myFile.readlines()                                   # read lines into list
    myFile.close()                                              # close file
    data = [float(d) for d in data]                             # convert data to float
    data = [(v/3*4096) for v in data]                           # convert to ADC values
    data = [round(x, 3) for x in data]                          # set precision of floats
    return data


def regression(x_train, y_train):
    x_test = [float(i) for i in range(101)]
    regr = linear_model.LinearRegression(fit_intercept=True)        # define lin reg object
    regr.fit(x_train, y_train)                                      # fit model to training set
    coefs = regr.coef_                                              # tuple of coefficients
    print(coefs)
    intc = regr.intercept_                                          # b intercept
    print(intc)
    y_pred = regr.predict(x_test)                                   # apply model to test
    # r2 = r2_score(y_true, y_pred)


main()
