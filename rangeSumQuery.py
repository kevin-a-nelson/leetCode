class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.runningSums = self.getRunningSums(nums)

    def getRunningSums(self, nums):
        sums = []
        sums.append(nums[0])

        for i in range(1, len(nums)):
            sums.append(sums[i - 1] + nums[i])

        return sums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        print(self.runningSums)

        return self.runningSums[j] - self.runningSums[i]


numArray = NumArray([-2, 0, 3, -5, 2, -1])
numArray.sumRange(0, 2) 
numArray.sumRange(2, 5) 
numArray.sumRange(0, 5) 