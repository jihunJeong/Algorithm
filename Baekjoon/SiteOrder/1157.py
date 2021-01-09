import sys
import operator

"""
strInput = sys.stdin.readline().upper()
alphabet_dict = dict()

# 여기서 알파벳 각각 몇개가 있는지 계산했다. 이때 조건문을 통해
# 기존에 있는 문자인지 아닌지 판별
for i in strInput:
	if i not in alphabet_dict.keys():
		alphabet_dict[i] = 1
	else :
		cnt = alphabet_dict.get(i)
		alphabet_dict.update({i : cnt + 1})

#단순히 최대값을 얻기 위해 큰 게 앞으로 오는 정렬 함수를 썼다.
result = sorted(alphabet_dict.items(), key=operator.itemgetter(1), reverse=True)

if result[0][1] == result[1][1]:
	print("?")
else :
	print(result[0][0])
"""

strInput = input().upper()
alphabet_list = list(set(strInput))		#set 함수에는 중복을 제거하는 기능 있다.
count_alphabet = []


# 중복이 제거된 알파벳 집합에 count 함수를 써서 갯수가 몇개인지 파악
for i in alphabet_list:
	count_alphabet.append(strInput.count(i))


# 최대값이 하나이면 출력이고 여러개면 그냥 특정 문자를 출력하면 되기 때문에
# 정렬 필요없다. 
if count_alphabet.count(max(count_alphabet)) >= 2:
	print("?")
else :
	print(alphabet_list[count_alphabet.index(max(count_alphabet))])
