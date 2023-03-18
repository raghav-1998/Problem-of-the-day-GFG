#User function Template for python3

class Solution:
    def maxTripletProduct (self, arr,  n): 
        #Complete the function
        arr.sort()
        return max(arr[-1]*arr[-2]*arr[-3],arr[0]*arr[1]*arr[-1])
