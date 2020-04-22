def maxSubArray(nums: 'List[int]') -> 'int':
    
    curr_sum = nums[0]
    max_sum = nums[0]

    for idx in range(1, len(nums)):
        num = nums[idx]
        possible_curr_sum = curr_sum + nums[idx]
        curr_sum = max(num, possible_curr_sum)
        max_sum = max(max_sum, curr_sum)
        
    return max_sum