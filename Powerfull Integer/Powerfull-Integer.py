from typing import List
from collections import Counter


class Solution:
    def powerfullInteger(self, n : int, intervals : List[List[int]], k : int) -> int:
        counts = Counter()
        for start, end in intervals:
            counts[start] += 1
            counts[end + 1] -= 1
        current_count = 0
        powerfull_integer = -1
        for i in sorted(counts):
            # The last index will be +1 after the last interval
            # and will have negative change, hence we first
            # check if the current count is greater than "k"
            # which means that the previous integer "i - 1"
            # was the maximum one.
            if current_count >= k:
                powerfull_integer = i - 1
            current_count += counts[i]
        return powerfull_integer
