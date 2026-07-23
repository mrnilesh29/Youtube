

# def decorate(func):
#     def wrapper() : 
#         print("i am printing before gretting")
#         func()
#         print("i am printing after gretting")  
#     return wrapper   
    



# @decorate
# def hello() : 
#     print("hello i am hello function")
    
# hello()



# def sumdecoration(func) :
#     def wrapper(*args ,**kwargs)  : 
#         print("i am printing before addition ")
#         func(*args,**kwargs)
#         print("i am printing after addition")
#     return wrapper
    


# @sumdecoration 
# def addtion(*args , **kwargs): 
#     sum = 0 
#     for i in args :
#         sum += i 
#     print(sum)
    
    
    
# addtion(10,20,30,40,50,40,50,60)

# def addition(**kwargs): 
#     print(kwargs)
        
    
# addition(a=10,b=20,c=30)


# a = 11
# print("even") if a%2 ==0 else print("odd")


# l = {i : i*2  for i in range(1,21) if i%2 ==0 }
# print(l)


# l1 = ["even" if i %2 == 0 else "odd" for i in range(1,21)]
# print(l1)



# add = lambda a,b : a+b 
# print(add(10,20))




# check = lambda a : "even" if a%2 ==0 else "odd"

# print(check(20))

# number = [1,2,3,4,5]
# k = map(lambda i : i**2 , number) 
# print(list(k))


# m = filter(lambda i : i%2 == 0 , number) 
# print(list(m))


