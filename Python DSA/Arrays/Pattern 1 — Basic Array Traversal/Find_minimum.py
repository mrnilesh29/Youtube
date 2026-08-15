def find_min(arr):
    min = arr[0]
    for i in range(len(arr)): 
        if min > arr[i] : min = arr[i]
    return min
            
        


# Test Cases
print(find_min([4, 2, 9, 1, 7]))      # Expected: 1
print(find_min([10, 5, 3]))           # Expected: 3
print(find_min([-5, -2, -9, -1]))     # Expected: -9
print(find_min([7]))                  # Expected: 7