#User function Template for python3


from collections import Counter
class Solution:
    def countSpecialNumbers(self, N, arr):
        # Code here
        arr.sort()
        d=Counter(arr)
        count=0
        for i in range(N):
            if d[arr[i]]>1:
                count+=1
            else:
                for j in range(i):
                    if arr[i]%arr[j]==0:
                        count+=1
                        break
                    j+=1
        return count