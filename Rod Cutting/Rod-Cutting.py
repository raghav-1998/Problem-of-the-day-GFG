#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        dp = [0] * (n+1)
        
        for i in range(1,n+1):
            dp[i] = price[i-1]
            for num in range( 1, i+1):
                dp[i] = max(dp[i], dp[num]+dp[i-num])
        return dp[-1]




