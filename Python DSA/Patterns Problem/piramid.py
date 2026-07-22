n:int = int(input("Enter a number = "))

for i in range(1,n+1) : 

    
    for k in range(n-i) : 
        print(" ",end="") 
        
        
    for j in range((2*i)-1) : 
        print("*", end="")
    print()
