#User function Template for python3

from heapq import heapify, heappushpop

class Solution:
    def maxDiamonds(self, A, N, K):
        heap = [-diamonds for diamonds in A]
        heapify(heap)
        
        gain = 0
        for i in range(K):
            diamonds = heap[0]
            gain -= diamonds
            heappushpop(heap, -((-diamonds) // 2))
        return gain
