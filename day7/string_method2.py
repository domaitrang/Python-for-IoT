# Một số phương thức tìm kiếm
s = "hello world, welcome to Python"

kw = input("Nhập từ khoá: ")
rs = s.find(kw)
if(rs== -1):
    print("Khong tim thay")
else:
    print("Vi tri bat dau:",rs )

# Kiem tra mot chuoi co bat đầu bằng 1 giá trị cụ thể hay ko

s1 = "hello"
print(s1.startswith('he'))

# end with, tuong tu start
print(s1.endswith("o"))