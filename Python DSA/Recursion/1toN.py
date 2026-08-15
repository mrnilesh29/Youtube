# def sum_all_numbers(n) : 
#     if n == 0 : 
#         return 0
#     else : 
#         return n + sum_all_numbers(n-1)


# print(sum_all_numbers(20))
    
    
    
# def N_to_1(n) : 
#     if n == 0 : return 
#     print(n)
#     N_to_1(n-1)
    

# N_to_1(5)
        
        
        
# def sum_all_number(n) : 
#     if n ==0 : return 0 
#     return n+sum_all_number(n-1)

# print(sum_all_number(10))




# def fact(n) : 
#     if n==1 : return 1 
#     return n*fact(n-1)

# print(fact(5))
 
        
        
        
# def count_digit(n) : 
#     if n == 0  or n < 0 : 
#         return 0 
#     return 1 + count_digit(n//10)

    
# print(count_digit(111))


# def power(x, n):
#     if n==0 : return 1 
#     return x * power(x,n-1)

# print(power(2,5))


# def sum_digits(n) : 
#     if n == 0 : return 0 
#     return (n%10)+ (sum_digits(n//10))

# print(sum_digits(5832))





# def reverse(n,rev= 0 ): 
#     if n == 0 :return rev 
#     else:
#         rev = (rev *10) + (n%10)
#         return  reverse(n//10,rev)
    
    
# print(reverse(1234))


# def is_palindrome(s, left=0, right=None):
#     right = len(s)-left-1
#     if left >= right : return True
#     else : 
#         if s[left] != s[right]: return False 
#         return is_palindrome(s,left+1)
    
    
# print(is_palindrome("MADAMq"))



# def find_max(arr, index=0, maxx=None):
#     if len(arr) == 1 : return arr[0]
#     elif len(arr) == index : return maxx 
#     else : 
#         if maxx  is None : maxx = arr[0]
#         if maxx < arr[index] : maxx = arr[index]
#         return find_max(arr,index+1,maxx)
          


# # Test Cases
# print(find_max([4, 9, 2, 7, 5]))      # Expected: 9
# print(find_max([10, 3, 8, 1]))        # Expected: 10
# print(find_max([-5, -2, -9, -1]))     # Expected: -1



# def count_occurrences(arr, target, index=0,occur = 0):
#     if len(arr) == index : return occur 
#     else : 
#         if arr[index] == target : 
#             occur += 1 
#         return count_occurrences(arr,target,index+1 , occur)
            


# # Test Cases
# print(count_occurrences([1, 2, 3, 2, 2, 4], 2))   # Expected: 3
# print(count_occurrences([5, 5, 1, 5, 2], 5))      # Expected: 3
# print(count_occurrences([1, 2, 3, 4], 9))          # Expected: 0




# def is_sorted(arr, index=1):
#     if len(arr) == 0 : return False 
#     if len(arr) == 1 : return True 
#     if len(arr) == index : return True
#     else : 
#         if arr[index] < arr[index-1]: return False 
#     return is_sorted(arr,index+1)
               


# # Test Cases
# print(is_sorted([1, 2, 3, 4, 5]))   # Expected: True
# print(is_sorted([1, 2, 4, 3, 5]))   # Expected: False
# print(is_sorted([5]))               # Expected: True
# print(is_sorted([1, 1, 2, 3]))       # Expected: True


# def count_zeros(n, count=0, original=True):
#     if n == 0:
#         if original:
#             return 1
#         return count

#     if n % 10 == 0:
#         count += 1

#     return count_zeros(n // 10, count, False)


# # Test Cases
# print(count_zeros(102030))     # Expected: 3
# print(count_zeros(5005))       # Expected: 2
# print(count_zeros(12345))      # Expected: 0
# print(count_zeros(0))          # Expected: 1




# def array_product(arr, index=0,ans=1):
#     if len(arr) == index : return ans 
#     else :
#        ans =  arr[index] * array_product(arr,index+1,ans)
#        return ans

# # Test Cases
# print(array_product([1, 2, 3, 4]))    # Expected: 24
# print(array_product([5, 2, 3]))       # Expected: 30
# print(array_product([7]))             # Expected: 7
# print(array_product([2, 0, 5]))       # Expected: 0


# def first_occurrence(arr, target, index=0):
#     if len(arr) == 0 or len(arr) == index : return -1 
#     else : 
#         return index if arr[index] == target else first_occurrence(arr,target,index+1)


# # Test Cases
# print(first_occurrence([4, 2, 7, 2, 9], 2))   # Expected: 1
# print(first_occurrence([5, 3, 5, 8], 5))      # Expected: 0
# print(first_occurrence([1, 2, 3, 4], 9))       # Expected: -1
# print(first_occurrence([], 5))                 # Expected: -1




# def count_even(arr, index=0, count=0):
#     if len(arr) == 0 :  return 0 
#     if index == len(arr) : return count 
#     else : 
#         if arr[index] %2 ==0 : count+=1 
#         return count_even(arr,index+1,count)
    
            
# # Test Cases
# print(count_even([1, 2, 4, 7, 8]))    # Expected: 3
# print(count_even([2, 6, 10]))          # Expected: 3
# print(count_even([1, 3, 5]))           # Expected: 0
# print(count_even([]))                  # Expected: 0


# def find_min(arr, index=0, minx=None):
#     if len(arr) == 1 : return arr[0]
#     if index == len(arr) : return minx
#     else: 
#         if minx is None : minx = arr[0]
#         if arr[index] < minx : 
#             minx = arr[index]
#         return find_min(arr,index+1,minx)
    

# # Test Cases
# print(find_min([4, 9, 2, 7, 5]))       # Expected: 2
# print(find_min([10, 3, 8, 1]))         # Expected: 1
# print(find_min([-5, -2, -9, -1]))      # Expected: -9
# print(find_min([7]))                   # Expected: 7



# def array_sum(arr, index=0, total=0):
#     if len(arr) == 0 : return 0
#     if len(arr) == 1 : return arr[0]
#     if index == len(arr) :return total 
#     total = arr[index] + array_sum(arr,index+1,total)
#     return total 


# # Test Cases
# print(array_sum([1, 2, 3, 4]))      # Expected: 10
# print(array_sum([5, 10, 15]))       # Expected: 30
# print(array_sum([7]))               # Expected: 7
# print(array_sum([]))                # Expected: 0



# def count_positive(arr, index=0, count=0):
#     if index == len(arr) : return count 
#     if len(arr)  == 0 : return 0 
#     if arr[index] > 0 : count+=1 
#     return count_positive(arr,index+1,count)


# # Test Cases
# print(count_positive([1, -2, 3, -4, 5]))   # Expected: 3
# print(count_positive([-1, -2, -3]))        # Expected: 0
# print(count_positive([5, 10, 2]))          # Expected: 3
# print(count_positive([]))                  # Expected: 0
# print(count_positive([0, 1, -1]))          # Expected: 1



# def exists(arr, target, index=0):
#     if index == len(arr) or len(arr) == 0 : return False 
#     else  : return True if arr[index] == target else exists(arr,target, index+1)


# # Test Cases
# print(exists([1, 2, 3, 4], 3))      # Expected: True
# print(exists([1, 2, 3, 4], 9))      # Expected: False
# print(exists([5, 5, 7], 5))         # Expected: True
# print(exists([], 5))                # Expected: False



