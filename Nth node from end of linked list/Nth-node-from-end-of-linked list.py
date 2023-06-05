#User function Template for python3
'''
    Your task is to return the data stored in
    the nth node from end of linked list.
    
    Function Arguments: head (reference to head of the list), n (pos of node from end)
    Return Type: Integer or -1 if no such node exits.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''
#Function to find the data of nth node from the end of a linked list

def getNthFromLast(head,n):
    curr = head
    cnt = 0
    for i in range(n):
        curr=curr.next
        cnt+=1
        if curr==None:
            break
    if cnt<n:
        return -1
    prev = head
    while curr!=None:
        curr=curr.next
        prev=prev.next
    return prev.data
