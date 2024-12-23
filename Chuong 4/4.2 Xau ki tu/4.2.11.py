import re
s = input().strip()
x = re.findall(r"-?\d+", s)
b = list(map(int, x))
m = max(b)
print(m)