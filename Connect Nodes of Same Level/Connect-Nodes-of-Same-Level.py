#User function Template for python3


'''
:param root: root of the given tree
:return: none, just connect accordingly.
{
    # Node Class:
    class Node:
        def __init__(self,val):
            self.data = val
            self.left = None
            self.right = None
            self.nextRight = None
}
'''
from collections import deque

class Solution:
    def connect(self, root):
        
        dq = deque([root])
        levels = []
        while dq:
            level = []
            for _ in range(len(dq)):
                cur = dq.popleft()
                level.append(cur)
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            levels.append(level)
            
        for level in levels:
            for a,b in zip(level, level[1:]):
                a.nextRight = b