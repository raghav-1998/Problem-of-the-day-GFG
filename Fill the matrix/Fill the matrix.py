#User function Template for python3

class Solution:
    def minIteration(self, N, M, x, y):
        #code here
        top=x-1
        down=N-x
        left=y-1
        right=M-y
        
        return max(top+left,max(top+right,max(down+left,down+right)))