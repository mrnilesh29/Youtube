     
def move_zeros(arr) :   
    s = 0 
    for i in range(0,len(arr)) : 
        if arr[i] != 0 : 
            arr[s] = arr[i] 
            s+=1 

    for i in range(s,len(arr),1) : 
        arr[i] = 0 
    return arr
        
        
print(move_zeros([0,1,0,1,2,3]))
    
