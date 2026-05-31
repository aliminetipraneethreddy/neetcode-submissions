class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=[0]*len(prices)
        min1 =max(prices)
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit=prices[i]-prices[j]
                if profit>0:
                    a.append(profit)
                else:
                    a.append(0)
        return max(a)

            
        