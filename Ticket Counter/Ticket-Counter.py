
import math

class Solution:

    def distributeTicket(self, N : int, K : int) -> int:

        # Code Here

        a=int(N//K)

        if(K==1):

            return int(N//2)+1

        m=N%K

        if(a%2==0):

            a=math.ceil(a/2)

            r=N-a*K+1

            if(m):

                r=a*K+m

        else:

            r=math.ceil(a/2)*K

            if(m):

                r=N-int(a//2)*K-m+1

        return r

