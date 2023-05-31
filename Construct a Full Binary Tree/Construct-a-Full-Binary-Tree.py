#User function Template for python3

class TreeNode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        
class Solution:
    def constructBinaryTree(self, pre, preMirror, size):
        # code here
        def create_a_tree(left,right):
            if left>right:
                return None
            mid=(left+right)//2
            node=TreeNode(pre[left])
            node.left=create_a_tree(left+1,mid)
            node.right=create_a_tree(mid+1,right)
            return node
        root=create_a_tree(0,len(pre)-1)
        return root


