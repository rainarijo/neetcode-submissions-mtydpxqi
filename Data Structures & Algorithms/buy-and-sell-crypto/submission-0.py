class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max=-1
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                profit=prices[j]-prices[i]

                if profit>max:
                    max=profit
                
        if max>0:
            return max
        else:
            return 0