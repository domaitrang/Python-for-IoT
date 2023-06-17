# Chương trình chính được thực hiện tại đây
# File main.py và example.py cùng cấp
import example

print("Số PI = ", example.PI)

x = example.sum(4, 5)
print("Tổng = ", x)

# C2: Import và đổi tên module -> hữu ích khi tên dài hoặc trùng tên
import hinhhoc as h

print("Chu vi hình tròn bán kính 5: ", h.cv_hinh_tron(5))

# C3: Import 1 phần của module: from...import....
from hinhhoc import dt_hinh_tron

print("Diện tích hình tròn bán kính 5: ", dt_hinh_tron(5))

# C4: Import 1phần và đôi tên dien_tich
from hinhhoc import dt_hinh_tron as dien_tich

print("Diện tích hình tròn bán kính 5: ", dien_tich(5))

# C5: Import tất cả bên trong module
# from hinhhoc import * 
# from hinhhoc1 import * 
# => Ko nên sử dụng ???
# VD 2 module trên có cùng 1 hàm tên giống nhau ??
# nên sử dụng 4 cách đầu tiên.
