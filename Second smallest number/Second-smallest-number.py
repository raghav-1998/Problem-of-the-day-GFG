#User function Template for python3

class Solution:
    def smallest_num(self,S , D):
        s = S - 1
        d = D
        ss = ""
        no_9 = s // 9 
        rem = s % 9 
        
        if(no_9 > 0):
            rem+=1
            ss = "9"*(no_9-1)
            ss = str(rem) + "8"+ ss
        elif(rem > 0 ):
            ss = str(1)+str(rem-1);
            
        if(len(ss) < D):
            ss = ("0" * (D - len(ss)) ) + ss 
        ss = str(int(ss[0])+1) + ss[1 : len(ss)]
        return ss;
            
        
    def secondSmallest(self, S, D):
        if(S == 1 or S >= 9*D or D == 1):
            return -1;
        else:
            return self.smallest_num(S , D)
