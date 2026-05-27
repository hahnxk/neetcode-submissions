class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Idea: 
        # Initialize profit as 0
        # 1. Loop through prices
        # 2. Initialize buy (day 1 price) and compare profit to diff between day 
        #    1 and following days.
        # 3. If new day has lower cost than current lowest day, swap and go back to step 1.
        # 4. Repeat.
        profit = 0
        buy = prices[0]
        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit
