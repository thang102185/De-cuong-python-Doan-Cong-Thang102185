import re

def doiXung(chuoi):
    s1 = ''.join(re.findall(r"[a-zA-Z]+|-?\d+", chuoi)).lower()
    return s1 == s1[::-1]

s1 = input()
s2 = input()

if doiXung(s1):
    print("true")
else:
    print("false")

if doiXung(s2):
    print("true")
else:
    print("false")