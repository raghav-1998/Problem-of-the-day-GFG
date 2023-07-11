#User function Template for python3

class Solution:
    def setSetBit(self, x, y, l, r):
        # code here
        
        if (l < 1 or r > 32):
            return x;
 
        maskLength = (int) ((1 << (r - l + 1)) - 1);
     
        mask = ((maskLength) << (l - 1)) & y
        x = x | mask
        return x