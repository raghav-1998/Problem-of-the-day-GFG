#User function Template for python3

class Solution:
    def union(self, head1,head2):
        # code here
        # return head of resultant linkedlist
        l=[]
        while head1!=None:
            l.append(head1.data)
            head1=head1.next
        while head2!=None:
            l.append(head2.data)
            head2=head2.next
        l=list(set(l))
        l.sort()
        a=Node(0)
        t=a
        for i in l:
            t.next=Node(i)
            t=t.next
        return a.next
