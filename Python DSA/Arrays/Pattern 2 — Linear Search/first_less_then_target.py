def first_smaller(arr, target):
    for i in range(len(arr)): 
        if arr[i] < target : return i 
    return -1
        
        
        


# Test Cases
print(first_smaller([5, 8, 3, 7, 2], 6))    # Expected: 2
print(first_smaller([10, 9, 8, 7], 8))      # Expected: 3
print(first_smaller([1, 2, 3], 1))           # Expected: -1
print(first_smaller([5, 4, 3], 10))          # Expected: 0
print(first_smaller([], 5))                  # Expected: -1