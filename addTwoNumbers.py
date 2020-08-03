class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode(0)
        
        head = node
        
        carry = 0
        
        while l1 or l2 or carry > 0:
            
            l1_val = (l1.val if l1 else 0)
            l2_val = (l2.val if l2 else 0)            
            
            sum = l1_val + l2_val + carry
            remainder = sum % 10
            carry = sum // 10
            node.next = ListNode(remainder)
            
            node = node.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None) 
            

        return head.next
    
#    99
#  + 99
#------------
#    

# NICK WHITE