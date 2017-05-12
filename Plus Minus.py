""" 
Challenge:
You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeroes in the array compared to its size.
"""

def findPositivesNegativesZeroes(arr):
	zeroes=0
	negatives=0
	positives=0
	numOfElts=len(arr)
	for num in arr:
		if num>0:
			positives+=1
		elif num<0:
			negatives+=1
		else:
			zeroes+=1
	return [positives/numOfElts,negatives/numOfElts,zeroes/numOfElts]


