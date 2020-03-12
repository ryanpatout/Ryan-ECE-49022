# Ryan Patout
# ECE 49022
# Senior Design Team 11
# Load Cell Data

def main():
    dataSet = {}
    filenames = ['percentiles']
    for file in filenames:
        data = getData(file)
        data = [float(d) for d in data]
        dataSet[file] = data
    print(dataSet)

def getData(file):
    myFile = open(file + ".txt", 'r')
    data = myFile.readlines()
    myFile.close()
    return data

main()