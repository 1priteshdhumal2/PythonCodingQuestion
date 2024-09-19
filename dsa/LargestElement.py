nums = [10, 5, 8, 20, 3]
nums.sort()
print(nums[len(nums) - 1])

def largestElemnt(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num

    return largest

print(largestElemnt(nums))