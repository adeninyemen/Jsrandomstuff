def Js_Inefficient_Sort(listA):
    '''Sort's list'''
    from math import ceil
    temp = [None] *  int(ceil(max(listA)+1))
    listB = [None] * (len(listA)-1)
    for i in range(len(listA)-1):
        if temp[ceil(listA[i]-1)] == listA[i]:
            listB[i] = listA[i]
        else:
            temp[ceil(listA[i]-1)] = listA[i]

    listB = list(filter(None, listB))
    for i in range(len(listB)):
        temp.insert(int(ceil(listB[i])-i), listB[i])
    return list(filter(None, temp))

listA = [231, 123, 1251, 12, 99, 971.5, 971.5, 0, 23, 14, 14, 14, 14]
print(Js_Inefficient_Sort(listA))