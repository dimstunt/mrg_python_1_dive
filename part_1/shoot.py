cnt = int(input())

sum = 0

for i in range(cnt):
    a, b = [float(a) for a in input().split()]
    t = (a**2 + b**2)**0.5
    sum += int(max((11 if int(t) != t else 10) - t, 0))
print(sum)
