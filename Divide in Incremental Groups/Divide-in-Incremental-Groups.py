#User function Template for python3

class Solution:
    def countWaystoDivide(self, N, K):
        a=[]
        for i in range(1,N+1):
            a.append(i)
        n=N
        k=K
        dp=[]
        for i in range(N+1):
            c=[]
            for j in range(N+1):
                d=[]
                for k in range(k+1):
                    d.append(-1)
                c.append(d)
            dp.append(c)
            
        def coin(i,su,a1):
            if(su==n):
                if(a1==k):
                    return 1
                else:
                    return 0
            if(su>n or i>=n or a1>k):
                return 0
            if(dp[i][su][a1]!=-1):
                return dp[i][su][a1]
            a3=coin(i,su+a[i],a1+1)
            a2=coin(i+1,su,a1)
            dp[i][su][a1]=(a3+a2)
            return dp[i][su][a1]
        return(coin(0,0,0))


