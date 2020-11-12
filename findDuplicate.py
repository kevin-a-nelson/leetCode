class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        visitedNums = set()
        
        for num in nums:
            if num in visitedNums:
                return num
            else:
                visitedNums.add(num)
        
        return -1
            
        
