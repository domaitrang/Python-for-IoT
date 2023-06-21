# Lam theo huong thu tuc
def tinh_chu_vi(chieu_dai: float, chieu_rong: float) -> float:
    """Hàm tính chu vi hình chữ nhật"""
    return (chieu_dai + chieu_rong) * 2


def tinh_dien_tich(chieu_dai, chieu_rong):
    """Hàm tính diện tích hình chữ nhật"""
    return chieu_dai * chieu_rong


# Nhập dữ liệu từ bàn phím và tính
c_dai, c_rong = map(float, input("Chiều dài, chiều rộng: ").split(","))
# Tính chu vi, diện tích
print(
    f"Chu vi:{tinh_chu_vi(c_dai, c_rong)} , dien tich :{tinh_dien_tich(c_dai,c_rong)}")

# Làm thế nào để lưu trữ được 10 hình chữ nhật trong hướng thủ tục ???
# -> list [(3, 4), (5, 6), (7, 8)]....