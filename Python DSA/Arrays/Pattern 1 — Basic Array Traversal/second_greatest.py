def second_largest(arr):
    maxx = float("-inf")
    smax = float("-inf")
    for i in range(len(arr)) : 
        if arr[i] > maxx : 
            smax = maxx 
            maxx = arr[i]
            
        elif arr[i] > smax and arr[i] != maxx: smax = arr[i]
    return smax
            
    


# Test Cases
print(second_largest([10, 5, 8, 20, 15]))   # Expected: 15
print(second_largest([4, 9, 2, 9, 7]))      # Expected: 7
print(second_largest([1, 2, 3]))            # Expected: 2
print(second_largest([-5, -2, -9]))         # Expected: -5
