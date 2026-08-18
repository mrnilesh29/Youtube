def count_negative_windows(arr, k):
    ans  = []
    n_c = 0 
    
    for i in range(k) : 
        if arr[i] < 0 : n_c+=1 
        
    ans.append(n_c)
    
    i = 0 
    for j in range(k,len(arr)): 
        if arr[i] < 0 : n_c -= 1 
        if arr[j] < 0   : n_c += 1 
        ans.append(n_c)
        i+=1 
    return ans
        
        
        
print(count_negative_windows([1,-2,-3,4,5],3))