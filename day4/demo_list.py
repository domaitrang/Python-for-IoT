# List tương tự như Array bên các ngôn ngữ khác như C/C++, Java...

# Tạo 1 list
day_so = [1, 2, 3, 4, 5, 6]
print(day_so)
# Kiểm tra kiểu dữ liệu
print(type(day_so))

# Tạo 1 list lưu trữ các chuỗi
chuoi_str = ["hello","hi","how are you"]
#              0      1       2
# In ra "hi"
print(chuoi_str[1])

# Khá giống Array ? Vậy điểm khác biệt là gì?
my_list = [1, 2, 1.5, "hello","abc"]
print(my_list)

# List có thể lưu trữ được các giá trị khác loại

mix_list = ["abc",2,3,[5,6,7,8]]
print(mix_list)

# Lấy ra phần tử đầu tiên index = 0
print("Phần tử đầu tiên:", mix_list[0])
print("Phần tử cuối cùng:", mix_list[3])
# Lấy giá trị cuối theo chỉ số âm
print("Phần tử cuối cùng:", mix_list[-1])

# In ra số 8 ở trong mix_list ??
print(mix_list[3][3], mix_list[3][-1], mix_list[-1][-1])
# mix_list[3, 3]

# Lấy ra giá trị thứ 2 gần cuối -2
print(mix_list[-2])