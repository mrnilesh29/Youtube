def last_smaller(arr, target):
    for i in range(len(arr)-1 , -1,-1) : 
        if arr[i] < target : return i 
    return -1


# Test Cases
print(last_smaller([5, 8, 3, 7, 2], 6))   # Expected: 4
print(last_smaller([10, 9, 8, 7], 8))     # Expected: -1
print(last_smaller([1, 2, 3], 5))         # Expected: 2
print(last_smaller([5, 4, 3], 4))         # Expected: 2
print(last_smaller([], 5))                # Expected: -1