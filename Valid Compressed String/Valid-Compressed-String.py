#User function Template for python3

class Solution:
    def checkCompressed(self, s,t):
        i=0
        j=0

        slen=len(s)
        tlen=len(t)
        
        while i<slen and j<tlen:
            # print(i,j)
            if s[i]==t[j]:
                i+=1
                j+=1
            elif t[j].isdigit():
                num=0
                while j<tlen and t[j].isdigit():
                    c=int(t[j])
                    num=num*10+c
                    j+=1
                i=i+num
                    
            else:
                return 0
        
        if i==slen and j==tlen:
            return 1
        else:
            return 0
    
