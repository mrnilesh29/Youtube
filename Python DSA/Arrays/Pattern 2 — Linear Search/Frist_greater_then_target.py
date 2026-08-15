def first_greater(arr, target):
    for i in range(len(arr)): 
        if arr[i] > target : 
            return i 
    return -1

# Test Cases
print(first_greater([1, 3, 5, 7, 9], 4))    # Expected: 2
print(first_greater([2, 4, 6, 8], 6))        # Expected: 3
print(first_greater([1, 2, 3], 5))           # Expected: -1
print(first_greater([10, 5, 8], 4))          # Expected: 0
print(first_greater([], 5))                  # Expected: -1