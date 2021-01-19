'''

Task Description :

The sum of the squares of the first ten natural numbers is, 385 - 1*1 + 2*2 etc

The square of the sum of the first ten natural numbers is, 3025 (1+2+3+4+5+6+7+8+9+10 = 55 * 55 = 3025)

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

19/01/20

'''

sums_of_100 = sum(range(101)) * sum(range(101))

sums = []

[sums.append(i*i) for i in range(0,101)]

print(25502500 - sum(sums))
