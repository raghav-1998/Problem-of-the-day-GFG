#User function Template for python3


class Solution:
    def isPossible(self, n, m, s):
        x,y = 0,0
        ml,mr,mu,md = 0,0,0,0
        for c in s:
            if c=='L':
                x-=1
            elif c=='R':
                x+=1
            elif c=='U':
                y-=1
            else:
                y+=1
            ml = min(ml,x)
            mr = max(mr,x)
            mu = min(mu,y)
            md = max(md,y)
        
        if abs(ml)+mr<m and abs(mu)+md<n:
            return 1
        return 0   

