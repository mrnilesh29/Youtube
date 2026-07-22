n = int(input("Enter your input = "))

 
for i in range(n,0,-1): 
    start = 2 * i - 1
    for j in range(n-i-1) : 
        print(" " ,end= "")
    
    for k in range(start): 
        print("*" ,end="")
    print()
    