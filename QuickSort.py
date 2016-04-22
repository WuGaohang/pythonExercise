def partition(NumList, lo, hi):
    i = lo
    j = hi + 1
    v = NumList[lo]

    while(True):
        i = i + 1
        while (NumList[i] < v):
            if (i == hi):
                break
            i = i + 1
        j = j - 1
        while (v < NumList[j]):
            if (j == lo):
                break
            j = j - 1
        if (i >= j):
            break
        temp = NumList[i]
        NumList[i] = NumList[j]
        NumList[j] = temp
    temp = NumList[lo]
    NumList[lo] = NumList[j]
    NumList[j] = temp
    return j

def sort(NumList, lo, hi):
    if (hi <= lo):
        return
    j = partition(NumList, lo, hi)
    sort(NumList, lo, j - 1)
    sort(NumList, j + 1, hi)

def QuickSort(NumList):
    sort(NumList, 0, len(NumList) - 1)

NumList = [12, 64, 35, 18, 96, 158, 31, 48, 20]
QuickSort(NumList)
print(NumList)
