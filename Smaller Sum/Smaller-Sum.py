from typing import List


class Solution:
    def smallerSum(self, n : int, arr : List[int]) -> List[int]:
        # code here
        d={}
        ind=0
        for i in arr:
            if(i in d):
                d[i].append(ind)
            else:
                d[i]=[ind]
            ind+=1
        res=[0 for i in range(n)]
        prev=0
        for i in sorted(d.keys()):
            for j in d[i]:
                res[j]=prev
            prev+=(i*len(d[i]))
        return res