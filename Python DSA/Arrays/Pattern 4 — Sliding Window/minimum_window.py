def min_sum_window(arr, k):
    window = sum(arr[:k])
    minn = window 
    min_index = 0 
    i = 0 
    j = k 
    
    while(j<len(arr)): 
        window += arr[j] 
        window -= arr[i] 
        
        if minn > window : 
            minn = window 
            min_index = i +1 
        
        i+=1 
        j+=1 
    return arr[min_index:min_index+k]
