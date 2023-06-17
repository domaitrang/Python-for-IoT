from math import pi

def chu_vi(r: float) -> float:
    """ 
    Hàm tính chu vi hình tròn
    Trả về giá trị -1 nếu bán kính không hợp lệ
    """
    if (r <= 0):
        return -1
    return pi * 2 * r

def dien_tich(r:float)->float:
    """
    Hàm tính diện tích hình tròn
    Trả về giá trị -1 nếu bán kính không hợp lệ
    """
    if (r <= 0):
        return -1
    return pi * r**2
