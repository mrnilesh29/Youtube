# def reverse_string(s,i=None,rev=""):
#     if i is None : 
#         i = len(s)-1
#     if i < 0 :return rev 
#     rev += s[i]
#     return reverse_string(s,i-1,rev)
        
        
        

# # Test Cases
# print(reverse_string("hello"))       # Expected: "olleh"
# print(reverse_string("python"))      # Expected: "nohtyp"
# print(reverse_string("a"))           # Expected: "a"
# print(reverse_string(""))             # Expected: ""



# def remove_char(s, target, index=0, result=""):
#     if len(s) == 0 or index < 0 or index == len(s) :return result 

#     if s[index] != target : 
#         result+=s[index]
#     return remove_char(s,target,index+1,result)


# # Test Cases
# print(remove_char("banana", "a"))       # Expected: "bnn"
# print(remove_char("hello", "l"))        # Expected: "heo"
# print(remove_char("python", "x"))       # Expected: "python"
# print(remove_char("", "a"))             # Expected: ""



def is_palindrome(s, left=0, right=None):
    if right is None : right = len(s)-1
    if len(s) == 0 or len(s) == 1 : return True 
    if left > right : return True 
    if s[left] != s[right] : return False 
    return is_palindrome(s,left+1,right-1)

    


# Test Cases
print(is_palindrome("madam"))     # Expected: True
print(is_palindrome("racecar"))   # Expected: True
print(is_palindrome("hello"))     # Expected: False
print(is_palindrome("abba"))      # Expected: True
print(is_palindrome(""))          # Expected: True