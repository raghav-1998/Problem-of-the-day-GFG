#User function Template for python3

# Tree Node
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
import sys

class Solution:
    
    #Function to find the least absolute difference between any node
    #value of the BST and the given integer.
    def __init__(self):
        self.minDiffVal = sys.maxsize
    def minDiff(self,root, K):
        if root == None:
            return self.minDiffVal
        if abs(root.data - K) < self.minDiffVal:
            self.minDiffVal = abs(root.data - K)
        if(root.data < K):
            return self.minDiff(root.right, K)
        if(root.data > K):
            return self.minDiff(root.left, K)
        return self.minDiffVal