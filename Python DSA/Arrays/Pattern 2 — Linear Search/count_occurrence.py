def count_occurrences(arr, target):
    count = 0 
    for i in range(len(arr)) : 
        if target == arr[i] : count+=1 
        
    return count 



# Test Cases
print(count_occurrences([1, 2, 2, 3, 2], 2))   # Expected: 3
print(count_occurrences([5, 5, 5], 5))         # Expected: 3
print(count_occurrences([1, 2, 3, 4], 9))      # Expected: 0
print(count_occurrences([], 5))                # Expected: 0
