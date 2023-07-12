import math

# Định nghĩa exception
class RadiusError(BaseException):
    def __init__(self, message=None):
        if (message is None):
            message = "Bán kính không hợp lệ"
        super().__init__(message)

# Viết hàm tính chu vi hình tròn
def tinh_chu_vi_hinh_tron(r):
    if isinstance(r, (int, float)):
        if (r <= 0):
            raise RadiusError()
    else:
        raise RadiusError("Bán kính phải là số")
    chu_vi = 2 * math.pi * r
    return chu_vi


print(tinh_chu_vi_hinh_tron(4))

