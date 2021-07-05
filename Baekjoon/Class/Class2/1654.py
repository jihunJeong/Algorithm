K, N  = map(int, input().split())

num = []
for i in range(K):
    n = int(input())
    num.append(n)

maximum = max(num)
left, right = 1, maximum
ans = 0
while left <= right:
    middle = (left+right) // 2
    sum = 0
    for i in range(K):
        sum += num[i] // middle
    if sum < N:
        right = middle - 1
    else : 
        ans = middle
        left = middle + 1

print(ans)