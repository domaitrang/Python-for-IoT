# Sử dụng composition

from math import pi

class hinh_tron:
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh

    def chu_vi(self):
        return self.ban_kinh * 2 * pi

    def dien_tich(self):
        return self.ban_kinh ** 2 * pi

class hinh_tru:
    def __init__(self, chieu_cao, ban_kinh) -> None:
        self.chieu_cao = chieu_cao
        self.day = hinh_tron(ban_kinh=ban_kinh)
    
    def the_tich(self):
        return self.day.dien_tich() * self.chieu_cao
    
ht1 = hinh_tru(2, 1)
print("The tich hinh tru: ", ht1.the_tich())

# Tinh chu vi day
print(ht1.day.chu_vi())