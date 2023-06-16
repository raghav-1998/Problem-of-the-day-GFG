#User function Template for python3
class Solution:
    def leastPrimeFactor (self, n):
        # code here 
        prime=[-1]*(n+1)
        prime[0]=0
        prime[1]=1
        
        for i in range(2,n+1):
            if(prime[i]==-1):
                for j in range(i,n+1,i):
                    if(prime[j]==-1):
                        prime[j]=i
        
        return prime