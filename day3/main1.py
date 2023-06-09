# Kiểu dữ liệu Boolean : True, hoặc False

a = True
print(a)

b = 5 > 6
print(b)
# Hàm bool cho phép chuyển giá trị/ biến -> kiểu dữ liệu bool
# Đôi khi gây khó hiểu

print(bool(123)) # True
print(bool([]))  # False
print(bool(()))  # False
print(bool(0))   # False
print(bool(""))  # False

# Có thể áp dụng để xác định một biến ko phải là số 0 hoặc ko phải chuỗi, list... rỗng
