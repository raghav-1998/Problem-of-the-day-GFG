#User function Template for python3

class Solution:
    def addMinChar (self, str1):
        # code here 
        ans=0
        l=0
        r=len(str1)-1
        
        while(l<=r):
            if(str1[l]==str1[r]):
                l+=1
                r-=1
            else:
                ans+=1
                l=0
                r=len(str1)-1-ans
        
        return ans
