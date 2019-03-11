f_s = input().lower()
s_s = input().lower()

st = set()
for ch in s_s:
    if ch.isalpha() and ch not in st:
        st.add(ch)
        print(ch, ' '.join(str(i+1) for i, v in enumerate(f_s) if v == ch) or 'None')