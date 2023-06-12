# Demo slice

my_list = [1,2,3,4,5,6,7,8,9]

# Lấy ra sublist [6, 7, 8] ??

print(my_list[5:8]) #678

print(my_list[5:]) # ?? Lấy từ index = 5 tro ve sau: [6 7 8 9]

print(my_list[:5]) # ?? 1,2,3,4,5

# Tạo list mới chứa 3 giá trị cuối cùng của list ban đầu ???
# [n-3,n-2,n-1]

new_list = my_list[-3:]
print(new_list)

print(my_list[0:-1]) # ???