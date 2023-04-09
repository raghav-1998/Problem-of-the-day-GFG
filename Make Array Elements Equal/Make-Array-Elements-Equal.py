#User function Template for python3

class Solution:
    def minOperations(self, N):
        # Code here
        return (N//2)**2 if N%2 == 0 else (N//2)*(N//2+1)


