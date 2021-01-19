'''

Task Description

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''
def find_product(sum):
     for a in range(1, sum):
         for b in range(1, sum - a):
             c = sum - a - b
             if a**2 + b**2 == c**2:
                   print (a*b*c)
     print ('No such triplet exists!')

find_product(1000)
