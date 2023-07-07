#User function Template for python3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def maxDepth(self,root):
        if root==None:
            return 0
        ls=self.maxDepth(root.left)
        rs=self.maxDepth(root.right)
        return max(ls,rs)+1
    