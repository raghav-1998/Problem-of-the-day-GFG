from typing import List


class Solution:
    def bitMagic(self, n : int, arr : List[int]) -> int:
        res = 0
        for i in range(n//2):
            if arr[i]!=arr[n-1-i]: res+=1
        return (res+1)//2
