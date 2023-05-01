#User function Template for python3

class Solution:
    def minimumNumber(self, n, arr):
        #code here
        def gcd(a, b):
            while b%a !=0 :
                t = a
                a = b%a
                b = t
            return a
        ans = arr[0]
        for i in range(1,n):
            ans = gcd(ans,arr[i])
        return ans