#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    def maxDifferenceBST(self,root, target):
        #code here
        tg_node, root_sum = self.get_target_node(root, target, 0)
        if not tg_node:
            return -1
        
        leaf_sum = self.tg_to_leaf_sum(tg_node, 0)
        return root_sum - (leaf_sum - tg_node.data)
    
    def tg_to_leaf_sum(self, tg, sum_):
        if not tg:
            return float("inf")
        
        if not tg.left and not tg.right:
            return sum_ + tg.data
        
        return min(self.tg_to_leaf_sum(tg.left, sum_ + tg.data), 
                    self.tg_to_leaf_sum(tg.right, sum_ + tg.data))
    
    def get_target_node(self, node, target, sum_):
        if not node:
            return node, -1
        
        if node.data == target:
            return node, sum_
        
        if target < node.data:
            return self.get_target_node(node.left, target, sum_ + node.data)
        
        return self.get_target_node(node.right, target, sum_ + node.data)