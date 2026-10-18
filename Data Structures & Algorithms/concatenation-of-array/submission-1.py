class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = [0] * 2 * len(nums)

        for i, n in enumerate(nums):
            result[i] = n
            result[i + len(nums)] = n

        return result