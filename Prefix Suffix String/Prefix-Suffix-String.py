#User function Template for python3

class Solution:
    def prefixSuffixString(self, s1, s2) -> int:
        #code here
        ans = 0
        i=0
        j=0
        m=len(s1)
        n=len(s2)
        while(i<m and j<n):
            if s2[j] in s1[i]:
                l = len(s2[j])
                if s2[j]==s1[i][:l] or s2[j]==s1[i][-l:]:
                    ans+=1
                    i=0
                    j+=1
                else: i+=1
            else: i+=1
        return ans
        
    