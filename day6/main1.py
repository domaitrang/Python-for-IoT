# Sử dụng một số module sẵn có: math, base64

import my_package.math as math

# Tính sin góc 90 độ
print(math.sin(90))
# Tính cos góc 0 độ
print(math.cos(0))

# Python sẽ ưu tiên tìm module có trong project chương trình
# trước sau đó mới tìm ở trong module chuẩn.

# Đối với c/C++
# include < > -> import thư viên
# include "" -> import file người dùng định nghĩa