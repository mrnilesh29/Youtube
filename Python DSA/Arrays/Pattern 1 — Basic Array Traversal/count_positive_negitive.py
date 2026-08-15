def count_pos_neg(arr):
    pos  = 0 
    neg = 0 
    for i in range(len(arr)) : 
        if arr[i] > 0 : pos +=1 
        elif arr[i] < 0 : neg +=1 
    t = (pos,neg)
    return t
        
        


# Test Cases
print(count_pos_neg([1, -2, 3, -4, 5]))
# Expected: (3, 2)

print(count_pos_neg([-1, -2, -3]))
# Expected: (0, 3)

print(count_pos_neg([1, 2, 3]))
# Expected: (3, 0)

print(count_pos_neg([0, 1, -1]))
# Expected: (1, 1)
