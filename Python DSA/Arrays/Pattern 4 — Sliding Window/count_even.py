def count_even_windows(arr, k):
    ans = []
    w_c = 0 
    for i in range(k):
        if arr[i] %2 ==0 : w_c+=1 
        
    ans.append(w_c)
    
    i = 0 
    for j in range(k,len(arr)) : 
        if arr[i] %2 ==0 : w_c -= 1 
        if arr[j] % 2 == 0 : w_c += 1  
        ans.append(w_c) 
        i+=1 
        
    return ans 

print(count_even_windows([2,1,4,6],3))