#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    
    def returnTotalGoodSubtrees(self, root, k):
        if not root:
            return [0,set()]
        leftPart = self.returnTotalGoodSubtrees(root.left, k)
        rightPart = self.returnTotalGoodSubtrees(root.right, k)
        
        myset = leftPart[1].union(rightPart[1])
        myset.add(root.data)
        goodSubtrees = leftPart[0]+rightPart[0]+1 if len(myset)<=k else leftPart[0]+rightPart[0]
        return [goodSubtrees, myset]
    
    def goodSubtrees(self, root, k):
        #code here
        return self.returnTotalGoodSubtrees(root, k)[0]

