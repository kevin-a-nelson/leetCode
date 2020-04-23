
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result = ListNode(0)
    result_tail = result
    carry = 0
            
    while l1 or l2 or carry:            
        val1  = (l1.val if l1 else 0)
        val2  = (l2.val if l2 else 0)
        carry, out = divmod(val1+val2 + carry, 10)    
                    
        result_tail.next = ListNode(out)
        result_tail = result_tail.next                      
        
        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)
            
    return result.next

def createListNode(arr):
    head = ListNode(arr[0])
    arr = arr[1:]
    node = head
    for val in arr:
        node.next = ListNode(val)
        node = node.next
    return head

l1 = createListNode([2, 4, 3])
l2 = createListNode([5, 6, 4])

l3 = addTwoNumbers(l1, l2)


        
