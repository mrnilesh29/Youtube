def range_sum(arr, left, right):
    sum = 0 
    for i in range(len(arr)):
        sum += arr[i] 
        arr[i] = sum 
    
    if left==0 : return arr[right]
    
    return arr[right] - arr[left-1]
         
     

print(range_sum([4, 2, -3, 5, 1, -2, 6],2,5))