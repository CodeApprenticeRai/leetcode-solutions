'''
    For every timestep the max profit is either the max profit
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        buy_price = prices[0]

        while (i + 1 < len(prices)):
            if (prices[i + 1] < prices[i]):
                profit += prices[i] - buy_price
                buy_price = prices[i + 1]
            i += 1

        if (buy_price != prices[-1]):
            profit += prices[-1] - buy_price

        return profit