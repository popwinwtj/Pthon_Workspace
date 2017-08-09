num = list(range(1,11))
n = int(0)
while n < len(num):
    num[n] = num[n]**3
    n = n + 1
for n in num:
    print(n)