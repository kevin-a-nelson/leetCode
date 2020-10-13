def searchTree(rowValues, root, row):
    if root is None:
        return 
    
    if row not in rowValues:
        rowValues[row] = []
    
    rowValues[row].append(root.val)

    if root.left:
        searchTree(rowValues, root.left, row + 1)
    if root.right:
        searchTree(rowValues, root.right, row + 1)
    


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        rowValues = {}

        searchTree(rowValues, root, 0)
        
        maxRowValues = []
        
        for row, values in rowValues.items():
            maxRowValue = max(values)
            maxRowValues.append(maxRowValue)

        return maxRowValues