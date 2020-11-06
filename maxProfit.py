class Solution(object):
    def maxProfit(self, prices):

        minPrice = float('inf')
        maxProfit = 0

        for price in prices:
            profit = price - minPrice
            if price < minPrice:
                minPrice = price
            elif profit > maxProfit:
                maxProfit = profit
        
        return maxProfit


ans = Solution().maxProfit([7,1,5,3,6,4])