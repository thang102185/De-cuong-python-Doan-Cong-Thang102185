def dem(s):
    hoa = 0
    thuong = 0
    so = 0

    for i in s:
        if i.isupper(): 
            hoa += 1
        elif i.islower():  
            thuong += 1
        elif i.isdigit():  
            so += 1

    return hoa, thuong, so

s = input()
hoa, thuong, so = dem(s)
print(hoa, thuong, so)
