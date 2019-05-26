import sys
import urllib.request
import json
import csv
import Data
import os


# Function that deletes all men data from main array
def MakeArrOnlyWomen(dataArray):
    for row in reversed(dataArray):
        if "mężczyźni" in row:
            dataArray.remove(row)


# As same as above but for women
def MakeArrOnlyMen(dataArray):
    for row in reversed(dataArray):
        if "kobiety" in row:
            dataArray.remove(row)


# Function for initial data processing
def DataProcessing(args=None):
    url = "https://api.dane.gov.pl/resources/17363"
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()
    data = json.loads(r)
    fileURL = data["data"]["attributes"]["link"]
    urllib.request.urlretrieve(fileURL, "data.csv")
    dataArray = []

    with open('data.csv', 'r', encoding="ANSI") as file:
        reader = csv.reader(file)
        for row in reader:
            stringRow = ''.join(row)
            singleRow = stringRow.split(';')
            dataArray.append(singleRow)

    if args == None:
        return Data.Data(dataArray)

    for i in args:
        if i == "-mężczyźni":
            MakeArrOnlyMen(dataArray)
        elif i == "-kobiety":
            MakeArrOnlyWomen(dataArray)

    return Data.Data(dataArray)


if __name__ == "__main__":

    data = DataProcessing(sys.argv)

    # calling tests
    os.system("pytest _test.py")

    # calling main features from data class
    try:
        for num, i in enumerate(sys.argv):
            if i == "-srednia":
                data.AverageVoivo(sys.argv[num + 1], int(sys.argv[num + 2]))
            elif i == "-zdawalnosc":
                data.PercentPassInVoivo(sys.argv[num + 1])
            elif i == "-najlepsze":
                data.MostPassInYear(int(sys.argv[num + 1]))
            elif i == "-regresja":
                data.DetectRegression()
            elif i == "-porownaj":
                data.CompareVoivos(sys.argv[num + 1], sys.argv[num + 2])
    except:
        print("Coś poszło nie tak, sprawdź podane parametry jeszcze raz")
