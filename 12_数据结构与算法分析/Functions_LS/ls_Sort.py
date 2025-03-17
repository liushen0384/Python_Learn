"""
排序算法
"""

def bubbleSort(alist, reverse = False):
    """
    冒泡排序
    :param alist: 要排序的列表
    :param reverse: False：顺序排序，True：逆序排序
    """
    if reverse:
        for passnum in range(len(alist) - 1, 0, -1):
            for i in range(passnum):
                if alist[i] < alist[i + 1]:
                    alist[i], alist[i + 1] = alist[i + 1], alist[i]
    else:
        for passnum in range(0, len(alist)):
            for i in range(len(alist) - passnum - 1):
                if alist[i] > alist[i + 1]:
                    alist[i], alist[i + 1] = alist[i + 1], alist[i]

def shortBubbleSort(alist, reverse = False):
    """
    短冒泡排序，在冒泡排序的基础上进行了修改，可以节省资源
    :param alist: 要排序的列表
    :param reverse:  False：顺序排序，True：逆序排序
    """
    exchanges = True
    if reverse:
        for passnum in range(len(alist) - 1, 0, -1):
            exchanges = True
            for i in range(passnum):
                if alist[i] < alist[i + 1]:
                    exchanges =False
                    alist[i], alist[i + 1] = alist[i + 1], alist[i]
            if exchanges:
                break
    else:
        for passnum in range(0, len(alist)):
            exchanges = True
            for i in range(len(alist) - passnum - 1):
                if alist[i] > alist[i + 1]:
                    exchanges = False
                    alist[i], alist[i + 1] = alist[i + 1], alist[i]
            if exchanges:
                break

def selectSort(alist, reverse = False):
    """
    选择排序
    :param alist: 要排序的列表
    :param reverse: False：顺序排序，True：逆序排序
    """
    if not reverse:
        for j in range(len(alist) - 1, 0, -1):
            max = 0
            for i in range(j):
                if alist[i + 1] > alist[max]:
                    max = i + 1
            alist[j], alist[max] = alist[max], alist[j]
    else:
        for j in range(len(alist) - 1, 0, -1):
            min = 0
            for i in range(j):
                if alist[i + 1] < alist[min]:
                    min = i + 1
            alist[j], alist[min] = alist[min], alist[j]

def insertSort(alist, reverse = False):
    """
    插入排序
    :param alist: 要排序的列表
    :param reverse: False：顺序排序，True：逆序排序
    """
    if not reverse:
        for passnum in range(1, len(alist)):
            for i in range(passnum, 0, -1):
                if alist[i] < alist[i - 1]:
                    alist[i], alist[i - 1] = alist[i - 1], alist[i]
                else:
                    break
    else:
        for passnum in range(1, len(alist)):
            for i in range(passnum, 0, -1):
                if alist[i] > alist[i - 1]:
                    alist[i], alist[i - 1] = alist[i - 1], alist[i]
                else:
                    break

def shellSort(alist, stap):
    """
    希尔排序
    :param alist: 要排序的列表
    :param reverse: False：顺序排序，True：逆序排序
    """
    sublistcount = len(alist) // stap
    while sublistcount > 0:
        for startposition in range(sublistcount):
            shellInsertSort(alist, startposition, sublistcount)
        sublistcount = sublistcount // stap


def shellInsertSort(alist, start, stap):
    """
    希尔排序内置插入排序
    """
    for passnum in range(start + stap, len(alist), stap):
        for i in range(passnum, 0, -stap):
            if alist[i] < alist[i - stap] and (i - stap) >= 0:
                alist[i], alist[i - stap] = alist[i - stap], alist[i]
            else:
                break

def mergeSort(alist):
    """
    归并排序函数
    """
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1

    print("Merging ", alist)

def quickSort(alist):
    """
    快速排序
    :param alist: 需要排序的列表
    """
    inQuickSort(alist, 0, len(alist) - 1)

def inQuickSort(alist, basispoint, rightseek):
    rightseekold = rightseek
    basispointold = basispoint
    if basispoint < rightseek:
        leftseek = basispoint + 1
        while leftseek < rightseek:
            while alist[leftseek] < alist[basispoint]:
                leftseek = leftseek + 1
            while alist[rightseek] > alist[basispoint]:
                rightseek = rightseek - 1
            if leftseek < rightseek:
                alist[leftseek], alist[rightseek] = alist[rightseek], alist[leftseek]
        alist[rightseek], alist[basispoint] = alist[basispoint], alist[rightseek]
        inQuickSort(alist, rightseek + 1, rightseekold)
        inQuickSort(alist, basispointold, rightseek - 1)
    print(alist)

