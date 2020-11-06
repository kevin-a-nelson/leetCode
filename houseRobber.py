class Solution(object):
    def rob(self, nums):
        if len(nums) == 0 or nums is None:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        runningTotal = {}
        runningTotal[0] = nums[0]
        runningTotal[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            runningTotal[i] = max(nums[i] + runningTotal[i - 2], runningTotal[i - 1])
        
        return runningTotal[len(runningTotal) - 1]


solution = Solution()

ans = solution.rob([2,7,9,3,1])