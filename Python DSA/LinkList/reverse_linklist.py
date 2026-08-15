class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head is None : 
            return None 
        if head.next is None : 
            return head

        prev = None 
        curr = head 
        
        while curr.next is not None : 
            temp = curr.next 
            curr.next = prev 
            prev = curr
            curr = temp 
        curr.next = prev
        return curr

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        
        
A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
D = ListNode(4)
E = ListNode(5)

A.next = B
B.next = C
C.next = D
D.next = E 
E.next = None 

head = A 

obj = Solution()
obj.reverseList(head) 