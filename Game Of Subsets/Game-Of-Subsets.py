from typing import List


class Solution:
    def goodSubsets(self, n : int, arr : List[int]) -> int:
        # code here
        mod = int(1e9) + 7
        maskPrime = [0]*31
        primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
        # compute the prime masks
        for i in range(2, 31):
            if i % 4 == 0 or i % 9 == 0 or i == 25:
                continue
            mask = 0
            for j in range(10):
                if i % primeNumbers[j] == 0:
                    mask |= 1 << j
            maskPrime[i] = mask
    
        # compute power of 2 function
        def powerOfTwo(n):
            result, value = 1, 2
            while n != 0:
                if n & 1 == 1:
                    result = (result * value) % mod
                value = (value * value) % mod
                n >>= 1
            return result
    
        oneCount, count, dp = 0, [0]*31, [0]*1024
        dp[0] = 1
        # count number of 1s and prime factors in the array
        for element in arr:
            if element == 1:
                oneCount += 1
            elif maskPrime[element] != 0:
                count[element] += 1
    
        # compute number of good subsets
        for i in range(31):
            if count[i] == 0:
                continue
            for j in range(1024):
                if j & maskPrime[i] != 0:
                    continue
                dp[j | maskPrime[i]] = (dp[j | maskPrime[i]] + dp[j] * count[i]) % mod
    
        answer = sum(dp) % mod - 1
        if oneCount != 0:
            answer = (answer * powerOfTwo(oneCount)) % mod
        return answer
