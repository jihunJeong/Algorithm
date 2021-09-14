N = int(input())

arr = []
for i in range(N):
    name, ko, en, math = input().split()
    arr.append([name, int(ko), int(en), int(math)])

arr = sorted(arr, key=lambda x : (-x[1], x[2], -x[3], x[0]))
for n in arr:
    print(n[0])