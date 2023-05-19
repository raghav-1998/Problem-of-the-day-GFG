import math

class Solution:
    def minimumSum(self, s : str) -> int:
        l=len(s)
        if l%2==0:
            i=int(l/2)-1
            f=int(l/2)
        else:
            i=int((l-1)/2)
            f=int((l-1)/2)
        s=list(s)
        while i>=0 and f<l:
            if s[i]==s[f] and s[i]!="?":
                i-=1
                f+=1
                continue
            elif s[i]==s[f] and s[i]=="?":
                if i+1<f:
                    s[i]=s[i+1]
                    s[f]=s[i+1]
                else:
                    k=i-1
                    m=f+1
                    while k>=0 and m<l and s[k]=="?" and s[m]=="?":
                        k-=1
                        m+=1

                    if m>=l:
                        s[i]="a"
                        s[f]="a"
                    elif s[k]!="?":
                        s[i]=s[k]
                        s[f]=s[k]
                    else:
                        s[i]=s[m]
                        s[f]=s[m]

            elif s[i]=="?" and s[f]!="?":
                s[i]=s[f]
            elif s[i]!="?" and s[f]=="?":
                s[f]=s[i]
            else:
                return -1
            i-=1
            f+=1

        sum1=0
        i=0
        l=len(s)
        while i<l-1:
            sum1=sum1+abs(ord(s[i])-ord(s[i+1]))
            i=i+1
        return sum1


        

