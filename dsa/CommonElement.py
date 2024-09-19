def findcommele(list1, list2):
    commonElements = []
    for item in list1:
        if item in list2:
            commonElements.append(item)
        
    return commonElements

list1 = [1,2,3,4,5]
list2 = [4, 5, 6,7,8]
print(findcommele(list1, list2))