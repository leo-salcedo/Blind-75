def maxProfit(self, prices):
        max_profit = 0
        buy, sell = 0, 1
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit < 0:
                buy = sell
            else:
                max_profit = max(profit, max_profit)
            sell += 1
        return max_profit


# Intuition:
    # Use a two pointer/sliding window approach to find a new lowest price and calculate profits until we find a lower price to buy at.
    # This calculates the max profit.
    # Initialize our two pointers, buy and sell, to be at the first two indices in the list.
    # While sell < len(prices), calculate the profit by subtracting the price at buy from the price at sell.
    # If the profit is < 0, this means we have found a new lowest price to buy at. Set buy equal to sell, shrinking the window.
    # Otherwise, update the max profit accordingly.
    # Then, increment sell to expand the window.

# Time complexity: O(n)
# Space complexity: O(1)