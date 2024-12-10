#7.	Viết hàm tính tổng các chữ số của một số nguyên.
def sumCS(n):
    if n < 0:
        n = -n
    sum = 0
    while n > 0:
        n1 = n % 10
        sum += n1
        n = n // 10
    return sum

n = int(input())
print(sumCS(n))