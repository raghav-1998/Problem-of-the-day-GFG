#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''


def su(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return root.data
    l = su(root.left)
    r = su(root.right)
    return root.data + l + r

def size(root):
    if root == None:
        return 0
    l = 1
    l += size(root.left)
    l += size(root.right)
    return l
    
def isbst(root, mini=float('-inf'), maxi=float('inf')):
    if root == None:
        return True
    if root.data >= maxi or root.data <= mini:
        return False
    left = isbst(root.left, mini, root.data)
    right = isbst(root.right, root.data, maxi)
    return left and right

def solve(root, target):
    mini = float('inf')
    if root == None:
        return mini
    if root.left == None and root.right == None:
        if root.data == target:
            return 1
    if isbst(root):
        l = 0
        s = su(root)
        if s == target:
            mini = min(mini, size(root))
    return min(mini, solve(root.left, target), solve(root.right, target))

class Solution:
    def minSubtreeSumBST(self, target, root):
        mini = solve(root, target)
        if mini == float('inf'):
            return -1
        else:
            return mini
