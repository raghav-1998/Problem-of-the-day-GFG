#User function Template for python3

from typing import List

class Solution:
    def uniqueRow(self, row, col, matrix):
        matrix_set = set()
        res = []
        for i in matrix:
            if str(i) not in matrix_set:
                matrix_set.add(str(i))
                res.append(i)
        return res

