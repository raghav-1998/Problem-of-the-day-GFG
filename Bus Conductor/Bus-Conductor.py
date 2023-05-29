#User function Template for python3

class Solution:
    def findMoves(self,n,chairs,passengers):
        chairs.sort()
        passengers.sort()
        moves = 0
        for i in range(n):
            diff = abs(chairs[i] - passengers[i])
            moves += diff
        return moves
