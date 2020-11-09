from ListNode import ListNode



class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1

nums = [i for i in range(100)]
target = 60
        
solution = Solution().search(nums, target)

print(solution)