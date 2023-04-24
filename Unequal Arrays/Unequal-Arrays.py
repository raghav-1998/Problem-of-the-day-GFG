from typing import List
class Solution:
    def solve(self, N : int, A : List[int], B : List[int]) -> int:
        # code here
        if sum(A)!=sum(B):
            return -1
        oa=[];ea=[]
        ob=[];eb=[]
        for i in A:
            if i%2:
                oa.append(i)
            else:
                ea.append(i)
        for i in B:
            if i%2:
                ob.append(i)
            else:
                eb.append(i)
        if len(oa)!=len(ob) or len(ea)!=len(eb):
            return -1
        oa.sort()
        ea.sort()
        ob.sort()
        eb.sort()
        ans=0
        for i in range(len(oa)):
            x=abs(oa[i]-ob[i])
            ans+=(x//2)
        for i in range(len(eb)):
            x=abs(eb[i]-ea[i])
            ans+=(x//2)
        
        return ans//2
