import sys
import math


"""summary 4963

	- 한 정사각형에서 가로, 세로 또는 대각선으로 연결이면 걸어갈 수 있는 사각형
	- 걸어갈 수 있는 사각형끼리는 하나의 섬으로 생각

	Input :
		첫번째 줄 : 0 < w, h <= 50  data type : int
		두번째 줄 부터 h 줄까지 : 1 -> land, 0 -> sea
		End of input : 0, 0
"""

while True:
	w, h = map(int, input().split())

	if w == 0 and h == 0:
		break

	for i in range(h):
		