f_s = input().lower()
t = 'abcdefghijklmnopqrstuvwxyz'
print(''.join(sign for sign in t if sign in f_s))
