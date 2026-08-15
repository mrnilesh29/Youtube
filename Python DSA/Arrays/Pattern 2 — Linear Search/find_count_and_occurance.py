def find_info(arr, target):
    frist_occurr = -1
    count = 0
    for i in range(len(arr)): 
        if arr[i] == target : 
            if frist_occurr == -1 :
                frist_occurr = i 
            count+=1 
            
    t = (count,frist_occurr)
    return t


# Test Cases
print(find_info([4, 2, 7, 2, 9, 2], 2))
# Expected: (3, 1)

print(find_info([5, 5, 3, 5], 5))
# Expected: (3, 0)

print(find_info([1, 2, 3, 4], 9))
# Expected: (0, -1)

print(find_info([], 5))
# Expected: (0, -1)