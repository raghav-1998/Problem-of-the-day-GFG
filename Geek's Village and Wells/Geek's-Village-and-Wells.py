#User function Template for python3


from typing import List
from collections import deque

class Solution:
    def chefAndWells(self, n : int, m : int, l : List[List[str]]) -> List[List[int]]:
        res =[]
        dx = [1,-1,0,0]
        dy = [0,0,-1,1]
        for i in range(n):
            res.append([-1]*m)
        vis =[]
        for i in range(n):
            vis.append([False]*m)
            new = deque()
        for i in range(n):
            for j in range(m):
                if l[i][j]=='W':
                    new.append([i,j])
                    vis[i][j] = True
                if l[i][j]=='W' or l[i][j]=='N' or l[i][j]=='.':
                    res[i][j]=0
        
        dis = 2
        while len(new)>0:
            size = len(new)
            while size>0:
                size=size-1
                k =new.popleft()
                for i in range(4):
                    x = k[0]+dx[i]
                    y = k[1]+dy[i]
                    if x>=0 and y>=0 and x<n and y<m and vis[x][y]==False and l[x][y]!='N':
                        vis[x][y]=True
                        new.append([x,y])
                        if l[x][y]=='H':
                            res[x][y]=dis 
            dis =dis+2 
        
        return res
