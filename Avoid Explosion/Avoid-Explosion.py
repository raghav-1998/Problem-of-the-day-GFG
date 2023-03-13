#User function Template for python3

class Solution:
    def avoidExlosion(self, mix, n, danger, m):
        
        arr = [i for i in range(n+1)]
        def union(i, j):
            r1, r2 = find(i), find(j)
            if r1 != r2:
                arr[r1] = r2
            return r2
        def find(i):
            while i != arr[i]:
                i = arr[i]
            return i
            

        ans = []
        for x, y in mix:
            rx, ry = find(x), find(y)
            for p, q in danger:
                rp, rq = find(p), find(q)
                if (rx, ry) == (rp, rq) or (rx, ry) == (rq, rp):
                    ans.append("No")
                    break
            else:
                union(rx, ry)
                ans.append("Yes")
        return ans