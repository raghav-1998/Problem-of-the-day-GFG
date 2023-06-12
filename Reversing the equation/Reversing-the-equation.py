class Solution:
    def reverseEqn(self,s):
        char=["+","-","*","/"]
        ans=[]
        length=len(s)-1
        j=length+1
        for i in range(length,-1,-1):
            if s[i] in char:
                # return s[i+1:j+1]
                ans.append(s[i+1:j])
                ans.append(s[i])
                j=i
            if i==0:
                ans.append(s[:j])
        return "".join(ans)