class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = sys.maxsize
        total = 0
        for x in prices:
            if x < low:
                low = x
            if x - low > total:
                total = x - low
        return total

"""
更新最低价格和 最大利润
"""