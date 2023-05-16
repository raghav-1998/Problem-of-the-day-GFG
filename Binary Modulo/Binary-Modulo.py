#User function Template for python3

class Solution():
    def modulo(self, s, m):
        #your code goes here
        n=len(s)
        num=0
        for i in range(n):
            num=(2*num+int(s[i]))%m
        
        return num