from ListNode import ListNode

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        prev = ListNode()
        prev.next = head
        root = prev
        trav = head

        while trav:
            if trav.val == val:
                prev.next = trav.next
                trav = trav.next
            else:
                prev = trav
                trav = trav.next

        return root.next

# listNodes1 = ListNode().createListNodes([1,2,3,3,3,4,5])
listNodes2 = ListNode().createListNodes([1,1,1,1,1])

# solution1 = Solution().removeElements(listNodes1, 3)
solution2 = Solution().removeElements(listNodes2, 1)

print(solution2)
print(solution1.toList())
