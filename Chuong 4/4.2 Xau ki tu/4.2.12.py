import re
s = input()
tong = 0
x = re.findall(r"\d+", s)
for i in x:
    tong += int(i)
print(tong)
