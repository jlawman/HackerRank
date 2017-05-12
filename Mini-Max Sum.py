""" 
Challenge:
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

"""

import sys

numbers=list(map(int, input().strip().split(' ')))

totalSum=sum(numbers)

differentSums=[totalSum-num for num in numbers]


print(sorted(differentSums)[0],sorted(differentSums)[-1])