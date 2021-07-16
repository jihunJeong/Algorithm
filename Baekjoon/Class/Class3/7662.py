import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    max_heap = []
    min_heap = []
    possible = [0 for _ in range(1000001)]
    for i in range(k):
        ty, n = sys.stdin.readline().split()
        n = int(n)

        if ty == "I":
            heapq.heappush(max_heap, (-n, i))
            heapq.heappush(min_heap, (n, i))
            possible[i] = 1
        elif ty == "D":
            if n == -1:
                while min_heap and not possible[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    n, k = heapq.heappop(min_heap)
                    possible[k] = 0
            else : 
                while max_heap and not possible[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    n, k = heapq.heappop(max_heap)
                    possible[k] = 0
        
    while min_heap and not possible[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not possible[max_heap[0][1]]:
        heapq.heappop(max_heap)
    if not min_heap and not max_heap:
        print("EMPTY")
    else :
        maximum, minimum = -heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0]
        print(f"{maximum} {minimum}")