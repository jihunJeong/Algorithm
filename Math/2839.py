"""summarize 2839

	2839번 : 설탕 배달

	Two cases : 3kg, and 5kg
	Total : Nkg (input)
	
	Answer : minimum count of case
	ex) N = 18kg -> 5kg * 3, 3kg * 1

	Exception : if cannot make Nkg with combining of two cases, print -1  
"""

import sys
import math


n = int(input()) # Total amount 3<= n <= 5000
cnt = 0 # Answer

"""Solution

n = case1 * cnt1 + case2 * cnt2
n = 5cnt1 + 3cnt2

cnt1 + cnt2 = cnt

We want smallest cnt

n = 5cnt1 + 3 * (cnt - cnt1)
n = 2cnt1 + 3cnt

So, if cnt1 is max and (n - 2cnt1) is multiple of 3, then cnt is min
"""

cnt1 = n // 5 # max count, no matter multiple

while cnt1 != 0:
	if (n - (cnt1 * 5)) % 3 == 0:
		cnt2 = (n - (cnt1 * 5)) // 3
		break

	cnt1 -= 1
	
if n == 3:
	print(1)
if cnt1 != 0:
	print(cnt1 + cnt2)
else :
	print(-1)