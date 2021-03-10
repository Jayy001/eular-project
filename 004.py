'''

Task description

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

19/01/2021 - Actully on the 14, but I lost it

'''

palindromes = set([])
for a in range(100,999):
    for b in range(100,999):
        num = a*b
        if "".join(list(reversed(str(num)))) == str(num):
            palindromes.append(a * b)
                
print(max(palindromes))
