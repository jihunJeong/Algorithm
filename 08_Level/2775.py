import sys

"""
	2775번 BaekJoon
	
	divide - conquer Algorithm, Recursive Algorithm
"""

def CountPeople(k, n) :
	if k == 0 :
		return n
	elif n == 1 :
		return 1
	else :
		return CountPeople(k, n - 1) + CountPeople(k - 1, n)

t = int(input()) # Num of TestCase

for i in range(t) :
	k = int(input()) #Floor
	n = int(input()) #Num of Room

	print (CountPeople(k, n))