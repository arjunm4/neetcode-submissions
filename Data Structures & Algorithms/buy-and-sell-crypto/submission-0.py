class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = float('inf')

        for i in range(0, len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
                continue
            else:
                profit = prices[i] - buy_price
                max_profit = max(max_profit, profit)
        
        return max_profit