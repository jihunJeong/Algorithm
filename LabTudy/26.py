import heapq

hp = []
N = int(input())

for i in range(N):
    heapq.heappush(hp, int(input()))
if N == 1:
    print(0)
    exit()
answer = 0
while len(hp) >= 2:
    num1, num2, = heapq.heappop(hp), heapq.heappop(hp)
    answer += (num1+num2)
    heapq.heappush(hp, num1+num2)
print(answer)