# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        def maxDepth(start=root):
            if start is None:
                return 0
            
            left = 1 + maxDepth(start.left)
            right = 1 + maxDepth(start.right)
            
            paths.append(left + right - 2)
            return max(left, right)
        
        paths = []
        maxDepth()

        return max(paths)  