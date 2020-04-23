"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:    
    
    def flatten(self, head: 'Node') -> 'Node':

        # stack 
        # prev
        # current
        # next
        
        if not head:
            return
        
        stack = [head]
        
        seudoHead = Node(0, None, None, None)
        
        prev = seudoHead
        
        while stack:
            
            current = stack.pop()
            
            prev.next = current
            current.prev = prev
            
            if current.next:
                stack.append(current.next)
            
            if current.child:
                stack.append(current.child)
                current.child = None
            
            prev = current
        
        seudoHead.next.prev = None
        return seudoHead.next
    
        
        
        
        
        
        