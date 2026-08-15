def is_sorted(arr):
    if len(arr) <=1 : return True 
    for i in range(1,len(arr),1) : 
        if arr[i] <arr[i-1] : return False 
    return True


# Test Cases
print(is_sorted([1, 2, 3, 4, 5]))    # Expected: True
print(is_sorted([1, 2, 4, 3, 5]))    # Expected: False
print(is_sorted([5]))                # Expected: True
print(is_sorted([1, 1, 2, 3]))       # Expected: True
print(is_sorted([]))                 # Expected: True