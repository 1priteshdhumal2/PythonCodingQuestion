def buble_sort(elements):
    n = len(elements)
    for i in range(n):
        for j in range( i + 1, n):
            if elements[i] > elements[j ]:
                elements[i], elements[j + 1] = elements[j+ 1], elements[i]

nums = [5, 2, 8, 1, 9]
buble_sort(nums)
print(nums)