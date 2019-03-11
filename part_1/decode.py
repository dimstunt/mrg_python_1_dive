a = input().lower()
dec = input().lower()
tr = 'abcdefjhijklmnopqrstuvwxyz'

d = {dec[i]: chr(ord('a') + i) for i in range(26)}

print(''.join(d.setdefault(ch, ch) for ch in a))
