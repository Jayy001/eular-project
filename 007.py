'''

Task Description :

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

19/01/20  

'''

def primes_leq(n):
    sqrtn = int(n**0.5) # Squares to a half
    sieve = [True] * (n+1)
    sieve[0] = False
    sieve[1] = False
 
    for i in range(2, sqrtn+1):
        if sieve[i]:
            m = n//i - i
            sieve[i*i:n+1:i] = [False] * (m+1)
 
    sieve = [i for i in range(n+1) if sieve[i]]
    return sieve

print(primes_leq(1000000)[10000])

This was one of the hardest challenges - Note to learn more on this (Sieve of Eratosthenes)
