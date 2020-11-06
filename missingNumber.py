class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)

        for idx, num in enumerate(nums):
            if idx != num:
                return idx
        return -1

solution = Solution()

answer = solution.missingNumber([0,1,2,3,5])

print(answer)
        
        
        