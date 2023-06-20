#User function Template for python3


from collections import Counter

class Solution:
    def update(self, a, n, updates, k):
        d = Counter(updates)
        a[0] = d[1]
        for x in range(1,n):
            a[x] = d[x+1] +a[x-1]
        return a


