import heapq
import sys
class Node :
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        if self.a < other.a:
            return True
        elif self.a == other.a:
            return self.b < other.b
        else:
            return False

N = int(sys.stdin.readline())

hp = []
for _ in range(N):
    n = int(sys.stdin.readline())

    if n == 0:
        if hp:
            p = heapq.heappop(hp).b
            print(p)
        else :
            print(0)
    else :
        heapq.heappush(hp, Node(abs(n), n))
