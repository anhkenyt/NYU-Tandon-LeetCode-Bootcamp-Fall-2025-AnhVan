class Solution(object):
    def coinChange(self, coins, amount):
        # Initialize dp. dp[x] = minimum
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
       
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] = min(dp[a], dp[a - coin] + 1)
        
        
        return dp[amount] if dp[amount] != float('inf') else -1
