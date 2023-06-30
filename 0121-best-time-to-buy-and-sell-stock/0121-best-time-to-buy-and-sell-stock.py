class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = max(prices)
        maxProfit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit
            