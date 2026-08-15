def nearest_element(arr, target):
    near = float("+inf")
    index = -1
    for i in range(len(arr)) :         
        subs = abs(arr[i] - target)
        if subs < near : 
            near = subs 
            index = i 
    return index
