def xaucondxdainhat(s):
    n = len(s)
    kq = ""

    for i in range(n):
        for j in range(i, n):
            chuoi_con = s[i:j + 1]
            if chuoi_con == chuoi_con[::-1]:  # Kiểm tra đối xứng
                if len(chuoi_con) > len(kq):
                    kq = chuoi_con

    return kq

# Nhập xâu từ người dùng
s = input()
result = xaucondxdainhat(s)
print(result)