"""summarize 4673

	- 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수
	- n을 d(n)의 생성자라고 한다.
	- 생성자가 없는 수를 셀프 넘버라고 한다.
"""

dn_list = list()

for i in range(1, 10001):
	pos1 = i // 10000
	pos2 = (i % 10000) // 1000
	pos3 = (i % 1000) // 100
	pos4 = (i % 100) // 10
	pos5 = i % 10

	dn = i + pos1 + pos2 + pos3 + pos4 + pos5
	dn_list.append(dn)

for i in range(1, 10001):
	if i not in dn_list:
		print(i)