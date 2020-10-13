class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # while num is less than n
        # increment num by power of two
        # if num equals n return true
        # if num is ever greater than n return false

        if n == 1:
            return True
        
        num = 1
        power = 0
        while num < n:
            num = 2 ** power
            if num == n:
                return True
            elif num > n:
                return False
            power += 1
        


solution = Solution()


print(solution.isPowerOfTwo(20))
        