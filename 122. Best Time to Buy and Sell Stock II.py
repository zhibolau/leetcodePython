class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        l=len(prices)
        total = 0
        for i in range(1,l):
            if prices[i]>prices[i-1]:
                total += prices[i]-prices[i-1]
        return total
"""
只要有利润就加起来
"""