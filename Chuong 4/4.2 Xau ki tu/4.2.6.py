# from collections import Counter

# def demKiTu(s):
#     dem = Counter(s)
#     return dem

# s = input()

# kq = demKiTu(s)
# for char, count in kq.items():
#     print("'{0}': {1}".format(char, count), end = ', ')

s = input()

dem = {}
for i in s:
    if i in dem:
       dem[i] += 1
    else:
        dem[i] = 1
print("ket qua la ", end = "")
for key, value in dem.items():
    print("'{0}': {1}".format(key, value), end = ", ")