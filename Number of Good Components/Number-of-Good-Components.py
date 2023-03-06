#User function Template for python3

import collections
from collections import deque
from collections import defaultdict

class Solution:
    def findNumberOfGoodComponent(self, V, adj):
        def solve(node,isVisited):
            if node in isVisited:
                return 0,0
            isVisited.add(node)
            res = 0 
            totalnode = 1
            for child in adj[node]:
                val,data = solve(child,isVisited)
                res = 1+val+res
                totalnode +=data
            return res,totalnode
            
        res = 0
        isVisited = set()
        for i in range(1,V+1):
            if i not in isVisited:
                val = solve(i,isVisited)
                if (val[1]*(val[1]-1) == val[0]):
                    res+=1
        return res