inp = input()

alpha = []
number = []
for s in inp:
    if s.isalpha():
        alpha.append(s)
    else :
        number.append(int(s))

alpha = sorted(alpha)
print(''.join(s for s in alpha) + str(sum(number)))