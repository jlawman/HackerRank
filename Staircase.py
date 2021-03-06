"""
Challenge:
Consider a staircase of size :

   #
  ##
 ###
####
Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .

Input Format

A single integer, , denoting the size of the staircase.

Output Format

Print a staircase of size  using # symbols and spaces.

Note: The last line must have  spaces in it.
"""
import sys
numRows=int(input().strip())

for rowNumber in range(1,numRows+1):
	line=""
	line+=" "*(numRows-rowNumber)
	line+="#"*(rowNumber)
	print(line)