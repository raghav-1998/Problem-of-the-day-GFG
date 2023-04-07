from typing import List


class Solution:
    def minimumInteger(self, N : int, A : List[int]) -> int:
        # code here
        A.sort()
        tot=sum(A)
        for i in A:
            if(tot<=N*i):
                mini=i
                break
        return mini