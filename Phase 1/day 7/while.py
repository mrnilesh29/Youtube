n = int(input("Enter a number = ")) #"234535"

rev = 0

while(n!=0):
    l = n%10 
    rev = rev * 10 + l 
    n = n//10 
    
print(type(rev))
    

a = 12345
print(a%10)
print(a//10)
    


n = int(input("Enter a number = "))
rev = 0 
temp = n 

while(n != 0) : 
    l = n%10 
    rev =( rev * 10) +l 
    n = n //10 
n = 0 
  
if temp == rev : 
    print("palindorme number")
else : 
    print("Not palindrome number")
    
    

import random 
A = random.randint(1,10,)
print(A)

while(True) : 
    n = int(input("guess the number between 1 to 10  =  "))
    if n == A : 
        print("you Win this game")
        break
    
    else : 
        print("you are not correct try agin")

    

