from typing import List

class Solution:
    def finLength(self, N: int, color: List[int], radius: List[int]) -> int:
        stk = [[color[0], radius[0]]]
        for i in range(1, N):
            if len(stk) > 0:
                if stk[-1][0] == color[i] and stk[-1][1] == radius[i]:
                    stk.pop()
                else:
                    stk.append([color[i], radius[i]])
            else:
                stk.append([color[i], radius[i]])
        return len(stk)
