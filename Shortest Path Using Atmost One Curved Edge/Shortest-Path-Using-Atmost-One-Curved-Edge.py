#User function Template for python3

import heapq

class Solution:
    def shortestPath(self, n, m, a, b, edges):
        # code here 
        adj = [[] for _ in range(2 * n + 1)]
        for [x, y, w1, w2] in edges:
            adj[x].append((y, w1))
            adj[y].append((x, w1))
            adj[x].append((y + n, w2))
            adj[y].append((x + n, w2))
            adj[x + n].append((y + n, w1))
            adj[y + n].append((x + n, w1))
            
        visited = [False] * (n * 2 + 1)
        visited[a + n] = True
        heap = [(0, a)]
        while heap:
            d, i = heapq.heappop(heap)
            if i == b or i == b + n:
                return d
            if visited[i]:
                continue
            
            visited[i] = True
            for j, w in adj[i]:
                if not visited[j]:
                    heapq.heappush(heap, (d + w, j))
        return -1