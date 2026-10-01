def Js_SemiEfficient_Sort(listA):
    '''Sort's list'''
    from math import ceil
    flag = 0
    temp = [None] *  int(ceil(max(listA)+1))
    listB = [None] * (len(listA)-1)
    for i in range(len(listA)):
        if temp[ceil(listA[i]-1)] != None:
            listB[i] = listA[i]
        else:
            temp[ceil(listA[i]-1)] = listA[i]

    listB = list(filter(None, listB))
    for i in range(len(listB)):
        if temp[ceil(listB[i])] == None:
            temp[ceil(listB[i])] = listB[i]
        elif temp[ceil(listB[i])-2] == None:
            temp[ceil(listB[i])-2] = listB[i]
        else:
            temp.insert(int(ceil(listB[i])-flag), listB[i])
            flag += 1

    return list(filter(None, temp))

listA = [99, 99, 99, 99,43,67,79,90,100,98,377]
print(Js_SemiEfficient_Sort(listA))