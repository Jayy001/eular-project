'''

Task Description :

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

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

print(sum(primes_leq(2000000)))
