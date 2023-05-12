from typing import List


class Solution:
    def maxCoins(self, n: int, ranges: List[List[int]]) -> int:
        ranges.sort()
        mx = [0] * (n+1)

        cnt = -1
        mx[n] = 0
        for i in range(n-1, -1, -1):
            cnt = max(cnt, ranges[i][2])
            mx[i] = cnt

        ans = -1
        for i in range(n):
            sec = ranges[i][1]
            l, h = i + 1, n - 1
            while (l <= h):
                m = l + (h - l) // 2
                if ranges[m][0] < sec:
                    l = m + 1
                else:
                    h = m - 1
            ans = max(ans, ranges[i][2] + mx[l])

        return ans


