from random import randint

cnt = int(input())
a, b = input().split()
a = int(a)
b = b.upper()

t = []

if cnt < a:
    for i in range(cnt):
        lot = randint(1, a)
        while lot in t:
            lot = randint(1, a)
        t.append(lot)
        print("Победитель номер {} - \"{:0>6} {}\"".format(i + 1, lot, b))
else:
    for i in range(a):
        print("Победитель номер {} - \"{:0>6} {}\"".format(i + 1, i + 1, b))
