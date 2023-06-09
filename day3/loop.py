# Vòng lặp for
# Cú pháp
# for e in interable:
    # câu lệnh 

# VD: in ra các giá trị 1 -> 10
# for(int i = 1; i<= 10; i++)

# range(start, stop, step = 1)
for i in range(1, 11): # [start, stop)
    print(i, end="\t")

# In ra các giá trị 2, 4, 6, 8, 10
# for (int i = 2; i < 11; i = i + 2)
print("\n")
for i in range(2, 11, 2):
    print(i, end="\t")

# Sử dụng vòng lặp duyệt qua các phần tử trong chuỗi kí tự

print()

for c in "hello":
    print(c, end="\t")

# Viết 1 chương trình cho phép nhập user, pass_word. 
# Tài khoản/ Mật khẩu mặc định là admin. -> nếu nhập quá 3 lần sẽ đưa thông báo -> 
# ko được truy cập
# Nếu nhập đúng -> "chào mừng, đăng nhập thành công!"

# Cú pháp 
#while dieu_kien:
    #khoi lenh khi dieu_kien dung


