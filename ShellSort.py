def ShellSort(NumList):
    N = len(NumList)
    h = 1
    while (h < N // 3):
        h = 3 * h + 1
    while (h >= 1):
        for i in range(h, N):
            j = i
            while (j >= h and NumList[j] < NumList[j - h]):
                temp = NumList[j]
                NumList[j] = NumList[j - h]
                NumList[j - h] = temp
                j = j - h
        h = h // 3
NumList = [12, 64, 35, 18, 96, 158, 31, 48, 20]
ShellSort(NumList)
print(NumList)