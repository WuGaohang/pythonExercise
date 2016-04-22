def Merge(NumList1, NumList2, lo, mid, hi):
    for k in range(lo, hi + 1):
        if (k < len(NumList2)):
            NumList2[k] = NumList1[k]
        else:
            NumList2.append(NumList1[k])
    i = lo
    j = mid + 1
    for k in range(lo, hi + 1):
        if (i > mid):
            NumList1[k] = NumList2[j]
            j = j + 1
        elif (j > hi):
            NumList1[k] = NumList2[i]
            i = i + 1
        elif (NumList2[j] < NumList2[i]):
            NumList1[k] = NumList2[j]
            j = j + 1
        else:
            NumList1[k] = NumList2[i]
            i = i + 1

def Sort(NumList1, NumList2, lo, hi):
    if (hi <= lo):
        return
    mid = lo + ((hi - lo) // 2)
    Sort(NumList1, NumList2, lo, mid)
    Sort(NumList1, NumList2, mid + 1, hi)
    Merge(NumList1, NumList2, lo, mid, hi)

def MergeSort(NumList):
    aux = []
    Sort(NumList, aux, 0, len(NumList) - 1)

NumList = [12, 64, 35, 18, 96, 158, 31, 48, 20]
MergeSort(NumList)
print(NumList)