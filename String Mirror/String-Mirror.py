import copy
class Solution:
    def stringMirror(self, s : str) -> str:
        # code here
        res=[s[0]];prev=[s[0]]
        for i in range(1,len(s)):
            res.append(s[i])
            temp=res[::-1]
            v1=res+temp
            temp2=prev[::-1]
            v2=prev+temp2
            if v1<=v2:
                prev=res.copy()
            else:
                return ''.join(prev+prev[::-1])
        return ''.join(res+res[::-1])

