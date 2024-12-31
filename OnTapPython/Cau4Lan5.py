import re

def chuanHoa(s):
    s = s.lower()
    x = re.findall(r'[,. A-Za-z]', s)
    capitalize_next = True
    result = ""

    for char in x:
        if capitalize_next and char.isalpha():
            result += char.upper()  # Viết hoa ký tự đầu tiên
            capitalize_next = False
        elif char.isalpha():
            result += char
        elif char == ',':
            result += char + ' '  # Thêm dấu phẩy và một dấu cách
            capitalize_next = False  # Ký tự tiếp theo sẽ không được viết hoa
        elif char == '.':
            result += char + ' '  # Thêm dấu chấm và một dấu cách
            capitalize_next = True  # Ký tự tiếp theo sẽ được viết hoa
        elif char == ' ':
            # Chỉ thêm dấu cách nếu ký tự trước đó không phải là dấu cách
            if result and result[-1] != ' ':
                result += ' '

    # Xóa dấu cách thừa ở cuối chuỗi
    result = ' '.join(result.split())  # Xóa dấu cách thừa giữa các từ
    print(result)
    
X = input()
Y = input()
chuanHoa(X)
chuanHoa(Y)