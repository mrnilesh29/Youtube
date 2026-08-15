def all_occurrences(arr, target):
    count = []
    for i in range(len(arr)): 
        if arr[i] == target : count.append(i)
        
    return count


# Test Cases
print(all_occurrences([4, 2, 7, 2, 9, 2], 2))
# Expected: [1, 3, 5]

print(all_occurrences([5, 5, 3, 5], 5))
# Expected: [0, 1, 3]

print(all_occurrences([1, 2, 3, 4], 9))
# Expected: []

print(all_occurrences([], 5))
# Expected: []