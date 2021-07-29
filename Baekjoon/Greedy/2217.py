N = int(input())

rope = []
for i in range(N):
    rope.append(int(input()))

rope = sorted(rope)
ans = 0
for i in range(N):
    ans = max(ans, rope[i]*(N-i))
print(ans)