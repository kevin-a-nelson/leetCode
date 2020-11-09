from ListNode import ListNode

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head
        
        curr = head.next
        prev = head

        while curr:
            print(f"curr {curr.toList()}")
            print(f"prev {prev.toList()}")
            print(f"head {head.toList()}")
            if curr.val == prev.val:
                prev.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
                prev = prev.next
        
        return head

listNodes1 = ListNode().createListNodes([1,1,1,1,2,2,2,2])

solution1 = Solution().deleteDuplicates(listNodes1)

print(solution1.toList())
        
             
        