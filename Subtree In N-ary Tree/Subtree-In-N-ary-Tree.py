#User function Template for python3

'''
class Node:
    def __init__(self, key, children=None):
        self.key = key
        self.children = children or []
    
    def __str__(self):
        return str(self.key)
'''


class Solution:
    def cst(self,root ,sp):
        s=str(root.key)
        for y in root.children:
            s+=self.cst(y,sp)
        sp[s]=sp.get(s,0)+1
        return s 
         
    def duplicateSubtreeNaryTree(self, root):
        sp={}
        self.cst(root,sp)
        c=0
        for x  in sp:
            if sp[x]>1:
                c+=1
        return c 

