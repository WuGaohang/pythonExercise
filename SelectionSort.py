def SelectionSort(NumList):
    for i in range(1, len(NumList)):
        for j in range(i, len(NumList)):
            min = i
            if (NumList[j] < NumList[min]):
                min = j
            temp = NumList[i]
            NumList[i] = NumList[min]
            NumList[min] = temp
NumList = [12, 64, 35, 18, 96, 158, 31, 48, 20]
SelectionSort(NumList)
print(NumList)