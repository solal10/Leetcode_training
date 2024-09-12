class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max=0
        min_price=float('inf')
        for price in prices:
            min_price=min(min_price,price)
            profit=price-min_price
            current_max=max(profit,current_max)
        return current_max