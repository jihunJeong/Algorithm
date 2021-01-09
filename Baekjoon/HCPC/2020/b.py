import sys
import math

inp = sys.stdin.readline()
n = int(inp[:-1])

rea_chk = False
for i in range(1, len(inp)-1):
    chk = True
    if (n % (10**i)) // (10**(i-1)) == 0:
        continue
    num = n // (10**i) + (n % (10**i))*(10**(len(inp)-i-1))
    if num == n:
        continue
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num % i == 0:
            chk = False
            break
    if chk == True:
        rea_chk = True
        break

if rea_chk == True:
    print("YES")
else :
    print("NO")