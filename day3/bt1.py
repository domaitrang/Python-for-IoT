# Viết 1 chương trình cho phép nhập user, pass_word. 
# Tài khoản/ Mật khẩu mặc định là admin. -> nếu nhập quá 3 lần sẽ đưa thông báo -> 
# ko được truy cập
# Nếu nhập đúng -> "chào mừng, đăng nhập thành công!"

is_login = False

count = 3
while count > 0:
    # Nhập user, password
    user = input("Enter user: ")
    password  = input("Enter password: ")
    if(user == password == "admin"):
        is_login = True
        break
    count = count -1

if(is_login):
    print("chào mừng, đăng nhập thành công!")
else:
    print("không truy cập được")

# Trong Python ko có vòng lặp do-while, ko có swich-case

