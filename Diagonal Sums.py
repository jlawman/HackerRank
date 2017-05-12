
""""
Hackerrank:
Function to find the absolute difference between the sum of diagonals across an nxn matrix.
"""

def findDifOfDiagonals(n,a):
	rightDiagonal=0
	leftDiagonal=0
	for i in range(0,n):
		rightDiagonal+=a[i][i]
		leftDiagonal+=a[i][n-1-i]
	return abs(rightDiagonal-leftDiagonal)

