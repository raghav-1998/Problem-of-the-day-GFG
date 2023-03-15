# Your task is to complete this function
# function should return max sum level in the tree
'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''
from collections import deque as dq
class Solution:
    def maxLevelSum(self, root):
        # Code here
        s=-float('inf')
        q=dq()
        q.append(root)
        while q:
            m=0
            n=len(q)
            for i in range(n):
                a=q.popleft()
                m+=a.data
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
            s=max(m,s)
        return s
