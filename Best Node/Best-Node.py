from typing import List


class Solution:
    def bestNode(self, N : int, A : List[int], P : List[int]) -> int:
        from collections import defaultdict
        g = defaultdict(list)
        for i, parent in enumerate(P):
            g[parent].append(i+1)
            
     
        ans = float('-inf')
        def dfs(n):
            nonlocal g, ans, A
            if not g[n]:
                ans = max(ans, A[n-1])
                return A[n-1], A[n-1]
            
            maxv, minv = float('-inf'), float('inf')
            for nxt in g[n]:
                ma, mi = dfs(nxt)
                maxv = max(maxv, A[n-1]-mi)
                minv = min(minv, A[n-1]-ma)
            ans = max(ans, maxv)
            return maxv, minv
        
        dfs(1)
        return ans

