# def count_greater_than_5(n): 
#     if n==0 : 
#         return  0 
#     if (n%10) > 5 : 
#         return 1+count_greater_than_5(n//10)
#     else : 
#         return count_greater_than_5(n//10)


# print(count_greater_than_5(123789))  # 123789 = argument



# def count_five(n):  # n = parameter
#     # your code
#     if n ==0 : return 0 
#     if (n%10) == 5 : return 1+count_five(n//10)
#     else : return count_five(n//10)

# print(count_five(1525553))  # 1525553 = argument



# def count_less_than_5(n):  # n = parameter
#     if n ==0 : return 0 
#     if n %10 <5 : return 1+count_less_than_5(n//10)
#     else: return count_less_than_5(n//10)
    

# print(count_less_than_5(123456))  # 123456 = argument


def count_greater_than_3(n):  # n = parameter
    if n ==0 : return 0 
    if n%10 > 3 : 
        return 1 + count_greater_than_3(n//10)
    else : 
        return count_greater_than_3(n//10)

print(count_greater_than_3(1234567))  # 1234567 = argument



# def count_less_than_7(n): 
#     if n ==0 : return 0 
#     if n%10 < 7 : 
#         return 1 + count_less_than_7(n//10)
#     else : 
#         return count_less_than_7(n//10)

# print(count_less_than_7(12345678))  # 12345678 = argument