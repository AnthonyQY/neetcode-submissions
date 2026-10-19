class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        results = []
        for i, n in enumerate(nums):
            x = n
            if i > 0 and x == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right] + x
                if current_sum == 0:
                    results.append([x, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and  nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1

        return results
