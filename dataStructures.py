
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def createLeftTreeNodes(self, root, values):

        if values == []:
            return 

        root.left = TreeNode(values[2])
        root.right = TreeNode(values[3])

        self.createLeftTreeNodes(root.right, values[3:])

    def createRightTreeNodes(self, root, values):

        if values == []:
            return

        root.left = TreeNode(values[4]) 
        root.right = TreeNode(values[5])

        self.createRightTreeNodes(root.right, values[3:])


    
    def createTreeNodes(self, values):

        if values == []:
            return

        root = TreeNode(values[0])
        root.left = TreeNode(values[1])
        root.right = TreeNode(values[2])

        self.createLeftTreeNodes(root.left, values[2:])
        self.createRightTreeNodes(root.right, values[2:])

        return

TreeNode().createTreeNodes([3,9,20,None,None,15,7])

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


    


