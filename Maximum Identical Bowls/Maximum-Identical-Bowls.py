
from typing import List
class Solution:
    def getMaximum(self, N : int, arr : List[int]) -> int:
        s=sum(arr)
        for i in range(N,0,-1):
            if s%i==0:
                m=i
                break
        return m        

