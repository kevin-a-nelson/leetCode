class Solution(object):
    def maxSubArray(self, nums):
        # keep track of dp
        # 
        dp = []

        dp.append(nums[0])

        for i in range(1, len(nums)):
            dp.append(max(dp[i - 1] + nums[i], nums[i]))
        
        return max(dp)





Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])