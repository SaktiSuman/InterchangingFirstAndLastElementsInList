def swapList(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    return newList
list = [12, 34, 45, 56, 78]
print(swapList(list))