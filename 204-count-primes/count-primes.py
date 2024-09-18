class Solution:
    def countPrimes(self, n: int) -> int:
        if n==2:
            return 0
        primes = [True] * n 
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n, p):
                    primes[i] = False
            p += 1
        prime_count = sum(1 for p in range(2, n) if primes[p])
        return prime_count
            
