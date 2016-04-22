def InsertionSort(NumList):
    for i in range(0, len(NumList)):
        j = i
        while (j > 0 and NumList[j] < NumList[j - 1]):
            temp = NumList[j]
            NumList[j] = NumList[j - 1]
            NumList[j - 1] = temp
            j = j - 1
NumList = [12, 64, 35, 18, 96, 158, 31, 48, 20]
InsertionSort(NumList)
print(NumList)