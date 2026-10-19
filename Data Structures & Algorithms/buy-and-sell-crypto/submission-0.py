class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buyin = float('inf')
        for p in prices:
            min_buyin = min(p, min_buyin)
            profit = p - min_buyin
            max_profit = max(max_profit, profit)

        return max_profit