def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    g = gcd(max(a, b), min(a, b))
    print(a*b//g)