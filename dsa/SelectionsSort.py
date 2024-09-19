arr = [5, 4, 1, 2, 8]

def SelectionSort(arr):
    n = len(arr)

    for i in range(n - 1):
        minEle = i
        for j in range(i + 1, n):
            if arr[j] < arr[minEle]:
                minEle = j
        arr[minEle], arr[i] = arr[i] , arr[minEle]
        
    return arr

print(SelectionSort(arr))
