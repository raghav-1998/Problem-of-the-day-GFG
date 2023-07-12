#User function Template for python3


class Solution:

    def maxIndexDiff(self,arr,n):
        #code here
        minIndex = [0] * n
        maxIndex = [0] * n
    
        minIndex[0] = 0
        for i in range(1, n):
            if arr[i] < arr[minIndex[i-1]]:
                minIndex[i] = i
            else:
                minIndex[i] = minIndex[i-1]
    
        maxIndex[n-1] = n-1
        for i in range(n-2, -1, -1):
            if arr[i] > arr[maxIndex[i+1]]:
                maxIndex[i] = i
            else:
                maxIndex[i] = maxIndex[i+1]
    
        maxDiff = -1
        i = j = 0
        while i < n and j < n:
            if arr[minIndex[i]] <= arr[maxIndex[j]]:
                maxDiff = max(maxDiff, maxIndex[j] - minIndex[i])
                j += 1
            else:
                i += 1
    
        return maxDiff