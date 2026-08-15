class Linklist:
    def __init__(self,val):
        self.val = val 
        self.next = None 
          
          
          
def printLinklist(head) :
    temp :Linklist = head 
    while temp != None : 
        print(temp.val)
        temp = temp.next 
        
        
def count_Nodes(head) : 
    temp : Linklist = head 
    count = 0 
    while temp is not None:
        count +=1 
        temp = temp.next 
    return count

def search_node(head, key):
    temp:Linklist = head
    while temp is not None :
        if temp.val == key: 
            return True 
        else :temp = temp.next 
    
    return False 

def insert_at_beginning(head, value):
    newNode :Linklist = Linklist(value) 
    newNode.next = head 
    head = newNode 
    return head


def insert_at_end(head, value):
    node : Linklist = Linklist(value)
    if head is None : 
        head = node
        return head 
    
    temp : Linklist = head 
   
    while temp.next is not None : 
        temp = temp.next 
        
    temp.next = node
    return head 


def insert_at_position(head, value, position):
    new_node:Linklist = Linklist(value )
    temp : Linklist = head
    if position == 1 : 
        new:Linklist = insert_at_beginning(head=head,value=value)
        return new
    
    for i in range(1,position-1):
        temp = temp.next 
        if temp is None : 
            return head 
    new_node.next = temp.next 
    temp.next = new_node 
    return head                         
            

def delete_first(head):
    if head is None :
        return None 
    head = head.next 
    return head
        
def delete_last(head):
    
    if head is None : 
        return None 
    if head.next is None: 
        return head 
    
    temp :Linklist = head 
    while temp.next.next is not None : 
        temp = temp.next
        
    temp.next = None 
    return head


def delete_by_value(head, value):
    if head is None :
        return None 
    
    if head.val == value : 
        return head.next
    
    temp : Linklist = head 
    while temp.next is not None :
        
        if temp.next.val == value : 
            temp.next = temp.next.next
            return head 
        
        temp = temp.next
        
    return head
         
            
   
A:Linklist = Linklist(10)
B:Linklist = Linklist(20)
C:Linklist = Linklist(30)
D:Linklist = Linklist(40)


A.next = B
B.next = C 
C.next = D

head = A 

head = insert_at_beginning(head , 100)
printLinklist(head)

insert_at_position(head,200,2)
printLinklist(head)


