# Hàm print
# Hai số nguyên a, b
a = 10
b = 20
# In ra 2 số a, b cách nhau bởi dấu ";"
print(a, b, sep=";")

# In ra a và kết thúc bằng \t - tab
print(a, end="\t")
print(b)
print(100)

# In ra 1 chuỗi "Xin chào đên với khoá học "PythonForIoT" 2023"
print("Xin chào đến với khoá học \"PythonForIoT\" 2023")

# a "Số quả táo"
a = 10
s = ''
if a > 1 :
    s = 's'
# C1
print("You have {} apple{}".format(a, s))

# C2
print(f"You have {a} apple{s}")

# Định dạng tiền tệ
# VD: 100000 -> 100.000 đ

# Nhập 1 số tiền từ bàn phím -> in ra giá trị sau định dạng
x = int(input("Nhap so tien: "))

print("x = {:,.0f} VNĐ".format(x))
