#User function Template for python3


class Solution:
    def lemonadeChange(self, N, bills):
        cash={ 5:0 , 10:0, 20:0}
        for x in bills:
            cash[x]+=1
            if x==5:
                continue
            elif x==10:
                cash[5]-=1
            else:
                if cash[10]>0:
                    cash[10]-=1
                    cash[5]-=1
                else:
                    cash[5]-=3
            if cash[5]<0:
                return False
        return True

