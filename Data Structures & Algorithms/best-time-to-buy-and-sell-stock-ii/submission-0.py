class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0  # Initialize a counter to keep track of total gains

        # We start the loop at index 1 (the second day) 
        # because we need to compare "today" with "yesterday"
        for i in range(1, len(prices)):
            
            # Check if the current price is higher than the previous day
            if prices[i] > prices[i - 1]:
                
                # If it is, "virtually" buy yesterday and sell today
                # Add that difference to our total profit
                profit += (prices[i] - prices[i - 1])

        return profit