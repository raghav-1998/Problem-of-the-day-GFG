#User function Template for python3

class Solution: 
    def maxIntersections(self, lines, N):
        # Code here
        list=[]
        kist=[]
        for a in lines:
            list.append(a[0])
            kist.append(a[1])
        list.sort()
        kist.sort()
        i,j,ans,k=0,0,0,0
        
        while(i<N and j<N):
            if(list[i]<=kist[j]):
                k+=1
                ans=max(ans,k)
                i+=1
            else:
                k-=1
                j+=1
        return ans