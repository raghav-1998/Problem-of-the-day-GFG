#User function Template for python3

class Solution():
    def no_of_subarrays(self,N,arr):
        count_0, count_subArr = 0, 0
        for i in range(N):
            if arr[i]==0:
                count_0 += 1
            else:
                count_subArr += ((count_0)*(count_0+1))//2
                count_0 = 0
        count_subArr += ((count_0)*(count_0+1))//2
        return count_subArr