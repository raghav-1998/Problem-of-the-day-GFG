#User function Template for python3
import sys
class Solution:
    # Time Complexity :- O(n);
    # Space Compleixty :- O(1);
    def maxPossibleValue(self, N, A, B): 
        #code here
        ans=0
        pv=0
        mn=sys.maxsize
        for i in range(0,N) :
            side=A[i]
            fre=B[i]//4
            ans+=(4*side*fre)
            if B[i]!=1 :
                mn = min(side,mn)
            if B[i]%4==2 or B[i]%4==3 :
                if pv==0 :
                    pv=side
                else :
                    ans+=((2*pv)+(2*side))
                    pv=0
        if pv!=0 :
            ans = max(ans,ans-2*mn+2*pv)
        return ans

#{ 

