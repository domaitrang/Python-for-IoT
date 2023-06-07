# Các kiểu dữ liệu trong python

# Số, chuỗi, list, tuple, dictionary, set, objects....

# Các kiểu dữ liệu số: số nguyên, số thực và số phức

a = 5
print(a)
# Kiểm tra kiểu dữ liệu thông qua type
print(type(a))

# Số nguyên không có phần thập phân (lập trình)

# Số thực, hiểu đơn giản là các số có phần thập phân
b = 1.5
print(b, type(b))

# Số phức: z = a + bi (a phân thực, b phần ảo)
z1 = 1 + 2j
z2 = 3 + 4j
print(z1 + z2, type(z1))

# Tương tự có trừ, nhân, chia

# Vậy nhập từ bàn phím như thế nào?
# Python có hàm input() - mặc định nhập chuỗi str

# VD1: Nhập số nguyên a từ bàn phím, tăng a lên 5 đơn vị và in ra
a = int(input("Nhập a = ")) # "4" khác 4
print(a + 5)

# VD2: Nhập số nguyên b từ bàn phím??
b = float(input("Nhập b = "))
print("b = ",b)

# VD3: Nhập vào 2 số phức, in ra tích của chúng??
# Gợi ý: complex()
z1 = complex(input("z1 = "))
z2 = complex(input("z2 = "))
z = z1 * z2
print(z)
# Lưu ý khi nhập: đúng đinhj dạng, viết liền
z3 = 3j    + 4
print(z3)
print("Hello")
