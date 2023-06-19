# String
s = "  hello   "
a = "hello world"
# Kiểm tra id
print(id(s), id(a))
# -> Cơ bản string bất biến, việc gán lại giá trị chuỗi -> thực chất là tạo ra chuỗi mới
# rồi gán lại giá trị đó cho biến

# Một số phương thức trong chuỗi
# Viết hoa: 
s = s.upper()
print("Chuỗi viết hoa:", s)
# Viết thường
print("Chuỗi viết thường:",s.lower())

# Cắt khoảng trắng, cắt khoảng trắng đầu và cuối
print(s.strip())

# Thay thế các kí tự trong chuỗi
# Thay toàn bộ hello bằng hi?
a = a.replace("hello", "hi")
print(a, id(a))

b = "hi world"
print(id(b))

