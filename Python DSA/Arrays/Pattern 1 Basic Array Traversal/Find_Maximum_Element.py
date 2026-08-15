def find_max(arr):
    maxx = arr[0]
    for i in range(0,len(arr),1) : 
        if arr[i] > maxx : maxx = arr[i]
    return maxx


# Test Cases
print(find_max([4, 2, 9, 1, 7]))     # Expected: 9
print(find_max([10, 5, 3]))          # Expected: 10
print(find_max([-5, -2, -9]))        # Expected: -2
print(find_max([7]))                 # Expected: 7
