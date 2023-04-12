class Solution:
    def minSteps(self, s : str) -> int:
        # code here
        temp=""
        for i in range(len(s)):
            if len(temp)==0 or temp[len(temp)-1]!=s[i]:
                temp+=s[i]
        return len(temp)//2 +1
