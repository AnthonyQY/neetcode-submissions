class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        target_index = -1

        while left <= right:
            midpoint = (left + right) // 2

            if nums[midpoint] == target:
                target_index = midpoint
            
            if nums[midpoint] < target:
                left = midpoint + 1
            else:
                right = midpoint - 1

        return target_index