#User function Template for python3


class Solution:
    
    def JobScheduling(self,Jobs,n):
        Jobs.sort(key=lambda x:x.profit,reverse=True)   
        ans=0
        day=0
        vis=[0]*(n+1)
        for i in range(n):
            tmp=Jobs[i].deadline
            while tmp>=1:
                if vis[tmp]==0:
                    ans+=Jobs[i].profit
                    day+=1
                    vis[tmp]=1
                    break
                tmp-=1
        return [day,ans]  
