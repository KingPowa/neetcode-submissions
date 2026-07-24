class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = 1000
        for price in prices:
            min_buy = min(price, min_buy)
            max_profit = max(max_profit, price - min_buy)
        return max_profit
      