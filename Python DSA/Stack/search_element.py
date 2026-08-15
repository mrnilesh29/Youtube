class Solution:

    def search(self, stack, target):
        while not stack.is_empty() :
            if stack.peek() == target : 
                return True 
            stack.pop()
            
        return False 
     
            
        
        
        
        
        
        def is_empty(self) : 
            return len(self.st) == 0 
        
        
        