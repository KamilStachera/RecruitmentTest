class Data:
    def __init__(self, dataArray):
        self.dataArray = dataArray

    # Check if given year is in boundaries if not raise an exception
    def CheckYear(self, year):
        if 2010 <= year <= 2018:
            pass
        else:
            raise

    # Function for first task
    def AverageVoivo(self, voivo, year):
        self.CheckYear(year)
        dataSum = 0

        # Searching in arrays for given voivodeship term "przystąpiło" and then checking if year is good
        # if yes add data in selected row to sum
        for dataRow in self.dataArray:
            if voivo in dataRow:
                if "przystąpiło" in dataRow:
                    if int(dataRow[3]) <= year:
                        dataSum += int(dataRow[4])

        average = int(dataSum / (year - 2009))
        print('{0} - {1}'.format(year, average))

    # Solution for second task
    def PercentPassInVoivo(self, voivo):
        voivoData = []

        # Searching for given voivodeship
        for dataRow in self.dataArray:
            if voivo in dataRow:
                voivoData.append(dataRow)

        # Printing pass rate for 2010-2018 period
        for year in range(2010, 2019):
            participated = 0
            passed = 0

            for dataRow in voivoData:
                if str(year) in dataRow:
                    if "przystąpiło" in dataRow:
                        participated += int(dataRow[4])
                    if "zdało" in dataRow:
                        passed += int(dataRow[4])

            percentage = int((passed / participated) * 100)

            print('{0} - {1} %'.format(year, percentage))

    # General function that returns dictionary of each voivo pass rate for every year
    def PassPercentage(self, year):
        self.CheckYear(year)
        yearData = []
        for dataRow in self.dataArray:
            if str(year) in dataRow:
                # Skipping redundant values
                if "Polska" in dataRow:
                    continue
                yearData.append(dataRow)

        voivoDictParticipated = {}
        voivoDictPassed = {}
        voivoDictPercentage = {}
        for dataRow in yearData:
            voivoDictParticipated[dataRow[0]] = 0
            voivoDictPassed[dataRow[0]] = 0
            voivoDictPercentage[dataRow[0]] = 0

        for dataRow in yearData:
            if "przystąpiło" in dataRow:
                voivoDictParticipated[dataRow[0]] += int(dataRow[4])
            if "zdało" in dataRow:
                voivoDictPassed[dataRow[0]] += int(dataRow[4])

        for voivo in set(voivoDictParticipated.keys()) & set(voivoDictPassed.keys()):
            voivoDictPercentage[voivo] = (voivoDictPassed[voivo] / voivoDictParticipated[voivo]) * 100

        return voivoDictPercentage

    # Function for task three
    def MostPassInYear(self, year):
        self.CheckYear(year)
        voivoDictPercentage = self.PassPercentage(year)

        sortedDict = [(k, voivoDictPercentage[k]) for k in
                      sorted(voivoDictPercentage, key=voivoDictPercentage.get, reverse=True)]

        winnerVoivo, percentage = sortedDict[0]

        print('{0} - województwo {1}'.format(year, winnerVoivo))

    # Function for task four
    def DetectRegression(self):
        dictArray = []

        for year in range(2010, 2019):
            voivoDictPercentage = self.PassPercentage(year)
            dictArray.append(voivoDictPercentage)

        for num in range(0, len(dictArray)):
            # Skipping year 2018 because of lacking 2019 data
            if num != 8:
                for voivo, percetage in dictArray[num].items():
                    if dictArray[num + 1][voivo] < percetage:
                        print('województwo {0}: {1} -> {2}'.format(voivo, num + 2010, num + 2011))

    # Function for task five
    def CompareVoivos(self, firstVoivo, secondVoivo):
        dictArray = []

        for year in range(2010, 2019):
            voivoDictPercentage = self.PassPercentage(year)
            dictArray.append(voivoDictPercentage)

        for num in range(0, len(dictArray)):
            if dictArray[num][firstVoivo] > dictArray[num][secondVoivo]:
                print('{0} - {1}'.format(num + 2010, firstVoivo))
            else:
                print('{0} - {1}'.format(num + 2010, secondVoivo))
