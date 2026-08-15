class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None

    def push(self, x):
        new_node = Node(x)

        new_node.next = self.top
        self.top = new_node

    def pop(self):

        if self.top is None:
            return "Stack is Empty"

        value = self.top.data
        self.top = self.top.next

        return value

    def peek(self):

        if self.top is None:
            return "Stack is Empty"

        return self.top.data

    def is_empty(self):
        return self.top is None
    
        
        
        
 




s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.peek())
print(s.pop())
print(s.peek())
print(s.is_empty())

