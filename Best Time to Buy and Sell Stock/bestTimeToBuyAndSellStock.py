class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i, j = 0, 1
        maxProfit = 0

        while j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxProfit = max(maxProfit,profit)
            else:
                i = j
            j += 1

        return maxProfit
