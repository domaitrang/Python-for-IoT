# Toán tử: các kí hiệu
# Trình biên dich, thông dịch -> toán tử -> thực hiện phép toán.

# 1. Toán tử số học: 
#  +, -, x, : (tóan) -> +, -, *, / (lập trình)
a = 11
b = 5
print("a + b = ", a + b)
print("a x b = ", a * b)
print("a : b = ", a / b)
# Phép chia lấy nguyên //, phép chia lấy dư (%)
print(a//b)
# 11 chia 5 dc 2 dư 1
print(a % b)
# Toán tử tính mũ : a ^ b => a ** b
print("3^2=", 3 ** 2)

# 2. Toán tử so sánh - toán tử quan hệ: > , <, >=, <=, ==, !=
# Trả về giá trị boolean: True hoặc False
print(a >= 5) #True
print(b < 8)  #True
print(a == b) #False

# 3. Toán tử gán VT = VP (giá trị vế phải gán cho vế trái)
x = 3
y = x
print(x, y)
# Gán cùng lúc nhiều giá trị: 
a, b = 5, 6
print(a, b)
# Hoán đổi 2 giá trị a, b
a, b = b, a
print(a, b)

# 4. Toán tử logic: and, or và not
# A and B: Đúng(True) khi cả hai cùng đúng
# A or B: Chỉ sai (True) khi cả hai cùng sai
# not A: phủ định của A

# Python ko dùng các kí hiệu && (and), || (or), ! (not)
print((5 > 6) and (7 < 8)) # False and True
print(not (5 > 6))


#5. Toán tử bit: AND (&), OR (|), XOR (^), NOT(!), LEFT_SHIFT(<<), RIGHT_SHIFT(>>)
# Ít dùng

a = 10
print(a, bin(a))
a = a << 2
print(a, bin(a))

#6. Toán tử thành viên (membership): in và not in
arr = [1,2,34,5,6,7,8]

print(8 in arr)
print(10 in arr)

#7. Toán tử đinh danh: is, not is
x = 5
y = x
z = y
print(x is z)

# z thay đổi, vậy x có thay đổi hay ko???
z = 6
print("x = ", x)
print("y = ", y)
print("z = ", z)

a = [1, 2, 3, 4]
b = a

print(a is b) # ??? True hay False
# b thay đổi, a có thay đổi ko ??
b[0] = 10
print(b)
print(a)