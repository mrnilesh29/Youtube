n = int(input("Enter a number = "))

for i in range(1,n+1,1):
    print("Hello World")



natural = int(input("Enter a number = "))

for i in range(1,natural+1 ,1) : 
    print(i)
    
    
n = int(input("Enter a  number = "))

for i in range(n,0,-1): 
    print(i)


n = int(input("Enter a number = "))
for i in range(1,11,1) : 
    print(n *i)  # 2*1 = 2 
    
    

n = int(input("Enter a number = "))
sum = 0 

for i in range(1,n+1,1):
    sum = sum + i 
    
print(sum)
    

n = int(input("Enter a number = "))
fact = 1 

for i in range(n,0,-1):
    fact *= i 
    
print(fact)
    


n = int(input("Enter a number = "))
even_sum = 0 
odd_sum = 0 

for i in range(0,n+1,1): 
    if i %2 ==0 :
        even_sum+=i 
    else : 
        odd_sum += i 
        
print(even_sum)
print(odd_sum)
    
    
    
n = int(input("Enter a number = "))

for i in range(1,n//2+1,1): 
    if n%i == 0 : 
        print(i)
    

    
    
n = int(input("Enter a number = "))

prefect = 0 

for i in range(1,n//2+1,1): 
    if n%i == 0 : 
        prefect += i 
        
if prefect == n : 
    print("The number is prefect Number")
else :
    print("not prefect number")
        
    
n = int(input("Enter a number "))

for i in range(2,n//2+1,1): 
    if n%i == 0 : 
        print("not prime number")
        break 
else : 
    print("prime number")
    

s = "Welcome"

for i in range(len(s)-1, -1,-1): 
    print(s[i])



s = "NAMANe"

rev = ""

for i in range(len(s)-1,-1,-1) : 
    rev += s[i] 
    
if rev == s : 
    print("palindrome")
else : 
    print("Not palindrome")
    
str1 = "P@#yn26at^&i5ve"

alpha = 0 
digits = 0
spical = 0 

for i in str1 : 
    if i.isalpha() : 
        alpha +=1
    elif i.isdigit() : 
        digits +=1 
    else : 
        spical +=1 

print(alpha , digits,spical)
         
        