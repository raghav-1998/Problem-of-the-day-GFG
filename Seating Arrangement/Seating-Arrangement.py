import math
from typing import List
class Solution:
    def is_possible_to_get_seats(self, n : int, m : int, seats : List[int]) -> bool:
        # code here
        if m==1 and seats[0]==0:
            n-=1
            seats[0]=1
        if m==2 and seats[0]==0 and seats[1]==0:
            n-=1
            seats[0]=1
            
        if n>math.ceil(m/2):
            return False
        if seats[0]==0 and seats[1]==0:
            seats[0]=1
            n-=1
        for i in range(1, m-1):
            if seats[i-1]==0 and seats[i]==0 and seats[i+1]==0:
                seats[i]=1
                n-=1
        
        if seats[m-1]==0 and seats[m-2]==0:
            seats[m-1]=1
            n-=1
        if n<=0:
            return True
        return False

