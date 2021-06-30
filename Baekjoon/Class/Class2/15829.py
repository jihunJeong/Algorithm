l = int(input())
string = input()

ans = 0
for i in range(l):
    ans += ((ord(string[i])-96)*(31**i)) % 1234567891
    ans = ans % 1234567891

print(ans)