def max_even_count(arr, k):
    # your code
    count = 0 
    maxx = 0 
    
    for i in range(k) : 
        if arr[i]%2 ==0  : count +=1 
        
    maxx = max(count,maxx)
    i = 0 
    for j in  range(k,len(arr)): 
        if arr[i] %2 ==0 : count -=1 
        if arr[j] %2  ==0 : count += 1 
        
        maxx = max(maxx,count)
        i+=1 
    return maxx
        
    
print(max_even_count([1,3,5,2,4],2))