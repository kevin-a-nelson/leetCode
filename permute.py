class Solution:
    def permute(self, nums):
        
        def backtrace(start = 0):
            
            if start == len(nums):
                permutations.append(list(nums))
                return 
            
            for idx in range(start, len(nums)):
                nums[start], nums[idx] = nums[idx], nums[start]
                backtrace(start + 1)
                nums[idx], nums[start] = nums[start], nums[idx]
        
        permutations = []
        backtrace()
        return permutations
    
# start = 0
# idx   = 0
# [1,2,3]

    # start = 1
    # idx   = 1
    # [1, 2, 3]
    
        # start = 2
        # idx   = 2
        # [1, 2, 3]     RETURN
        
    # start = 1
    # idx   = 2
    # [1, 3, 2]
    
        # start = 2
        # idx   = 2
        # [1, 3, 2]     RETURN

# start = 0
# idx   = 1
# [2, 1, 3]

    # start = 1
    # idx   = 1
    # [2, 1, 3]
    
        # start = 2
        # idx   = 2
        # [2, 1, 3]     RETURN 
    
    # start = 1
    # idx   = 2
    # [2, 3, 1]
    
        # start = 2
        # idx   = 2
        # [2, 3, 1]     RETURN
    
# start = 0
# idx   = 2
# [3, 2, 1]

    # start = 1
    # idx   = 1
    # [3, 2, 1]
    
        # start = 2
        # idx   = 2
        # [3, 2, 1]     RETURN
    
    # start = 1
    # idx   = 2
    # [3, 1, 2]
        
        # start = 2
        # idx   = 2
        # [3, 1, 2]     RETURN 
        
