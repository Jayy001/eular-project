#/usr/bin/python3

''' Task Description

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

possible_num = 0
while True:
    failed = True
    possible_num += 1
    for i in range(1,20):
        if possible_num % i != 0:
            break
        if i == 20:
            print(possible_num)
            break