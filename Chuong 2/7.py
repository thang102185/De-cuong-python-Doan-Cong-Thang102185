#7.	Tính S = 1/(1.2) + 1/(2.3) + 1/(3.4) + ….. + 1/(n.(n+1))
n = int(input())
s = 0
for i in range(1, n+1):
     s += 1 / (n * (n+1))
print(":.2f".format(s))