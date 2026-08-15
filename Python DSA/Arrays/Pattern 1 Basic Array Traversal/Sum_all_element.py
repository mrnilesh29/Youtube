def array_sum(arr):
    sum = 0 
    for i in range(len(arr)) : 
        sum += arr[i]
    return sum


# Test Cases
print(array_sum([1, 2, 3, 4, 5]))   # Expected: 15
print(array_sum([10, 20, 30]))       # Expected: 60
print(array_sum([-1, 2, -3, 4]))     # Expected: 2
print(array_sum([7]))                # Expected: 7
