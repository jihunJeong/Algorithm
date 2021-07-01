import math
from collections import Counter
from sys import maxsize

N = int(input())

num = []
for i in range(N):
    n = int(input())
    num.append(n)

num = sorted(num)
count = Counter(num)
mode = count.most_common(1)[0][1]

print(round(sum(num)/N))
print(num[N//2])

modes = []
for n, c in count.items():
    if c == mode:
        modes.append(n)
if len(modes) > 1:
    print(sorted(modes)[1])
else :
    print(sorted(modes)[0])
print(max(num)-min(num))