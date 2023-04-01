#User function Template for python3

from typing import List
from array import array

class Solution:
    def removeReverse(self, s: str) -> str:
        
        counter = array('I', [0] * 128)
        
        s_len = len(s)
        included = [True] * s_len
        
        for c in s:
            counter[ord(c)] += 1
        
        left = 0
        right = s_len - 1
        rev = False
        
        while left <= right:
            first = s[left]
            last = s[right]
            
            if not rev:
                if counter[ord(first)] > 1:
                    counter[ord(first)] -= 1
                    rev = not rev
                    included[left] = False
                left += 1
            else:
                if counter[ord(last)] > 1:
                    counter[ord(last)] -= 1
                    rev = not rev
                    included[right] = False
                right -= 1
        
        res = ''
        for i in range(s_len):
            if included[i]:
                res += s[i]
        
        if rev:
            res = res[::-1]
        
        return res