#4.2.4.	Xâu liền xâu
s = input()

for i in range(len(s) - 1, -1, -1):
    s += s[i]
print(s)