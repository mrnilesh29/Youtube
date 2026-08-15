class Stack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        # your code
        return self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]


    def is_empty(self):
        return len(self.stack) == 0 
    
    def size(self) : 
        return len(self.stack)
    
    
    def is_full(self , stack, capacity):
        return len(self.stack) == capacity 
    
        
    def display(stack):
        for i in stack : 
            print(i)
            
            
     
     
     
      # your code
# s = Stack()

# s.push(10)
# s.push(20)
# s.push(30)

# print(s.peek())
# print(s.pop())
# print(s.peek())
# print(s.is_empty())










# def reverse_string(name:str) : 
#     st2 : Stack = Stack()
#     for i in name : 
#         st2.push(i)
    
#     rev = ""
#     while not st2.is_empty() :
#         x = st2.peek()
#         rev += x 
#         st2.pop()
        
#     return rev 



# print(reverse_string("hello"))








# def is_palindrome(s: str):
#     rev = ""
#     st : Stack = Stack() 
    
#     for i in s : 
#         st.push(i) 
        
    
#     while not st.is_empty() : 
#         x = st.peek() 
#         rev +=  x 
#         st.pop()
    
#     if rev == s : 
#         return True 
#     else : 
#         return False
    
        




# print(is_palindrome("madam"))
# print(is_palindrome("hello"))
# print(is_palindrome("racecar"))





def reverse_array(arr):
    st:Stack = Stack()
    arr2 = []
    for i in arr : 
        st.push(i) 
        
    while not st.is_empty() :
        top = st.peek()
        arr2.append(top) 
        st.pop()
    
    return arr2
        
        
        
    