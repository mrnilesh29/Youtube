def last_greater(arr, target):
    for i in range(len(arr)-1 , -1,-1): 
        if arr[i] > target : return i 
    return -1
        

# Test Cases
print(last_greater([1, 7, 3, 9, 5], 4))    # Expected: 3
print(last_greater([10, 5, 8, 12], 9))     # Expected: 3
print(last_greater([1, 2, 3], 5))          # Expected: -1
print(last_greater([5, 4, 3], 2))          # Expected: 2
print(last_greater([], 5))                 # Expected: -1