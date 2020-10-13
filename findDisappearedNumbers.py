class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return []

        maxNum = max(nums)

        numsHasNum = {}

        for i in range(1, len(nums) + 1):
            numsHasNum[i] = False
        
        for num in nums:
            numsHasNum[num] = True
        
        disappearedNumbers = []

        for num, hasNum in numsHasNum.items():
            if not hasNum:
                disappearedNumbers.append(num)
        
        return disappearedNumbers
        



        

solution = Solution()

answer = solution.findDisappearedNumbers([4,3,2,7,8,2,3,1])

print(answer)