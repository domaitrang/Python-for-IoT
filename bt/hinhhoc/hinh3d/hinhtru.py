from math import pi
def the_tich(r:float, h:float)->float:
    """
    Hàm tính thể tích hình trụ
    Trả về -1 nếu kích thước không hợp lệ
    """
    if(r <= 0 or h <= 0):
        return -1
    return pi * r * r * h

