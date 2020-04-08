
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for idx1, num1 in enumerate(nums):
        for idx2, num2 in enumerate(nums):
            if(num1 + num2 == target and idx1 != idx2):
                return [idx1, idx2]


# print(twoSum([2, 7, 11, 15], 9))
# print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
    
    
    