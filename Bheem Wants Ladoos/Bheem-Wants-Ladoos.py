'''
# node class:

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

from collections import deque

class Solution:
    def ladoos(self, root, home, k):
        if root is None: return 0
        
        if not root.left and not root.right:
            if root.data==home: return root.data
            return 0

        temp, q, pos, len1, node = {}, deque(), 0, 1, None
        q.append(root)
        
        while pos<len1:
            if q[pos].data==home:
                node=q[pos]
                break

            if q[pos].left:
                q.append(q[pos].left)
                temp[q[pos].left], len1 = q[pos], len1+1
            
            if q[pos].right:
                q.append(q[pos].right)
                temp[q[pos].right], len1 = q[pos], len1+1
            
            pos+=1

        q, sum1,temp1 = deque(), 0, set()
        q.append([node, 0])
        while q:
            node, k1 = q.popleft()
            sum1+=node.data
            temp1.add(node)
            if node.left and k1<k and node.left not in temp1:q.append([node.left, k1+1])
            if node.right and k1<k and node.right not in temp1:q.append([node.right, k1+1])
            if node in temp and k1<k and temp[node] not in temp1:q.append([temp[node], k1+1])
        return sum1

