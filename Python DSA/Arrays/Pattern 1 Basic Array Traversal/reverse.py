def reverse_array(arr):
    if len(arr) == 0 : return arr
    end = len(arr)-1
    start = 0 
    while start != end : 
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp 
        start += 1
        end -=1 

    return arr


# Test Cases
print(reverse_array([1, 2, 3, 4, 5]))
# Expected: [5, 4, 3, 2, 1]

print(reverse_array([10, 20, 30]))
# Expected: [30, 20, 10]

print(reverse_array([7]))
# Expected: [7]

print(reverse_array([]))
# Expected: []
