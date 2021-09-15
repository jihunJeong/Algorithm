from itertools import permutations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
for permutation in sorted(list(permutations(arr, M))):
    for num in permutation:
        print(num, end=" ")
    print()