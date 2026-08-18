class stack : 
    def __init__(self):
        self.arr = []
        
    def push(self,val) : 
        self.arr.append(val)
        
    def printstack(self) : 
        print(self.arr)
        
    def pop(self) : 
        self.arr.pop()
        
        
    
obj = stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(40)
obj.pop()

obj.printstack()
