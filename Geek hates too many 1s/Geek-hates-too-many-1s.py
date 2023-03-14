class Solution:
    def noConseBits(self, n: int) -> int:
        a = bin(n)
        i = 2
        b = a
        while i <= len(a):
            if a[i:i+3] == '111':
                b = a[:i+2] + '0' + a[i+3:]
                a = b
            i += 1
        return int(a, 2)
