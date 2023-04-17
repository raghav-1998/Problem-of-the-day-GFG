
def compute_factorial(N, MOD):
    fact = [1]*(N+1)
    inv_fact = [1]*(N+1)
    for i in range(1, N+1):
        fact[i] = (fact[i-1]*i)%MOD
        inv_fact[i] = pow(fact[i], MOD-2, MOD)
    return fact, inv_fact
        
class Solution:
    MOD = 10**9 + 7
    fact, inv_fact = compute_factorial(10**5, MOD)
    
    def bestNumbers(self, N : int, A : int, B : int, C : int, D : int) -> int:
        if A == B:
            S = set(map(int, str(A*N)))
            return int(C in S or D in S)
      
        res = 0
        for x in range(N+1):
            y = N - x
            S = set(map(int, str(A*x + B*y)))
            if C in S or D in S:
                res = (res + Solution.fact[N] * Solution.inv_fact[x] * Solution.inv_fact[y]) % Solution.MOD
        
        return res
