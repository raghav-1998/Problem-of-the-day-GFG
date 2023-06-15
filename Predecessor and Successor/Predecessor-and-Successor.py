'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''


# This function finds predecessor and successor of key in BST.
# It sets pre and suc as predecessor and successor respectively


class Solution:
    
    def trav(self, root):
        
        if root == None:
            return
        
        self.trav(root.left)
        if root.key < self.key:
            self.left = root
            
        self.trav(root.right)
        if root.key > self.key and (self.right == None or root.key < self.right.key):
                    self.right = root
            
        
            
        
    def findPreSuc(self, root, pre, suc, key):
        # Your code goes here
        self.right = None
        self.left = None
        self.key = key
        
        self.trav(root)
        return (self.left, self.right)