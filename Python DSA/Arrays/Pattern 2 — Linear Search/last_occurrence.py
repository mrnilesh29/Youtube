def last_occurrence(arr, target):
    for i in range(len(arr)-1 , -1,-1) : 
        if arr[i] == target : 
            return i 
        
    return -1 
        


# Test Cases
print(last_occurrence([4, 2, 7, 2, 9], 2))   # Expected: 3
print(last_occurrence([5, 3, 5, 8], 5))      # Expected: 2
print(last_occurrence([1, 2, 3, 4], 9))      # Expected: -1
print(last_occurrence([], 5))                 # Expected: -1