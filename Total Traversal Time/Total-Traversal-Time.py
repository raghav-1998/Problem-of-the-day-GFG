from typing import List


class Solution:
    def totalTime(self, n : int, arr : List[int], time : List[int]) -> int:
        # code here
        s=set()
        ans=0
        
        s.add(arr[0])
        for i in range(1,n):
            if arr[i] in s:
                ans+=time[arr[i]-1]
            else:
                ans+=1
            s.add(arr[i])
    
        return ans
