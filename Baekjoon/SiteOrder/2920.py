import sys
import math

ascending_list = [1, 2, 3, 4, 5, 6, 7, 8]
desending_list = [8, 7, 6, 5, 4, 3, 2, 1]\

input_list = list(map(int, sys.stdin.readline().split()))

if input_list == ascending_list:
	print("ascending")
elif input_list == desending_list:
	print("descending")
else :
	print("mixed")