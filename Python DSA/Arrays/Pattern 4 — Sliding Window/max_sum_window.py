def max_sum_window(arr, k):
    window_sum = sum(arr[:k]) 
    maxx = window_sum 
    
    i = 0 
    j = k 
    max_index = 0
    while j < len(arr) : 
        window_sum += arr[j] 
        window_sum -= arr[i]
        
        if window_sum > maxx : 
            maxx = window_sum 
            max_index = i+1
        i+=1 
        j+=1 
    return arr[max_index:max_index+k]
            
            
print(max_sum_window([5,5,1,2],2))
        
    