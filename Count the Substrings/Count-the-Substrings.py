#User function Template for python3
class Solution:
    def countSubstring(self, S): 
        res=0
        for i in range(0,len(S)):
            l=0
            u=0
            for j in range(i,len(S)):
                if(S[j]>='a' and S[j]<='z'):
                    l=l+1
                
                else:
                    u=u+1
                if(l==u):
                    res=res+1
                
        return res
    