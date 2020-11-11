class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def dfs(self, root, acc, level = 0):

        if root is None:
            return
        
        if level not in acc:
            acc[level] = []
        
        acc[level].append(root.val)
        
        self.dfs(root.left, acc, level + 1)
        self.dfs(root.right, acc, level + 1)

    def toList(self):

        acc = {}
        self.dfs(self, acc)

        print(acc)
        treeNodeList = []

        for level, values in sorted(acc.items()):
            for value in values:
                treeNodeList.append(value)

        return treeNodeList
    
    def createRightTreeNodes(self, root, values):

        if values == []:
            return
        
        if len(values) >= 3:
            root.right = TreeNode(values[2])
        else:
            root.right = None
        
        if len(values) >= 4:
            root.right = TreeNode(values[3])
        else:
            root.right = None


        self.createRightTreeNodes(root.right, values[4:])

    def createLeftTreeNodes(self, root, values):

        if values == []:
            return

        if len(values) >= 1:
            root.left = TreeNode(values[0])
        else:
            root.left = None
        
        if len(values) >= 2:
            root.left = TreeNode(values[1])
        else:
            root.left = None

        self.createLeftTreeNodes(root.left, values[4:])

    def createTreeNodes(self, values):

        if values == []:
            return

        root = TreeNode(values[0])
        root.left = TreeNode(values[1])
        root.right = TreeNode(values[2])

        self.createLeftTreeNodes(root.left, values[3:])
        self.createRightTreeNodes(root.right, values[3:])

        return root

ans = TreeNode().createTreeNodes([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]).toList()

print(ans)


#       3
#      / \
#     9   20
#         / \  
#        15  7