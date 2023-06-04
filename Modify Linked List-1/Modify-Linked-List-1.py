#User function Template for python3

class Solution:

    def modify_the_list(self, head):
        # code here
        p=head
        li=[]
        while(p):
            li.append(p.data)
            p=p.next
        n=len(li)
        k=li[:]
        for i in range(n//2):
            k[i]=li[n-i-1]-li[i]
        for i in range(n//2):
            k[n-i-1]=li[i]
        #print(k)
        p=Node(0)
        j=p
        for i in k:
            y=Node(i)
            p.next=y
            #print(p.data)
            p=p.next
            #print(p.data)
        return j.next

