# def sum_digits(n):  # n = parameter
#     if n == 0 : return  0 
#     return n%10 + sum_digits(n//10)
     


# print(sum_digits(12345))  # 12345 = argument




# def product_digits(n):  # n = parameter
#     if n == 0 : 
#         return 1
#     return n%10 * product_digits(n//10)
 


# print(product_digits(1234))  # 1234 = argument





# def count_zero(n):  # n = parameter
    
#     if n == 0 : return 0 
#     if n %10 == 0 : return 1+count_zero(n//10)
#     else :return count_zero(n//10)


# print(count_zero(10203040))  # 10203040 = argument




# def product_n(n):  # n = parameter
#     # your code  
#     if n== 1 :return 1 
#     return n * product_n(n-1)
        


# print(product_n(5))  # 5 = argument




# def max_digit(n):
#     if n < 10: 
#         return n 
    
#     last = n%10 
#     maxx = max_digit(n//10)
    
#     if int(last) > int(maxx) : 
#         return last 
#     return maxx
    
        
    


# print(max_digit(58321))  # 58321 = argument


# def min_digit(n) : 
#     if n < 10 : 
#         return  n  
#     A = min_digit(n//10) 
#     n = n//10 
#     B = min_digit(n//10)
#     if A > B : 
#         return B 
#     return A 

       
    
    
# print(min_digit(58321))


# def count_digits(n):  # n = parameter
#     # your code
#     if n == 0 : return 0 
#     return 1 + count_digits(n//10)



# print(count_digits(58321))  # 58321 = argument