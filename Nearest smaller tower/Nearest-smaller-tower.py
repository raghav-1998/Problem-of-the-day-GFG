#User function Template for python3

class Solution:
    def nearestSmallestTower(self,a):
        #code here
        n=len(a)
        k=[]
        t=min(a)
        for i in range(0,n):
            t1=0
            t2=0
            if a[i]==t:
                k.append(-1)
            else:
                if i+1<n:
                    for r in range(i+1,n):
                        if a[r]<a[i]:
                            t1=1
                            break
                if i-1>=0:
                    for l in range(i-1,-1,-1):
                        if a[l]<a[i]:
                            t2=1
                            break
                if t1==0:
                    k.append(l)
                elif t2==0:
                    k.append(r)
                elif abs(i-r)>(i-l):
                    k.append(l)
                elif abs(i-r)<(i-l):
                    k.append(r)
                else:
                    if a[r]>a[l]:
                        k.append(l)
                    elif a[l]>a[r]:
                        k.append(r)
                    else:
                        k.append(l)
        return k