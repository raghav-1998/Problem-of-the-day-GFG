from typing import List

class Solution:

    def solve(self, N : int, p : List[int]) -> int:

        # code here

        ans=N-1
        degree=[0]*(N+1)
        
        for i in range(1,N):
            degree[p[i]]+=1
            degree[i]+=1
            
        for i in range(N):
            if(degree[i]==1):
                ans-=1
        
        if(ans<0):
            return 0
        
        return ans
            
