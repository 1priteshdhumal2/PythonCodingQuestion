def removeDuplicates(nums):
    uniqueNumbers = []
    for num in nums:
        if num not in uniqueNumbers:
            uniqueNumbers.append(num)
    return uniqueNumbers

nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
print(removeDuplicates(nums))