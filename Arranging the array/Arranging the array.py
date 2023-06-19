
from typing import List


class Solution:
    def Rearrange(self, n : int, arr : List[int]) -> None:
        # code here
        a = []
        m = []
        for i in range(n):
            if arr[i] >=0:
                a.append(arr[i])
            elif arr[i] <0:
                m.append(arr[i])
        m.extend(a)
        for j in range(n):
            arr.pop()
        arr.extend(m)
        return m
        

