#User function Template for python3

class Solution():
    def solve(self, a, b, c):
        #your code goes here
        maxNum = max(a,b,c)
        if(maxNum<=(2*(a+b+c-maxNum+1))):
            return a+b+c
        else:
            return -1