#User function Template for python3

class Solution:
    def klengthpref(self,arr,n,k,s):
        if k>len(s):
            return 0
        count=0
        for e in arr:
            if s[:k]==e[:k]:
                count+=1
        return count