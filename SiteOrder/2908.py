a, b = map(int, input().split())
new_a = a//100 + (a%10)*100 + ((a%100)-(a%10))
new_b = b//100 + (b%10)*100 + ((b%100)-(b%10))
print(max(new_b,new_a))