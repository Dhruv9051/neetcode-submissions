class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left=buy right=sell
        maxProfit = 0

        while r < len(prices):
            # profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r #shift l to r since we found the lowest from the current
            r += 1 #shift r irrespective
        return maxProfit