s = list(map(int, input().split(",")))

for num in s:
    if num % 2 != 0:
        print(num, end=" ")