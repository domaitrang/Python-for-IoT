# Viết 1 class HinhTron có thuộc tính bán kính (private), mặc định r = 1.0
# Có các phương thức:
# Khởi tạo
# setter, getter
# chu_vi(), dien_tich()

# Cần bắt tất cả lỗi về ngoại lệ có thể xảy ra.
# Chủ động ném ra 1 exception.

from math import pi

class HinhTron:
    def __init__(self, r = 1.0):
        self.__r = r
        if(r <= 0):
            # raise ~ throw
            raise Exception("Không thể khởi tạo đối tượng")
    
    def set_r(self,r):
        if(r <= 0):
             raise Exception("Bán kính phải là số dương")
        self.__r = r

    def get_r(self):
        return self.__r
    
    def chu_vi(self):
        return pi * 2 * self.__r
    
    def dien_tich(self):
        return pi* self.__r**2
    

ht1 = HinhTron(3)
print("Dien tich:",ht1.dien_tich())
    
ht2 = HinhTron(5)
print("Chu vi:",ht2.chu_vi())
ht2.set_r(1)
print("Chu vi:",ht2.chu_vi())
