list1 = [5, 4, 1, 8, 3]

def bubbleSort(list1):
    n = len(list1)
    
    for i in range(n):
        isSwapped = False
        for j in range(0 , n - i - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
                isSwapped = True
        if isSwapped == False:
            break
    return list1
list2 = bubbleSort(list1)
print(list2)