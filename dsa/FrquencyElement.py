def count_frequency(lst):
    # Create an empty dictionary to store frequency of each element
    frequency = {}

    # Iterate through the list
    for item in lst:
        # Increment count if the item is already in the dictionary
        if item in frequency:
            frequency[item] += 1
        # Add the item to the dictionary if not present
        else:
            frequency[item] = 1

    return frequency

# Sample list
nums = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6, 6]

# Get the frequency of each element
result = count_frequency(nums)
print("Count terms of dictionary",count_frequency(nums))

# Print the result
print("Element Frequency:")
for key, value in result.items():
    print(f"{key}: {value}")


for num in nums:
    cnt = 0
    no = num
    for j in nums:
        if (no == j):
            cnt += 1

    print("Frequency of", no, "is", cnt)

