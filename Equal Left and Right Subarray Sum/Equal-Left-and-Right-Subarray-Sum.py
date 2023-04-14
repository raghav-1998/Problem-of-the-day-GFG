# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equalSum(self,A, N):
        # Your code here
        left=0
        right=sum(A)
        
        for i in range(N):
            if(left==right-A[i]):
                return i+1
            left+=A[i]
            right-=A[i]
        
        
        return -1