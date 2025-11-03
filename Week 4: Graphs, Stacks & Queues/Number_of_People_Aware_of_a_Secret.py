class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(1, n + 1):
            for j in range(i + delay, min(n + 1, i + forget)):
                dp[j] = (dp[j] + dp[i]) % MOD

       
        result = sum(dp[n - forget + 1: n + 1]) % MOD
        return result
