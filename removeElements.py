from ListNode import ListNode

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        prev = ListNode(0)
        prev.next = head
        root = prev
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

        return root.next

listNodes1 = ListNode().createListNodes([1,2,3,3,3,4,5])
listNodes2 = ListNode().createListNodes([1])

solution1 = Solution().removeElements(listNodes1, 3)
solution2 = Solution().removeElements(listNodes2, 1)

print(solution2 == None)
print(solution1.toList())
