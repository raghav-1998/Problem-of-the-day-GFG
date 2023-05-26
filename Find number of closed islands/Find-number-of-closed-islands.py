#User function Template for python3

class Solution:
    def closedIslands(self, matrix, N, M):
        def dfs(i:int, j:int, G:list):
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                if i < 0 or j < 0 or i >= len(G) or j >= len(G[0]):
                    continue
                if G[i][j] == 0:
                    continue
                G[i][j] = 0
                stack.append((i+1, j))
                stack.append((i, j+1))
                stack.append((i-1, j))
                stack.append((i, j-1))
        n = N
        m = M
        G = matrix
        count = 0
        for i in range(n):
            for j in range(m):
                if i < 1 or j < 1 or i >= len(G) - 1 or j >= len(G[0]) - 1 and G[i][j]:
                    dfs(i,j,G)
                        
        for i in range(n):
            for j in range(m):
                if G[i][j]:
                    dfs(i,j,G)
                    count+=1
                        
        return count

