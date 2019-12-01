import math



t = int(input()) #Num of TestCase

for i in range(t) :
	x1, y1, r1, x2, y2, r2 = map(int, input().split())

	distance_spot = (x1 - x2) ** 2 + (y1 - y2) ** 2 
	sum_radius = (r1 + r2) ** 2
	sub_radius = (r1 - r2) ** 2

	if distance_spot == 0 :
		if r1 == r2 :
			print ('-1')
		else :
			print ('0')

	else :
		#두 원의 중심과 만나는 점이 삼각형을 그린다고 했을 때 짧은 두 변의 합은 가장 긴 변보다 커야 한다
		if sum_radius == distance_spot or sub_radius == distance_spot :
			print('1')

		elif sum_radius > distance_spot and sub_radius < distance_spot :
			print('2')

		else :
			print('0')