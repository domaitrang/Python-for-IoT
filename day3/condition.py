# Nhập vào thông tin thời tiết
# Nếu trời mưa thì đi bốt
# Nếu trời không mưa đi giày thể thao

# thoi_tiet = input("Nhập thông tin thời tiết: ").lower()

# if thoi_tiet.find("mưa") != -1:
#     print("Đi bốt")
#     if thoi_tiet == "mưa to":
#         print("Đi ủng")

# else:
#     print("Đi giày thể thao")


# Khối if - else if - else... -> python: if - elif.. else

# VD: Viết 1 chương trình nhập vào số x, hỏi x là số âm hay dương.

# Viết theo 3 khối if, sử dụng if-else, sử dụng if-elseif-else

x = int(input("x = "))

# C1
if x < 0:
    print(f"{x} là số âm")
if x == 0:
    print(f"{x} là số ko âm, ko dương")
if x > 0:
    print(f"{x} là số dương")

# C2
if x > 0:
    print(f"{x} là số dương")
else:
    # x <= 0
    if(x == 0):
        print(f"{x} là số ko âm, ko dương")
    else:
        print(f"{x} là số âm")

# C3
if x > 0:
    print(f"{x} là số dương")
elif x == 0:
    print(f"{x} là số ko âm, ko dương")
else:
    print(f"{x} là số âm")

