#User function Template for python3

from typing import List

class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        # code here
        answer = []
        for i in arr:
            if len(answer) == 0:
                answer.append(i)
            elif (answer[-1] >= 0 and i < 0) or (answer[-1] < 0 and i >= 0):
                answer.pop()
            else:
                answer.append(i)
        return answer