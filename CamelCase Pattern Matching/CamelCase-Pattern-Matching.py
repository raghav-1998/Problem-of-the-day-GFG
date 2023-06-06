#User function Template for python3

class Solution:
    def CamelCase(self,N,D ,P):
        fn=[]
        for x in D:
            ans=""
            for i in x:
                if i.isupper()==True:
                    ans+=i
                if P==ans[:len(P)]:
                    fn.append(x)
                    break
        if fn :
            return fn
        else:
            return [-1]