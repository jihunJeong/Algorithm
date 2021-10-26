def find(docking, a):
    if docking[a] == a:
        return a
    
    return find(docking, docking[a])

def union(docking, a, b):
    a_root = find(docking, a)
    b_root = find(docking, b)

    if a_root > b_root:
        docking[a] = b_root
    else :
        docking[b] = a_root

G = int(input())
docking = [i for i in range(G+1)]

answer = 0
P = int(input())
for i in range(P):
    n = int(input())

    root = find(docking, n)
    if root == 0:
        break
    
    union(docking, root, root-1)
    answer += 1
print(answer)