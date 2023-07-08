#User function Template for python3

class Solution:
    def nextHappy (self, N):
        # Base cases of squares of 1..9
        squares = dict((str(i), i**2) for i in range(10))
        
        def sum_of_squares(n):
            if n not in squares:
                n_sum = sum(squares[c] for c in str(n))
                squares[n] = n_sum
            return squares[n]
        
        visited = set()
        happy_candidate = N + 1
        while True:
            n = happy_candidate
            while n != 1:
                if n in visited:
                    break
                visited.add(n)
                n = sum_of_squares(n)
            else:
                return happy_candidate
            happy_candidate += 1


