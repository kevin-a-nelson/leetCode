class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        visitedNums = set()
        duplicateNums = set()
        
        for num in nums:
            if num in visitedNums:
                duplicateNums.add(num)
            else:
                visitedNums.add(num)
        
        return duplicateNums
        
