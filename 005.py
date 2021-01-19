#/usr/bin/python3

''' Task Description

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

num = 2520
while True:
    num += 20
    for i in range(10,20):
        if num % i != 0:
            break
        if i == 19:
            print(f"Found --> {num}") ; exit(0)
