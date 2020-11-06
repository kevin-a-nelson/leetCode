class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        dp = {1: 1, 2: 2}

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

solution = Solution()

solution.climbStairs(5)