#User function Template for python3

class Solution:
    def unvisitedLeaves(self, N, leaves, frogs):
        # code here
        hashh = [False for _ in range(leaves+1)] 
        for frog in frogs : 
            if frog <= leaves and not hashh[frog] :
                for i in range(0, leaves+1, frog) : 
                    hashh[i] = True 
        return hashh.count(False)