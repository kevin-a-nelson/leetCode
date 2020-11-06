import copy

def climbStairsHelper(allSteps, steps):

    tempSteps = steps

    return allSteps






class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        allSteps = []
        steps = [1 for i in range(1, n + 1)]
        climbStairsHelper(allSteps, steps)
        print(allSteps)


solution = Solution()

solution.climbStairs(5)