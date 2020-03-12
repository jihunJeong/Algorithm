x, y, w, h = map(int, input().split())
ans = 1001
ans = min(ans, x, y, w-x, h-y)
print(ans)