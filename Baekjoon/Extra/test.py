from sys import stdin
from collections import Counter

n = int(stdin.readline())
arr = []

avg = 0
center = 0
freqt = 0
rang = 0

for i in range(n):
    arr.append(int(stdin.readline()))

arr.sort()

avg = round(sum(arr) / len(arr))

center = arr[len(arr)//2]

cnt = Counter(arr)
freqt = cnt.most_common(2)
fre = freqt[0][0]

rang = max(arr)-min(arr)
if n == 1:
    fre = arr[0]
    print(avg)
    print(center)
    print(fre)
    print(rang)
else:
    if freqt[0][1] == freqt[1][1]:
        fre = freqt[1][0]
    print(avg)
    print(center)
    print(fre)
    print(rang)