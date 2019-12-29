"""summarize 2753

	Leap Year : 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때 

	Input case :
		첫째 줄 : 연도
"""

n = int(input())

check_leap_year = False

if n % 4 == 0:
	if n % 100 != 0 or n % 400 == 0:
		check_leap_year = True



if check_leap_year == True:
	print("1")
else :
	print("0")
