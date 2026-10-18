class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = []
        for n in nums:
            if len(prefix_products) == 0:
                prefix_products.append(n)
            else:
                prefix_products.append(prefix_products[-1] * n)
        suffix_products = []
        for n in reversed(nums):
            if len(suffix_products) == 0:
                suffix_products.append(n)
            else:
                suffix_products.append(suffix_products[-1] * n)
        suffix_products = list(reversed(suffix_products))
        
        result = []
        for i, n in enumerate(nums):
            if i == 0:
                result.append(suffix_products[1])
            elif i == len(nums) - 1:
                result.append(prefix_products[len(nums) - 2])
            else:
                result.append(prefix_products[i - 1] * suffix_products[i + 1])

        return result
        