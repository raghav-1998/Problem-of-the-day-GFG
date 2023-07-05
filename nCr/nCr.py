#User function Template for python3

class Solution:
    def nCr(self, n, r):
        facto = [1]
        for i in range(1, 1001): 
            facto.append(facto[~0] * i)
            
        return (facto[n] // (facto[r] * facto[n - r])) % (10 ** 9 + 7)
        