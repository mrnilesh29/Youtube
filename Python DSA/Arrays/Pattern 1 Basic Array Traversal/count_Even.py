def count_even(arr):
    E = 0 
    for i in range(len(arr)) : 
        if arr[i] %2 == 0 : E +=1 
    return E
        


# Test Cases
print(count_even([1, 2, 3, 4, 6]))   # Expected: 3
print(count_even([2, 4, 6, 8]))       # Expected: 4
print(count_even([1, 3, 5, 7]))       # Expected: 0
print(count_even([-2, 3, 4, -6]))     # Expected: 3
print(count_even([0, 1, 2]))          # Expected: 2
