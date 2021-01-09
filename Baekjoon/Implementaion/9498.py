import sys
import math

"""summary 9498

	9498번 : 시험 성적

	90 ~ 100 : A
	80 ~ 89  : B
	70 ~ 79  : C
	60 ~ 69  : D
	   ~ 59  : F
"""

score = int(input()) # test score, data type : int

if score < 60:
	print("F")
elif score < 70:
	print("D")
elif score < 80:
	print("C")
elif score < 90:
	print("B")
else :
	print("A")