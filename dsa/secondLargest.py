def second_largest(numbers):
    # Remove duplicates by converting the list to a set
    unique_numbers = list(set(numbers))
    
    # Check if there are at least two unique numbers
    if len(unique_numbers) < 2:
        return "List does not have enough unique numbers."
    
    # Sort the list in descending order
    unique_numbers.sort(reverse=True)
    
    # The second largest number will be at index 1
    return unique_numbers[1]

# Example usage
numbers = [12, 35, 1, 10, 34, 1]
result = second_largest(numbers)

# Output the result
print("The second largest number is:", result)
import math

def find_second_largest(nums):
    largest = -math.inf
    secondLargest = -math.inf
    for num in nums:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest and num != largest:
            secondLargest = num
        
    return secondLargest

nums = [10, 5, 8, 20, 3]
print(find_second_largest(nums))