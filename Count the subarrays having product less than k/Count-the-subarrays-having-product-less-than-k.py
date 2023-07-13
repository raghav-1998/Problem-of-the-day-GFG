#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, lis, n, k):
        #Code here
    
        count=0
        p=1
        start=0
        end=0
        while(end<n):
            p=p*lis[end]
            while((start<end)and p>=k):
                p=p//lis[start]
                start+=1
            
            if(p<k):
                l=1+(end-start)
                count+=l
            
            end+=1
        
        return count
