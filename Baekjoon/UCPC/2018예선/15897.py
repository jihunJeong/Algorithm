import math
import sys

n = int(sys.stdin.readline())

chk = n
ans = n + 1
cnt = 0

for i in range(2, math.ceil(math.sqrt(n))):
	div = n / i
	
print(ans)