age = int(input("Enter your age = "))

if age >= 18 :
    print("you are eligible for voteing")
else : 
    print("not eligible")
    
    

a = int(input("Enter a number = "))  #10 
b = int(input("Enter a number = ")) #20 
c = int(input("Enter a number = ")) #30 
d = int(input("Enter a number = ")) #40 

number = int(input("Enter a number = "))

if number <= a : 
    print("a")
elif number > a and number <= b: 
    print("b")
elif number > b and number <= c: 
    print("c")
else : 
    print("D") 
    

A = int(input("Enter a number = "))
B = int(input("Enter a number  = "))


if A >B: 
    print("A is greater") 
else :
    print("B is greatest ")
       

ch = input("Enter your gender = ")
if ch == "M" or ch == "m" : 
    print("good morning sir ")
elif ch == "F" or ch =="f" : 
    print("good morning mam")
else: 
    print("invaild gender")
    

number = int(input("Enter your number = "))

if number %2 == 0 : 
    print("number is even")
else : 
    print("Number is odd")



year = int(input("Enter year = "))


if year % 100 == 0 : 
    if year %400 : 
        print("leap year")
    else : 
        print("not leap year")
else : 
    if year %4 == 0 : 
        print("leap year")
    else : 
        print("not leap year")
        
    

temp = int(input("Enter temprature in celcies = "))

if temp < 0 : 
    print("Freezing Cold ")
elif temp > 0 and temp <= 10 : 
    print("very cold")
elif temp > 10 and temp <= 20 : 
    print("cold")
elif temp > 20 and temp <= 30 : 
    print("pleasent")
elif temp > 30 and temp <= 40 : 
    print("hot")
else : 
    print("very hot")
    


    