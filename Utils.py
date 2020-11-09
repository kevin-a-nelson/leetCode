from ListNode import ListNode

def copy_list(head):
    if head is None:
        return head
    
    # Create a new node
    new_node = ListNode(head.val)
    # The new nodes next pointer would point to the node returned from recursion
    # i.e. the next new node.
    new_node.next = copy_list(head.next)
    
    return new_node

curr = copy_list(ListNode().createListNodes([1,2,3,4,5]))

def printListNode(listNode, msg = ""):
    if listNode is None:
        return listNode
    
    listNodeValues = []

    curr = copy_list(listNode)

    # while curr:
    #     listNodeValues.append(curr.val)
    #     curr = curr.next
    
    print(f"{msg} {listNodeValues}")
    

