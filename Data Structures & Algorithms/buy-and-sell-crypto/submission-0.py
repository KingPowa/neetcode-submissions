class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = 1000
        min_buys = []
        for price in prices:
            min_buys.append(min(price, min_buy))
            if price < min_buy:
                min_buy = price
            if price - min_buys[-1] > max_profit:
                max_profit = price - min_buys[-1]
        return max_profit
      