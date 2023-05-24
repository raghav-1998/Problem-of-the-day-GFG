#User function Template for python3

import math
import re
class Solution:
    def cuts(self, s):
        d = {}
        def generate_binary_powers(n):
            base = 5
            exponent = 0
            power = 1
            
            while power <= n:
                binary = bin(power)[2:]  
                d[binary] = 1
                exponent += 1
                power = base ** exponent
                
        n = int(s,2)
        generate_binary_powers(n)
        sorted_list = sorted(d.items(), key=lambda x: len(x[0]), reverse=True)
        cnt = 0

        for item in sorted_list:
            key,value = item
            if len(s) == 0:
                return cnt
            pattern = str(key)
            matches = re.findall(pattern, s)
            if matches:
                s = s.replace(key,"")
                cnt += len(matches)
            
        if len(s) == 0:
            return cnt
        return -1