from TreeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def dfs(self, t1, t2):
        
        if t1 is None and t2 is None:
            return None
        
        if t1 is None:
            return t2
        
        if t2 is None:
            return t1
        
        root = TreeNode(t1.val + t2.val)
        root.left = self.dfs(t1.left, t2.left)
        root.right = self.dfs(t1.right, t2.right)
        
        return root

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        
        if t1 is None:
            return t2
        
        if t2 is None:
            return t1
        
        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        
        return root
        