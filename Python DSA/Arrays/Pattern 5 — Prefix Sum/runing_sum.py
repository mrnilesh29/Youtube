def prefix_sum(arr):
    sum = 0 
    for i in range(len(arr)): 
        sum += arr[i] 
        arr[i] = sum 
    
    return arr

print(prefix_sum([5,5,5]))
