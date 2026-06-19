class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff=0
        for i in range(0,len(prices)-1):
            maxval=max(maxDiff, max(prices[i+1:len(prices)]))
            maxDiff=max(maxDiff, maxval-prices[i])
        return maxDiff

        