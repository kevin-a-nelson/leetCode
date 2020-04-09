
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    mapping = {}
    for idx, num in enumerate(nums):
        if target - num in mapping:
            return [mapping[target - num], idx]
        mapping[num] = idx
    return [-1, -1]


# print(twoSum([2, 7, 11, 15], 9))
# print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
    
    
    