# def ten_ham (danh_sach_tham_so):
#     # khoi lenh
#     # return (option)

# VD1: Viết 1 hàm tính tổng 2 số nguyên a và b

def tong(a: float, b: float) -> None:
    """ Hàm tính tổng hai số nguyên a và b """
    if (isinstance(a, float) or isinstance(a, int)) and (isinstance(b, float) or isinstance(b, int)):
        t = a + b
        print(t)
    else:
        print("Không hợp lệ")


# In ra tong 3, 4
tong(3, 4)
tong(10, -4.5)

tong("abc", "def")
# Hạn chế việc truyền sai kiểu dữ liệu ??? Làm thế nào?
# Viết document cho hàm


# VD2: Viết hàm tính chu vi của hình tròn.
# Xác định tham số: bán kính r (số thực) - điều kiện > 0
# Tên hàm: chu_vi_hinh_tron()
# Xác định giá trị trả về: -1 khi bán kính ko hợp lệ, ngược lại thì trả về chu vi của hình tròn (dương)


def chu_vi_hinh_tron(r: float) -> float:
    """Hàm tính chu vi hình tròn"""
    if (isinstance(r, int) or isinstance(r, float)) and r > 0:
        from math import pi
        cv = 2 * pi * r
        return cv

    return -1


print(chu_vi_hinh_tron(3))
print(chu_vi_hinh_tron(-2))
print(chu_vi_hinh_tron("abc"))


# Trong Python tham số có thể có các giá trị mặc định
def tinh_dien_tich_hinh_tron(r: float = 1) -> float:
    """Hàm tính diện tích hình tròn"""
    if (isinstance(r, int) or isinstance(r, float)) and r > 0:
        from math import pi
        dt = pi * r**2
        return dt

    return -1


# Tinh dien tich hinh tron co ban kinh bang 1
print(tinh_dien_tich_hinh_tron())

# Tinh dien tich hinh tron co ban kinh bang 3.5
print(tinh_dien_tich_hinh_tron(3.5))

# Viết hàm tính chu vi, diện tích hình chữ nhât có 2 tham số truyền vào
# chiều dài, chiều rộng, giá trị trả về là float
# -1: nếu ko hợp lệ, còn lại số thực dương chu vi, diện tích
# yêu cầu: có giới thiệu hàm, chỉ rõ kiểu dữ liệu của các tham số và giá trị trả về.

# Hàm python có thể trả về nhiều giá trị 1 lúc.


def hcn(chieu_dai: float = 1, chieu_rong: float = 1) -> tuple[float, float]:
    """ Hàm tính chu vi, diên tích hình chữ nhật """
    if ((isinstance(chieu_dai, int) or isinstance(chieu_dai, float)) and (isinstance(chieu_rong, int) or isinstance(chieu_rong, float))
       and chieu_dai > 0 and chieu_rong > 0):
        cv = (chieu_dai + chieu_rong) * 2
        dt = chieu_dai * chieu_rong
        return cv, dt
    return -1, -1


cv1, dt1 = hcn(4, 5)
cv2, _ = hcn(10, 20)
_ , dt3 = hcn(30, 10)

print(f"Chu vi {cv1}, dien tich {dt1}")
# Nếu chiều dài, chiều rộng có giá trị mặc định , (1, 1)?
# hcn() -> (1, 1)
# hcn(2) ?? măc định chièu dài = 2 -> do truyền đúng thứ tự
print(hcn(2))

# Vậy chỉ muốn đặt chiều rộng thì làm thế nào?
cv4, dt4 = hcn(chieu_rong=2)
print(f"Chu vi {cv4}, dien tich {dt4}")

# Viết 1 hàm tính tổng số nguyên, tham số truyền vào có thể 1 hoặc nhiều
# VD tong(1) => 1
# tong(1,2) => 3
# tong(4,5,6,7,8) =  ??


def tong(*nums):
    if(len(nums) == 0):
        print("Không hợp lệ")
    else:
        t = 0
        for n in nums:
            t += n
        print("Tổng  =",t)

tong(1)
tong(2, 3, 4)
tong(5, 6, 7, 8)
