
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def strLink(self):
        return f"{self.val} -> {self.next}"
    
    def toList(self):

        nodeValues = []
        nodeValues.append(self.val)

        while(self.next):
            self = self.next
            nodeValues.append(self.val)

        return nodeValues
    
    def createListNodes(self, values):

        if not values:
            return

        head = self
        self.val = values[0]

        for idx, value in enumerate(values):
            self.val = value
            
            if idx == len(values) - 1:
                continue
                
            self.next = ListNode()
            self = self.next
        
        return head


    


