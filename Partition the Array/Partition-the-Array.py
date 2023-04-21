#User function Template for python3
class Solution:
    def minDifference(self, N, A): 
    
        sums = [0]*(N+1)
        for i, e in enumerate(A):
            sums[i+1] = sums[i]+e
        
        def search(l, r):
            lo, hi = l, r
            while lo < hi:
                m = lo+(hi-lo)//2
                lp = sums[m+1]-sums[l]
                rp = sums[r+1]-sums[m]
   
                if lp >= rp:    # we are looking the first postion such that left-part >= right-part
                    hi = m
                else:
                    lo = m+1
     
            v1, v2 = sums[lo+1]-sums[l], sums[r+1]-sums[lo+1]
            if lo > l:   # we try left-part <= right-part
                v3, v4 = sums[lo] - sums[l], sums[r+1] - sums[lo]
                if abs(v2-v1) > abs(v4-v3): 
                    return min(v3, v4), max(v3, v4)
            return min(v1, v2), max(v1, v2)
        
  
        ans = float('inf')
        for i in range(1, N-2):
            minv1, maxv1 = search(0, i)
            minv2, maxv2 = search(i+1, N-1)
            ans = min(ans, max(maxv1, maxv2)-min(minv1, minv2))
        return ans
