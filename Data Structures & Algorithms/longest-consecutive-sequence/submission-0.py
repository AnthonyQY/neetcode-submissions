class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for n in seen:
            if n - 1 not in seen:
                right = n
                while right + 1 in seen:
                    right += 1
                
                longest = max(longest, right - n + 1)
        return longest