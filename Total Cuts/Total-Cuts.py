from typing import List


class Solution:
    def totalCuts(self, N : int, K : int, A : List[int]) -> int:
        # code here
        if N==1:
            return 0
        l=[A[0]]
        r=[A[-1]]
        maxi = A[0]
        for i in range(1,N-1):    
            maxi=max(maxi,A[i])
            l.append(maxi)
        mini=A[-1]
        for i in range(N-2,0,-1):
            mini=min(mini,A[i])
            r.append(mini)
        r=r[::-1]
        c=0
        for i in range(len(l)):
            if l[i]+r[i]>=K:
                c+=1
        return c
        

