from ListNode import ListNode
from Utils import printListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        curr = head.next
        prev = head
        
        while curr:
            temp = curr.next
            print("=" * 20)
            printListNode(curr, "curr")
            printListNode(prev, "prev")
            printListNode(temp, "temp")
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
            
        
solution = Solution().reverseList(ListNode().createListNodes([1,2,3,4,5]))