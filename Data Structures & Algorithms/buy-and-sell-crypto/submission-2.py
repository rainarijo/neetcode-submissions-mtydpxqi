class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        minp=prices[0]

        for sell in prices:
            maxp=max(maxp,sell-minp)
            minp=min(minp,sell)
        return maxp
