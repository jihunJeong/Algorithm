N, M = map(int, input().split())

memo = []
for i in range(N):
    site, password = input().split()
    memo.append([site, password])

memo = sorted(memo, key=lambda x : x[0])
for i in range(M):
    find = input()
    left, right = 0, len(memo)-1
    while left <= right:
        middle = (left+right) // 2
        if memo[middle][0] == find:
            print(memo[middle][1])
            break
        
        if memo[middle][0] > find:
            right = middle-1
        elif memo[middle][0] < find:
            left = middle+1