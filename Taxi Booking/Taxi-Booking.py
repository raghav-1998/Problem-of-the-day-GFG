from typing import List


class Solution:
    def minimumTime(self, N : int, cur : int, pos : List[int], time : List[int]) -> int:
        # code here
        ans = min([abs(x - cur)*t for x,t in list(zip(pos,time))])
        return ans
